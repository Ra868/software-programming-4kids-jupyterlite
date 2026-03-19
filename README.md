# Software Programming 4 Kids — JupyterLite

> Interactive JupyterLite platform for teaching Python, NumPy, and data science.
> Runs entirely in the browser — no installation required.

Live site: **https://Ra868.github.io/software-programming-4kids-jupyterlite/**

---

## 📚 Lessons

| Subject | Notebook |
|---------|----------|
| 🚀 Physics | [Projectile Motion](content/numpy/physics/projectile_motion.ipynb) |
| 🚀 Physics | [Atmospheric Pressure vs Altitude](content/numpy/physics/atmospheric_pressure.ipynb) |
| 🧪 Chemistry | [pH & H⁺ Ion Concentration](content/numpy/chemistry/pH_concentration.ipynb) |
| 🧪 Chemistry | [Radioactive Decay — Half-Life](content/numpy/chemistry/half_life.ipynb) |
| 💰 Math | [Compound Interest Calculator](content/numpy/math/compound_interest.ipynb) |

---

## 🚀 Getting the Live Site Up (do these steps in order)

### Step 1 — Merge the PR into `main`

The deploy workflow, notebooks, and all config live on this PR branch.
Merging it to `main` is required before anything else works.

### Step 2 — Switch GitHub Pages source to "GitHub Actions"

> ⚠️ This is a **one-time** click.  GitHub's default is "Deploy from a branch"
> which serves raw source files, not the built JupyterLite app.

1. Go to **Settings → Pages** in your repository:
   ```
   https://github.com/Ra868/software-programming-4kids-jupyterlite/settings/pages
   ```
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Click **Save** (if the button appears).

### Step 3 — Trigger the first deployment

Merging the PR already triggers the workflow automatically.  If it didn't run
(e.g. you changed the Pages source *after* merging), start it manually:

1. Click the **Actions** tab:
   ```
   https://github.com/Ra868/software-programming-4kids-jupyterlite/actions
   ```
2. Click **Deploy JupyterLite to GitHub Pages** in the left list.
3. Click **Run workflow → Run workflow**.

### Step 4 — Visit the live site

Wait about 2–3 minutes for the build to finish, then open:
```
https://Ra868.github.io/software-programming-4kids-jupyterlite/
```

You will be redirected automatically to the interactive JupyterLite interface
where students can write and run Python programs directly in the browser.

> **Browser requirements:** JupyterLite uses WebAssembly and Service Workers.
> It works in all modern browsers (Chrome 89+, Firefox 90+, Edge 89+, Safari 15+).
> Internet Explorer is not supported.

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| Workflow never appeared in Actions | Check **Settings → Pages → Source** is set to **GitHub Actions**, not "Deploy from a branch" |
| Build fails with `jupyter: command not found` | The pip install step failed — re-run the workflow; it usually succeeds on retry |
| Site shows a 404 | The first deployment hasn't finished yet — wait 2–3 minutes and refresh |
| Site shows raw file listings | Pages source is still set to "Deploy from a branch" — see Step 2 |

---

## 🔄 Adding or Updating Lessons

1. Edit or add `.ipynb` notebooks inside the `content/` folder.
2. Commit and push to `main`.
3. The GitHub Actions workflow rebuilds and redeploys the site automatically —
   no other action needed.

---

## 🖥️ Embedding in WordPress

Once your GitHub Pages site is live, you can embed it in any WordPress page.
There are two ways to do this — a quick **Custom HTML block** approach and a
reusable **shortcode plugin** approach.

### Quick embed (Custom HTML block)

1. In the WordPress block editor, add a **Custom HTML** block.
2. Paste the following code:

```html
<!-- JupyterLite — Interactive Coding Lessons -->
<div style="width:100%; height:900px; border:1px solid #ddd;
            border-radius:4px; overflow:hidden; background:#f8f8f8;">
  <iframe
    src="https://Ra868.github.io/software-programming-4kids-jupyterlite/lab/index.html?path=index.ipynb"
    style="width:100%; height:100%; border:none;"
    title="Interactive JupyterLite Coding Lesson"
    allow="clipboard-read; clipboard-write"
    sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals allow-downloads"
    loading="lazy">
  </iframe>
</div>
```

3. Save / publish the WordPress page.

### Reusable shortcode plugin

For embedding on multiple pages with a simple tag like
`[jupyterlite_embed notebook="numpy/physics/projectile_motion.ipynb"]`,
use the drop-in plugin in this repo's `wordpress/` folder.

📖 **See the full guide: [wordpress/README.md](wordpress/README.md)**

It covers:
- Installing and activating the plugin
- All shortcode attributes (`notebook`, `height`, `width`)
- Direct links for each individual lesson
- Troubleshooting common embedding problems
- Notes for WordPress.com hosted sites

---

## 🗂️ Repository Structure

```
software-programming-4kids-jupyterlite/
├── index.html                     ← GitHub Pages entry point
├── jupyter_lite_config.json       ← JupyterLite build configuration
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml             ← Automated build & deploy workflow
├── wordpress/
│   ├── jupyterlite-embed.php      ← Drop-in WordPress shortcode plugin
│   └── README.md                  ← Full WordPress embedding guide
└── content/                       ← All Jupyter notebooks
    ├── index.ipynb                ← Welcome / table of contents
    └── numpy/
        ├── physics/
        │   ├── projectile_motion.ipynb
        │   └── atmospheric_pressure.ipynb
        ├── chemistry/
        │   ├── pH_concentration.ipynb
        │   └── half_life.ipynb
        └── math/
            └── compound_interest.ipynb
```
