Admin UI for Jungle City

Overview
- Simple admin that authenticates via GitHub OAuth and commits edits/uploads to the repository.

Setup (Vercel or similar):
1. Create a GitHub OAuth App (https://github.com/settings/developers)
   - Homepage URL: https://<your-site>
   - Authorization callback URL: https://<your-site>/api/oauth-callback

2. In your deployment settings, add env vars:
   - GITHUB_OAUTH_CLIENT_ID
   - GITHUB_OAUTH_CLIENT_SECRET
   - GITHUB_REPO (optional, default: rahim324g/junglecity)

3. Deploy. Visit /admin to login and /admin/dashboard.html to edit files or upload images.

Notes
- Uploaded images are saved under public_html/lovable-uploads/ by default.
- This admin stores the GitHub token in an HttpOnly cookie (gh_token). Keep your site secure and use HTTPS in production.
- For more robust auth/session handling or permissions, integrate a proper session store.
