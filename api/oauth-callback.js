import fetch from 'node-fetch';

export default async function handler(req, res) {
  const code = req.query.code || req.url && new URL(req.url, `https://${req.headers.host}`).searchParams.get('code');
  if (!code) {
    res.status(400).send('Missing code');
    return;
  }

  const client_id = process.env.GITHUB_OAUTH_CLIENT_ID;
  const client_secret = process.env.GITHUB_OAUTH_CLIENT_SECRET;
  if (!client_id || !client_secret) {
    res.status(500).send('OAuth not configured');
    return;
  }

  try {
    const tokenResp = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
      body: JSON.stringify({ client_id, client_secret, code })
    });
    const tokenJson = await tokenResp.json();
    if (!tokenJson.access_token) {
      res.status(400).json(tokenJson);
      return;
    }

    // Set cookie and redirect to admin dashboard
    const token = tokenJson.access_token;
    // cookie: HttpOnly, Secure when deployed, SameSite=Lax
    const maxAge = 60 * 60 * 24 * 7; // 7 days
    res.setHeader('Set-Cookie', `gh_token=${token}; HttpOnly; Path=/; Max-Age=${maxAge}; SameSite=Lax`);
    res.writeHead(302, { Location: '/admin/dashboard.html' });
    res.end();
  } catch (err) {
    console.error(err);
    res.status(500).send('OAuth exchange failed');
  }
}
