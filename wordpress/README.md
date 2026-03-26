# WordPress Embedding Guide

This guide explains how to embed the interactive JupyterLite lessons
into a WordPress page or post using the shortcode plugin.

**Prerequisites:** The GitHub Pages site must already be live at
`https://Ra868.github.io/software-programming-4kids-jupyterlite/`
before you embed it.  See the [main README](../README.md) for the one-time
GitHub Pages setup step.

**Notebook structure:** All notebooks live in a flat `content/` folder —
no subfolders. Reference them by filename only (e.g., `projectile_motion.ipynb`).

---

## Installation

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

---

## Shortcode Usage

Once the plugin is active, use the shortcode in any page, post, or widget.

### Basic (loads the welcome/index notebook)

```
[jupyterlite_embed]
```

### Open a specific notebook

Reference notebooks by filename only:

```
[jupyterlite_embed notebook="projectile_motion.ipynb"]
[jupyterlite_embed notebook="projectile_motion.ipynb" title="Projectile Motion"]
[jupyterlite_embed notebook="pH_concentration.ipynb" title="pH & H⁺ Concentration" height="800"]
[jupyterlite_embed notebook="half_life.ipynb" title="Radioactive Decay"]
[jupyterlite_embed notebook="atmospheric_pressure.ipynb" title="Atmospheric Pressure"]
[jupyterlite_embed notebook="compound_interest.ipynb" title="Compound Interest"]
```

### Adjust height and width

```
[jupyterlite_embed height="700"]
[jupyterlite_embed height="1100" width="90%"]
```

### Shortcode attributes

| Attribute  | Default   | Description |
|------------|-----------|-------------|
| `notebook` | *(index)* | Filename of a `.ipynb` file in the flat `content/` folder |
| `title`    | *(none)*  | Optional display title for documentation purposes |
| `height`   | `900`     | Iframe height in pixels |
| `width`    | `100%`    | Container width (any CSS value) |

---

## Notebook structure

All notebooks are stored flat in the `content/` folder:

```
content/
├── index.ipynb
├── projectile_motion.ipynb
├── pH_concentration.ipynb
├── half_life.ipynb
├── atmospheric_pressure.ipynb
└── compound_interest.ipynb
```

To add a new notebook, place the `.ipynb` file directly in `content/` and
reference it in the shortcode by filename.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Blank iframe / "refused to connect" | GitHub Pages site not yet deployed | Complete the [GitHub Pages setup](../README.md) first |
| Notebook not found / file browser shown instead | Filename typo in shortcode | Double-check the filename matches exactly (case-sensitive) |
| Iframe shows but Python doesn't run | Browser blocks cross-origin service workers in some configurations | Advise students to open `https://Ra868.github.io/software-programming-4kids-jupyterlite/` directly in a new tab |
| WordPress strips the `<iframe>` tag | Some security plugins remove iframes | Use the shortcode method which bypasses this restriction |
| Iframe is too short / scrolls inside | Default height doesn't match your content | Add `height="1100"` (or larger) to the shortcode |

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
