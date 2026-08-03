Deployment package: `junglecity-public_html.zip`

Contents:
- Full static site located in `public_html/` (HTML, assets, images).

Quick deploy options:

1) Upload the zip to your static host (Netlify, Vercel, S3 + CloudFront):
   - Unzip on host or set the host's upload root to the extracted `public_html` contents.

2) For simple FTP/SFTP upload to a server:
   - Unzip locally and upload contents of `public_html/` to the server document root.

3) To serve locally for testing:

```bash
python3 -m http.server 8000 --directory public_html
```

4) To push to a Git remote (GitHub/GitLab):
   - Create a repo on the remote service, then:

```bash
git remote add origin <REMOTE_URL>
git branch -M main
git push -u origin main
```

Netlify automated deploy via GitHub Actions
-----------------------------------------

1. Create a site on Netlify and note the `Site ID` (Site settings → Site information).
2. Create a personal access token on Netlify (User Settings → Applications → Personal access tokens).
3. In your GitHub repository, add two repository secrets:
   - `NETLIFY_AUTH_TOKEN` = your Netlify personal access token
   - `NETLIFY_SITE_ID` = your Netlify Site ID
4. Push this repository to GitHub (see step 4). On push to `main`, GitHub Actions will run the workflow `.github/workflows/deploy-netlify.yml` and deploy `public_html` to Netlify.

Notes:
- The workflow installs `netlify-cli` and runs `netlify deploy --dir=public_html --prod`.
- If you prefer preview deploys on PRs, I can update the workflow to deploy to Netlify previews as well.

Notes:
- I did not add the zip to Git. If you want it committed, I can add it.
- If you'd like a CI pipeline (GitHub Actions) to auto-deploy on push, I can scaffold one.
