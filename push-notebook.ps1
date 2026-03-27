# PowerShell script to automate pushing Jupyter Notebooks to GitHub.

# Prompt user for the notebook filename.
$notebookFile = Read-Host -Prompt 'Enter the name of the notebook file (without extension)'
$notebookPath = "$HOME\Downloads\$notebookFile.ipynb"

# Check if the file exists.
if (Test-Path $notebookPath) {
    # Change to the local git repository directory.
    Set-Location -Path "$HOME\path_to_your_repo"
    
    # Copy the notebook to the repository directory.
    Copy-Item -Path $notebookPath -Destination "$HOME\path_to_your_repo"
    
    # Stage the changes.
    git add "$notebookFile.ipynb"
    
    # Commit the changes with a timestamp.
    git commit -m "Auto-commit: Updated $notebookFile.ipynb on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    
    # Push the changes to GitHub.
    git push origin main
} else {
    Write-Host "File $notebookPath does not exist." 
}