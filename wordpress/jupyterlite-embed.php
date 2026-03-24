<?php
/**
 * Plugin Name:  JupyterLite Embed
 * Plugin URI:   https://github.com/Ra868/software-programming-4kids-jupyterlite
 * Description:  Adds a [jupyterlite_embed] shortcode to embed the interactive
 *               JupyterLite coding lessons anywhere on your WordPress site.
 * Version:      1.0.0
 * Author:       Ra868
 * License:      MIT
 *
 * ── INSTALLATION ────────────────────────────────────────────────────────────
 * Option A — Drop-in plugin (recommended)
 *   1. Copy this file to  wp-content/plugins/jupyterlite-embed/jupyterlite-embed.php
 *   2. Go to WordPress Admin → Plugins → Installed Plugins
 *   3. Activate "JupyterLite Embed"
 *
 * Option B — Add to your child theme
 *   Paste the code below the "Plugin header" block into your child theme's
 *   functions.php (skip the header comment block).
 *
 * ── USAGE ───────────────────────────────────────────────────────────────────
 * Basic (loads the welcome/index notebook):
 *   [jupyterlite_embed]
 *
 * Open a specific notebook by its filename (files live flat in content/):
 *   [jupyterlite_embed notebook="projectile_motion.ipynb"]
 *   [jupyterlite_embed notebook="half_life.ipynb"]
 *   [jupyterlite_embed notebook="pH_concentration.ipynb"]
 *   [jupyterlite_embed notebook="atmospheric_pressure.ipynb"]
 *   [jupyterlite_embed notebook="compound_interest.ipynb"]
 *
 * Adjust the height (pixels) or width (CSS value):
 *   [jupyterlite_embed height="700"]
 *   [jupyterlite_embed height="1100" width="90%"]
 *   [jupyterlite_embed notebook="projectile_motion.ipynb" height="800"]
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Do not execute outside of WordPress.
}

/**
 * Render the [jupyterlite_embed] shortcode.
 *
 * Shortcode attributes:
 *   notebook  (string)  Filename of the .ipynb file (e.g. "projectile_motion.ipynb").
 *                       All notebooks live flat in the content/ folder.
 *                       Defaults to index.ipynb (the welcome page).
 *   height    (int)     Iframe height in pixels.  Default: 900.
 *   width     (string)  Iframe container width (any CSS value). Default: 100%.
 *
 * @param array $atts Shortcode attributes provided by the user.
 * @return string      HTML string containing the iframe wrapper.
 */
function jupyterlite_embed_shortcode( $atts ) {
    $atts = shortcode_atts(
        array(
            'notebook' => '',
            'height'   => '900',
            'width'    => '100%',
        ),
        $atts,
        'jupyterlite_embed'
    );

    $base_url = 'https://Ra868.github.io/software-programming-4kids-jupyterlite/';

    // Accept a flat filename only — strip any directory components so that
    // shortcodes like notebook="projectile_motion.ipynb" work correctly and
    // path-traversal attempts (e.g. "../../etc/passwd") are harmless.
    if ( ! empty( $atts['notebook'] ) ) {
        $src = $base_url . 'lab/index.html?path=' . rawurlencode( basename( $atts['notebook'] ) );
    } else {
        $src = $base_url . 'lab/index.html?path=index.ipynb';
    }

    // Sanitize attribute values before inserting into HTML.
    $src    = esc_url( $src );
    $width  = esc_attr( $atts['width'] );
    $height = absint( $atts['height'] );

    return sprintf(
        '<div style="width:%s; height:%dpx; border:1px solid #ddd; border-radius:4px; overflow:hidden; background:#f8f8f8;">'
        . '<iframe'
        . ' src="%s"'
        . ' style="width:100%%;height:100%%;border:none;"'
        . ' title="Interactive JupyterLite Coding Lesson"'
        . ' allow="clipboard-read; clipboard-write"'
        . ' sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals allow-downloads"'
        . ' loading="lazy"'
        . '>'
        . '</iframe>'
        . '</div>',
        $width,
        $height,
        $src
    );
}
add_shortcode( 'jupyterlite_embed', 'jupyterlite_embed_shortcode' );
