import os
import json
import codecs

content_folder = 'content/'

def fix_notebook_metadata(filename):
    try:
        with codecs.open(filename, 'r', encoding='utf-8-sig') as file:
            notebook = json.load(file)

        for cell in notebook.get('cells', []):
            if cell['cell_type'] == 'code':
                cell['execution_count'] = None
                cell['outputs'] = []

        with codecs.open(filename, 'w', encoding='utf-8') as file:
            json.dump(notebook, file, indent=2)
        
        print(f"Fixed: {filename}")
    except Exception as e:
        print(f"Error with {filename}: {e}")

print("Starting notebook metadata fix...")
for filename in os.listdir(content_folder):
    if filename.endswith('.ipynb'):
        fix_notebook_metadata(os.path.join(content_folder, filename))

print("All notebooks processed!")
