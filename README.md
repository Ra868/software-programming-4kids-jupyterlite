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

## 🚀 One-Time GitHub Pages Setup (required after merging the PR)

GitHub Pages must be told to use the **GitHub Actions** deployment source instead of a branch.
This is a one-time click in the repository settings.

### Step-by-step

1. Open your repository on GitHub:
   ```
   https://github.com/Ra868/software-programming-4kids-jupyterlite
   ```

2. Click the **Settings** tab (the gear icon, top-right area of the repo page).

3. In the left sidebar, click **Pages**
   (under *Code and automation*).

4. Under **Build and deployment → Source**, open the dropdown and choose
   **GitHub Actions**.
   > ⚠️ The default value is "Deploy from a branch" — change it to "GitHub Actions".

5. Click **Save** (if a Save button appears).

That's the entire manual step. GitHub will now run the
`.github/workflows/deploy.yml` workflow whenever you push to `main`, build
JupyterLite, and publish the result to GitHub Pages automatically.

### Trigger the first deployment

After saving the setting, push any small change (e.g., add a blank line to this
README) or use the **Run workflow** button:

1. Click the **Actions** tab in your repository.
2. Click **Deploy JupyterLite to GitHub Pages** in the left list.
3. Click **Run workflow → Run workflow**.

Wait about 2–3 minutes, then visit your live site:
```
https://Ra868.github.io/software-programming-4kids-jupyterlite/
```

---

## 🔄 Adding or Updating Lessons

1. Edit or add `.ipynb` notebooks inside the `content/` folder.
2. Commit and push to `main`.
3. The GitHub Actions workflow rebuilds and redeploys the site automatically —
   no other action needed.

---

## 🖥️ Embedding in WordPress

Once your GitHub Pages site is live, you can embed it in any WordPress page:

1. In the WordPress editor, add a **Custom HTML** block.
2. Paste the following iframe code, replacing the `src` URL if you use a custom domain:

```html
<div style="width:100%; height:900px; border:1px solid #ddd;">
  <iframe
    src="https://Ra868.github.io/software-programming-4kids-jupyterlite/"
    style="width:100%; height:100%; border:none;"
    allow="same-origin"
    sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
  </iframe>
</div>
```

3. Save / publish the WordPress page.

Visitors will see the full interactive JupyterLite interface and can run all
Python programs directly inside your WordPress page — no installation required.

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
