# Deploy Joseph Land to the web (GitHub Pages)

Your repo already has a workflow that builds and deploys the game. You only need to turn on GitHub Pages and point it at that workflow.

## One-time setup on GitHub

1. **Rename the repo to `josephland`** (so the site is at `https://datagod9000.github.io/josephland/`):
   - Open your repo → **Settings** → under **Repository name** change `2D_game_portfolio_website` to **josephland** → **Rename**.
   - Update your local remote:  
     `git remote set-url origin https://github.com/DataGod9000/josephland.git`

2. Open your repo: **https://github.com/DataGod9000/josephland**
3. Go to **Settings** → **Pages** (left sidebar).
4. Under **Build and deployment**:
   - **Source:** choose **GitHub Actions** (not “Deploy from a branch”).
5. Save. You don’t need to create a workflow; it’s already in the repo.

## Deploy (automatic and manual)

- **Automatic:** Every push to `main` runs the workflow and deploys the latest build.
- **Manual:** **Actions** tab → **Deploy to GitHub Pages** → **Run workflow** → **Run workflow**.

## Your live URL

After the first successful run:

**https://datagod9000.github.io/josephland/**

(If your GitHub username is different, replace `datagod9000` with it.)

## Using a custom domain (optional)

In **Settings** → **Pages**, you can add a custom domain. Then set `base: "/"` in `vite.config.js` and redeploy.
