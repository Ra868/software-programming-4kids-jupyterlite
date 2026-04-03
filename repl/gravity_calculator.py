"""
Newton's Universal Law of Gravitation
Calculates acceleration due to Earth's gravity at various distances.

Formula: g = GM / r^2
where:
  G = gravitational constant (6.674e-11 N·m²/kg²)
  M = mass of Earth (5.972e24 kg)
  r = distance from Earth's center (meters)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

G = 6.674e-11
M_earth = 5.972e24
R_earth = 6.371e6

R_moon_orbit = 3.844e8
R_moon_surface = 1.737e6

locations = [
    ("Earth's Surface",          R_earth),
    ("10 km",                    R_earth + 1.0e4),
    ("15 km",                    R_earth + 1.5e4),
    ("20 km",                    R_earth + 2.0e4),
    ("100,000 km",               R_earth + 1.0e8),
    ("200,000 km",               R_earth + 2.0e8),
    ("300,000 km",               R_earth + 3.0e8),
    ("Moon's Surface\n(at Moon's orbital distance)", R_moon_orbit + R_moon_surface),
]

distances_m = np.array([loc[1] for loc in locations])
distances_km = distances_m / 1e3
distances_from_surface_km = (distances_m - R_earth) / 1e3

g_values = G * M_earth / distances_m**2
g_surface = g_values[0]

colors = [
    "#3fb950",
    "#ffa657",
    "#e3b341",
    "#f78166",
    "#d2a8ff",
    "#79c0ff",
    "#58a6ff",
    "#ff7b72",
]

r_plot = np.linspace(R_earth, R_moon_orbit + R_moon_surface + 5e6, 2000)
g_plot = G * M_earth / r_plot**2
r_plot_km = r_plot / 1e3

fig = plt.figure(figsize=(16, 11), facecolor="#0d1117")
fig.suptitle(
    "Acceleration Due to Earth's Gravity — Newton's Universal Law of Gravitation  |  g = GM/r²",
    fontsize=14,
    fontweight="bold",
    color="white",
    y=0.99,
)

gs = gridspec.GridSpec(
    2, 2,
    height_ratios=[2.0, 1.15],
    width_ratios=[1.6, 1],
    hspace=0.42,
    wspace=0.32,
    left=0.07, right=0.97,
    top=0.94, bottom=0.04,
)

# ── Main plot (full scale) ──────────────────────────────────────────────────
ax_main = fig.add_subplot(gs[0, 0])
ax_main.set_facecolor("#161b22")
ax_main.plot(r_plot_km / 1e3, g_plot,
             color="#58a6ff", linewidth=2.5, zorder=2, label="g(r)")
ax_main.set_title("Full Scale  (Surface → Moon)", color="#8b949e",
                  fontsize=10, pad=6)

far_indices = [0, 4, 5, 6, 7]
for i in far_indices:
    label, r_m = locations[i]
    r_km = r_m / 1e3
    g = g_values[i]
    ax_main.scatter(r_km / 1e3, g, color=colors[i], s=90, zorder=5)
    offset_x = 8
    offset_y = g + 0.06 * g_surface * max(0.05, 1 - far_indices.index(i) * 0.18)
    ax_main.annotate(
        label.replace("\n", " "),
        xy=(r_km / 1e3, g),
        xytext=(r_km / 1e3 + offset_x, offset_y),
        color=colors[i],
        fontsize=8,
        arrowprops=dict(arrowstyle="->", color=colors[i], lw=0.9),
        zorder=6,
    )

ax_main.set_xlabel("Distance from Earth's Center  (×10³ km)", color="#8b949e", fontsize=10)
ax_main.set_ylabel("Gravitational Acceleration  (m/s²)", color="#8b949e", fontsize=10)
ax_main.tick_params(colors="#8b949e", labelsize=8.5)
for sp in ax_main.spines.values():
    sp.set_edgecolor("#30363d")
ax_main.grid(True, color="#21262d", linestyle="--", linewidth=0.8, zorder=1)
ax_main.set_xlim(left=0)
ax_main.set_ylim(bottom=0)
ax_main.legend(facecolor="#161b22", edgecolor="#30363d", labelcolor="white", fontsize=8.5)

# ── Zoomed plot (near-Earth: surface to 50 km) ─────────────────────────────
ax_zoom = fig.add_subplot(gs[0, 1])
ax_zoom.set_facecolor("#161b22")

r_zoom = np.linspace(R_earth, R_earth + 6e4, 500)
g_zoom = G * M_earth / r_zoom**2
r_zoom_alt_km = (r_zoom - R_earth) / 1e3

ax_zoom.plot(r_zoom_alt_km, g_zoom, color="#58a6ff", linewidth=2.5, zorder=2)
ax_zoom.set_title("Zoomed  (Surface to 50 km altitude)", color="#8b949e",
                  fontsize=10, pad=6)

near_indices = [0, 1, 2, 3]
for i in near_indices:
    label, r_m = locations[i]
    alt_km = (r_m - R_earth) / 1e3
    g = g_values[i]
    ax_zoom.scatter(alt_km, g, color=colors[i], s=90, zorder=5)
    ax_zoom.annotate(
        label.replace("\n", " "),
        xy=(alt_km, g),
        xytext=(alt_km + 1.5, g - 0.0008 * (near_indices.index(i) + 1)),
        color=colors[i],
        fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color=colors[i], lw=0.9),
        zorder=6,
    )

ax_zoom.set_xlabel("Altitude above Earth's Surface  (km)", color="#8b949e", fontsize=10)
ax_zoom.set_ylabel("Gravitational Acceleration  (m/s²)", color="#8b949e", fontsize=10)
ax_zoom.tick_params(colors="#8b949e", labelsize=8.5)
for sp in ax_zoom.spines.values():
    sp.set_edgecolor("#30363d")
ax_zoom.grid(True, color="#21262d", linestyle="--", linewidth=0.8, zorder=1)
ax_zoom.set_xlim(-1, 52)

y_min = g_zoom[-1] - 0.001
y_max = g_zoom[0] + 0.003
ax_zoom.set_ylim(y_min, y_max)

# ── Table (spans both columns) ─────────────────────────────────────────────
ax_table = fig.add_subplot(gs[1, :])
ax_table.set_facecolor("#161b22")
ax_table.axis("off")

col_labels = [
    "Location",
    "Distance from\nEarth's Center (km)",
    "Altitude above\nEarth's Surface (km)",
    "Gravitational\nAcceleration (m/s²)",
    "Fraction of\nSurface g",
]

table_data = []
for i, (label, r_m) in enumerate(locations):
    short_label = label.replace("\n", " ")
    dist_center_km = f"{distances_km[i]:,.3f}" if distances_from_surface_km[i] < 1 else f"{distances_km[i]:,.0f}"
    alt_km = f"{distances_from_surface_km[i]:,.1f}" if distances_from_surface_km[i] < 100 else f"{distances_from_surface_km[i]:,.0f}"
    g_str = f"{g_values[i]:.6f}"
    frac = f"{g_values[i] / g_surface:.6f}"
    table_data.append([short_label, dist_center_km, alt_km, g_str, frac])

table = ax_table.table(
    cellText=table_data,
    colLabels=col_labels,
    cellLoc="center",
    loc="center",
    bbox=[0, 0, 1, 1],
)
table.auto_set_font_size(False)
table.set_fontsize(8.5)

header_color = "#1f6feb"
row_bg = ["#161b22", "#1c2128"]

for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor("#30363d")
    if row == 0:
        cell.set_facecolor(header_color)
        cell.set_text_props(color="white", fontweight="bold")
    else:
        cell.set_facecolor(row_bg[(row - 1) % 2])
        if col == 0:
            cell.set_text_props(color=colors[row - 1], fontweight="bold")
        else:
            cell.set_text_props(color="#c9d1d9")

output_path = "gravity_results.png"
plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {output_path}")

print("\n--- Gravity Results ---")
print(f"{'Location':<44} {'Distance (km)':>20} {'Altitude (km)':>14} {'g (m/s²)':>12} {'g/g_surface':>13}")
print("-" * 106)
for i, (label, r_m) in enumerate(locations):
    short = label.replace("\n", " ")
    print(f"{short:<44} {distances_km[i]:>20,.3f} {distances_from_surface_km[i]:>14.1f} {g_values[i]:>12.6f} {g_values[i]/g_surface:>13.6f}")
