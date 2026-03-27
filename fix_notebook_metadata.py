import os
import json

# Path to the content folder containing .ipynb files
content_folder = 'content/'

# Function to fix execution_count and outputs metadata

def fix_notebook_metadata(filename):
    with open(filename, 'r') as file:
        notebook = json.load(file)

    # Iterate over each cell in the notebook
    for cell in notebook.get('cells', []):
        if cell['cell_type'] == 'code':
            # Fix execution_count and outputs
            cell['execution_count'] = None
            cell['outputs'] = []

    # Write the updated notebook back to file
    with open(filename, 'w') as file:
        json.dump(notebook, file, indent=2)

# Iterate over all .ipynb files in the content folder
for filename in os.listdir(content_folder):
    if filename.endswith('.ipynb'):
        fix_notebook_metadata(os.path.join(content_folder, filename))
