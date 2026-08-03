export default function handler(req, res) {
  const clientId = process.env.GITHUB_OAUTH_CLIENT_ID || '';
  const repo = process.env.GITHUB_REPO || 'rahim324g/junglecity';
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({ client_id: clientId, repo }));
}
