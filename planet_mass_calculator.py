"""
Planet Mass Calculator using Newton's Universal Law of Gravitation
=================================================================

Newton's Law: F = G * M * m / r^2
At the surface: F = m * g  =>  g = G * M / R^2
Solving for mass: M = g * R^2 / G

Planets analyzed: Mercury, Venus, Earth, Mars, Jupiter
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── Gravitational Constant ─────────────────────────────────────────────────────
G = 6.674e-11  # N·m²/kg²

# ── Planet Data ───────────────────────────────────────────────────────────────
# Surface gravity (m/s²) and mean radius (m) for each planet
planets = np.array([
    # name          g (m/s²)   R (m)         known_mass (kg)    color
    # stored separately below
])

names             = np.array(["Mercury", "Venus",    "Earth",    "Mars",     "Jupiter"])
surface_gravity   = np.array([3.70,       8.87,       9.81,       3.71,       24.79  ])  # m/s²
radii             = np.array([2.4397e6,   6.0518e6,   6.3710e6,   3.3895e6,   7.1492e7])  # m
known_masses      = np.array([3.3011e23,  4.8675e24,  5.9720e24,  6.4171e23,  1.8982e27])  # kg
colors            = ["#b5b5b5", "#e8cda0", "#4a90d9", "#c1440e", "#c88b3a"]

# ── Newton's Law Calculation (vectorised with NumPy) ──────────────────────────
#   M = (g × R²) / G
calculated_masses = (surface_gravity * radii**2) / G

# ── Error Analysis ────────────────────────────────────────────────────────────
percent_error = np.abs(calculated_masses - known_masses) / known_masses * 100

# ── Print Tabular Results ─────────────────────────────────────────────────────
print("=" * 90)
print(" Newton's Universal Law of Gravitation  —  Planet Mass Calculation")
print(" Formula: M = (g × R²) / G    |    G = 6.674 × 10⁻¹¹ N·m²/kg²")
print("=" * 90)
header = f"{'Planet':<10} {'g (m/s²)':>10} {'R (m)':>12} {'Calc. Mass (kg)':>18} {'Known Mass (kg)':>18} {'Error %':>9}"
print(header)
print("-" * 90)
for i in range(len(names)):
    def sci(val):
        exp = int(np.floor(np.log10(abs(val))))
        mantissa = val / 10**exp
        return f"{mantissa:.3f}×10^{exp}"
    print(
        f"{names[i]:<10} {surface_gravity[i]:>10.2f} {radii[i]:>12.3e} "
        f"{sci(calculated_masses[i]):>18} {sci(known_masses[i]):>18} "
        f"{percent_error[i]:>8.5f}%"
    )
print("=" * 90)
print(f"\nG (gravitational constant) = {G:.3e} N·m²/kg²")
print(f"Largest planet  → {names[np.argmax(calculated_masses)]} ({calculated_masses.max():.3e} kg)")
print(f"Smallest planet → {names[np.argmin(calculated_masses)]} ({calculated_masses.min():.3e} kg)")
print(f"Max error: {percent_error.max():.5f}%  (all values agree with accepted data to < 0.5%)\n")

# ── Plotting ──────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle(
    "Planet Mass via Newton's Law of Gravitation\n"
    r"$M = \frac{g \cdot R^2}{G}$",
    fontsize=14, fontweight="bold", y=1.02
)

x = np.arange(len(names))
bar_width = 0.6

for ax, scale, title in zip(
    axes,
    ["linear", "log"],
    ["Linear Scale", "Logarithmic Scale (base 10)"]
):
    bars = ax.bar(x, calculated_masses, width=bar_width, color=colors, edgecolor="white", linewidth=0.8)

    ax.set_yscale(scale)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=11)
    ax.set_xlabel("Planet", fontsize=12)
    ax.set_ylabel("Mass (kg)", fontsize=12)
    ax.set_title(title, fontsize=12, pad=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    if scale == "linear":
        # Annotate bars with scientific notation
        for bar, mass in zip(bars, calculated_masses):
            exp = int(np.floor(np.log10(mass)))
            mantissa = mass / 10**exp
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() * 1.02,
                f"{mantissa:.2f}×10^{exp}",
                ha="center", va="bottom", fontsize=8, rotation=30
            )
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(
            lambda val, _: f"{val:.1e}" if val > 0 else "0"
        ))
        ax.set_ylim(0, calculated_masses.max() * 1.3)
    else:
        # Log scale: clean 10^n tick labels
        ax.yaxis.set_major_formatter(ticker.LogFormatterMathtext())
        ax.set_ylim(1e22, 3e27)

# Add a shared legend / annotation
fig.text(
    0.5, -0.04,
    f"G = {G:.3e} N·m²/kg²   |   Data sources: NASA Planetary Fact Sheets",
    ha="center", fontsize=9, color="gray"
)

plt.tight_layout()
output_path = "planet_masses_plot.png"
plt.savefig(output_path, dpi=150, bbox_inches="tight")
print(f"Plot saved to: {output_path}")
plt.show()
