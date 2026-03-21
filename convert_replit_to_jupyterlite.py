import json
import os
from pathlib import Path

def py_to_ipynb(py_file, output_file, title="Python Program", description="", topic="General"):
    """
    Convert a .py file to a .ipynb notebook with markdown headers and educational enhancements
    """
    
    # Read the Python file
    with open(py_file, 'r', encoding='utf-8') as f:
        code_content = f.read()
    
    # Split code into lines for the notebook cell
    code_lines = code_content.split('\n')
    
    # Create notebook structure with educational content
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    f"**Topic:** {topic}\n",
                    "\n",
                    f"{description}\n",
                    "\n",
                    "## 📖 Instructions\n",
                    "\n",
                    "1. **Run the code** by clicking the ▶️ button or pressing Shift+Enter\n",
                    "2. **Review the output** - graphs, calculations, and visualizations\n",
                    "3. **Modify the code** - change values and re-run to experiment\n",
                    "4. **Try the challenges** at the bottom of this lesson\n",
                    "\n",
                    "---"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + '\n' for line in code_lines[:-1]] + [code_lines[-1]] if code_lines else []
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📝 Try These Modifications\n",
                    "\n",
                    "Experiment with the code above:\n",
                    "- Change input values\n",
                    "- Modify visualization parameters\n",
                    "- Add new data points\n",
                    "- Create additional plots\n",
                    "\n",
                    "---\n",
                    "\n",
                    "**Happy Learning!** 🎉"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write the notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    
    print(f"✅ Converted: {py_file} → {output_file}")

def batch_convert(conversions_map):
    """
    Batch convert multiple .py files to .ipynb
    """
    
    for py_path, config in conversions_map.items():
        output_path = config['output_path']
        
        # Create output directory if it doesn't exist
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        if os.path.exists(py_path):
            py_to_ipynb(
                py_path,
                output_path,
                title=config['title'],
                description=config['description'],
                topic=config['topic']
            )
        else:
            print(f"⚠️  File not found: {py_path}")

# ============================================
# CONFIGURATION FOR ALL 5 PROGRAMS
# ============================================

if __name__ == "__main__":
    
    conversions = {
        # Physics Programs (2)
        "projectile_motion.py": {
            'output_path': './content/numpy/physics/projectile_motion.ipynb',
            'title': 'Projectile Motion',
            'description': 'Analyze how projectiles follow different trajectories based on launch angles. Compare the range and height for 30°, 45°, and 60° launch angles using physics equations.',
            'topic': 'Physics - Kinematics'
        },
        
        "atmospheric_pressure.py": {
            'output_path': './content/numpy/physics/atmospheric_pressure.ipynb',
            'title': 'Atmospheric Pressure vs Altitude',
            'description': 'Analyze how atmospheric pressure decreases with altitude using the barometric formula. Visualize pressure changes across different atmospheric layers and compare measurement units.',
            'topic': 'Physics & Chemistry - Atmospheric Science'
        },
        
        # Chemistry Programs (2)
        "log_pH_plot.py": {
            'output_path': './content/numpy/chemistry/pH_concentration.ipynb',
            'title': 'pH and H⁺ Ion Concentration',
            'description': 'Calculate hydrogen ion (H⁺) concentration for different pH values using the formula H⁺ = 10^(-pH). Visualize the exponential relationship between pH and H⁺ concentration.',
            'topic': 'Chemistry - Acid-Base Chemistry'
        },
        
        "half_life.py": {
            'output_path': './content/numpy/chemistry/half_life.ipynb',
            'title': 'Radioactive Decay: Half-Life',
            'description': 'Analyze how radioactive isotopes decay over time using the concept of half-life. Calculate remaining amounts and visualize decay on both linear and logarithmic scales.',
            'topic': 'Chemistry & Physics - Nuclear Chemistry'
        },
        
        # Mathematics Programs (1)
        "interest_compounding.py": {
            'output_path': './content/numpy/math/compound_interest.ipynb',
            'title': 'Compound Interest Calculator',
            'description': 'Explore how investments grow over time with compound interest. Compare different interest rates and time periods using the compound interest formula.',
            'topic': 'Mathematics & Finance - Exponential Growth'
        },
    }
    
    # Convert all files
    batch_convert(conversions)
    
    print("\n" + "="*60)
    print("✅ ALL CONVERSIONS COMPLETE!")
    print("="*60)
    print("\n📂 Generated files:")
    for config in conversions.values():
        print(f"   ✓ {config['output_path']}")
    
    print("\n📊 Summary:")
    print("   • Physics: 2 programs")
    print("   • Chemistry: 2 programs")
    print("   • Mathematics: 1 program")
    print("   • Total: 5 programs ready for JupyterLite!")