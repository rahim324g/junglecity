import fetch from 'node-fetch';

function parseCookies(header) {
  const obj = {};
  if (!header) return obj;
  header.split(';').forEach(c => {
    const [k,v] = c.split('=').map(s => s && s.trim());
    if (k) obj[k] = v || '';
  });
  return obj;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end('Method not allowed');
  const cookies = parseCookies(req.headers.cookie || '');
  const token = cookies.gh_token || req.headers['authorization'] && req.headers['authorization'].replace('Bearer ', '');
  if (!token) return res.status(401).json({ error: 'Not authenticated' });

  const { path, content, message, branch } = req.body || {};
  if (!path || typeof content !== 'string') return res.status(400).json({ error: 'Missing path or content' });

  const [owner, repo] = (process.env.GITHUB_REPO || 'rahim324g/junglecity').split('/');
  const apiBase = `https://api.github.com/repos/${owner}/${repo}/contents/${encodeURIComponent(path)}`;

  try {
    // Check if file exists to get sha
    const getResp = await fetch(apiBase + (branch ? `?ref=${branch}` : ''), {
      headers: { Authorization: `token ${token}`, Accept: 'application/vnd.github+json' }
    });

    let sha = null;
    if (getResp.status === 200) {
      const j = await getResp.json();
      sha = j.sha;
    }

    const putResp = await fetch(apiBase, {
      method: 'PUT',
      headers: { Authorization: `token ${token}`, Accept: 'application/vnd.github+json', 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message || `Update ${path}`, content: Buffer.from(content, 'utf8').toString('base64'), sha, branch: branch || 'main' })
    });

    const putJson = await putResp.json();
    if (!putResp.ok) return res.status(putResp.status).json(putJson);
    res.json({ ok: true, result: putJson });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Commit failed' });
  }
}
