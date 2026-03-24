# WordPress Embedding Guide

This guide explains two ways to embed the interactive JupyterLite lessons
into a WordPress page or post.

**Prerequisites:** The GitHub Pages site must already be live at
`https://Ra868.github.io/software-programming-4kids-jupyterlite/`
before you embed it.  See the [main README](../README.md) for the one-time
GitHub Pages setup step.

---

## Method 1 — Custom HTML Block (no plugin, quickest)

Use this method to embed the lessons on a single page or post without
installing anything extra.

### Step-by-step

1. Open the WordPress page or post you want to embed the lessons in
   (or create a new one).

2. In the block editor, click the **"+"** button to add a new block,
   search for **Custom HTML**, and insert it.

3. Paste the following code into the Custom HTML block:

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

4. Click **Save draft** or **Publish**.

5. Preview the page — the full JupyterLite interface loads inside the iframe.
   Students can write and run Python programs without leaving your site.

### Open a specific lesson directly

Replace the `src` URL to link directly to a specific notebook:

| Lesson | `src` URL |
|--------|-----------|
| Welcome / Index | `.../lab/index.html?path=index.ipynb` |
| Projectile Motion | `.../lab/index.html?path=projectile_motion.ipynb` |
| Atmospheric Pressure | `.../lab/index.html?path=atmospheric_pressure.ipynb` |
| pH & H⁺ Concentration | `.../lab/index.html?path=pH_concentration.ipynb` |
| Radioactive Decay | `.../lab/index.html?path=half_life.ipynb` |
| Compound Interest | `.../lab/index.html?path=compound_interest.ipynb` |

*(The base URL `...` is `https://Ra868.github.io/software-programming-4kids-jupyterlite`)*

### Adjust the height

Change `height:900px` in the wrapper `<div>` to any value that fits
your page layout (e.g. `700px`, `1100px`).

---

## Method 2 — Shortcode Plugin (reusable across all pages)

Use this method when you want to embed lessons on multiple pages or posts
with a simple shortcode like `[jupyterlite_embed]`.

### Installation

1. On your computer, locate the plugin file:
   ```
   wordpress/jupyterlite-embed.php   ← in this repository
   ```

2. Upload it to your WordPress host:
   - In WordPress Admin, go to **Plugins → Add New Plugin → Upload Plugin**.
   - Click **Choose File**, select `jupyterlite-embed.php`, then click
     **Install Now**.
   - Click **Activate Plugin**.

   *Alternatively*, copy the file to
   `wp-content/plugins/jupyterlite-embed/jupyterlite-embed.php` via FTP or
   your host's File Manager, then activate it from **Plugins → Installed Plugins**.

### Shortcode usage

Once the plugin is active, use the shortcode in any page, post, or widget:

```
[jupyterlite_embed]
```

This embeds the full JupyterLite interface (welcome page) at the default
900 px height.

#### Open a specific notebook

```
[jupyterlite_embed notebook="projectile_motion.ipynb"]
[jupyterlite_embed notebook="half_life.ipynb"]
[jupyterlite_embed notebook="pH_concentration.ipynb"]
[jupyterlite_embed notebook="atmospheric_pressure.ipynb"]
[jupyterlite_embed notebook="compound_interest.ipynb"]
```

#### Adjust height and width

```
[jupyterlite_embed height="700"]
[jupyterlite_embed height="1100" width="90%"]
[jupyterlite_embed notebook="projectile_motion.ipynb" height="800"]
```

| Attribute  | Default  | Description |
|------------|----------|-------------|
| `notebook` | *(index)* | Filename of a `.ipynb` file in the flat `content/` folder |
| `height`   | `900`    | Iframe height in pixels |
| `width`    | `100%`   | Container width (any CSS value) |

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Blank iframe / "refused to connect" | GitHub Pages site not yet deployed | Complete the [GitHub Pages setup](../README.md#-one-time-github-pages-setup-required-after-merging-the-pr) first |
| Iframe shows but Python doesn't run | Browser blocks cross-origin service workers in some configurations | Advise students to open `https://Ra868.github.io/software-programming-4kids-jupyterlite/` directly in a new tab |
| WordPress strips the `<iframe>` tag | Some security plugins remove iframes | Use the shortcode method (Method 2) which bypasses this restriction |
| Iframe is too short / scrolls inside | Default height doesn't match your content | Add `height="1100"` (or larger) to the shortcode, or change `height:900px` in the Custom HTML |

---

## Notes for WordPress.com hosted sites

WordPress.com free and personal plans do not allow custom HTML or plugins
from third parties.  You have two options:

1. **Upgrade to a Business plan** — this allows custom HTML blocks and plugin
   uploads.
2. **Link instead of embed** — add a button or hyperlink that opens the
   JupyterLite site in a new tab:
   ```html
   <a href="https://Ra868.github.io/software-programming-4kids-jupyterlite/"
      target="_blank" rel="noopener noreferrer">
     ▶ Open Interactive Coding Lessons
   </a>
   ```
