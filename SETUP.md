# Workshop Setup 🚀

Completing this setup before the workshop ensures we can dive straight into coding without install delays.

## Prerequisites

Start by making sure you have the following software installed:

- **Git:** https://git-scm.com/downloads  
- **`uv` (package manager):** https://docs.astral.sh/uv/getting-started/installation/  
  Used to manage project dependencies and ensure consistent Python versions. After installing `uv`, restart the terminal.
- **Code editor:** Any editor is fine. I personally use VS Code: https://code.visualstudio.com/download  

## Step 1: Clone the course repo

Run: 
```sh 
git clone https://github.com/arilamstein/streamlit-workshop.git
cd streamlit-workshop
```

## Step 2: Create the course virtual environment

Run:
```sh
uv sync
```

This creates `.venv` and installs all dependencies pinned for the workshop.

## Step 3: Activate the virtual environment

Use the command for your OS/shell:

- Mac/Linux:  `source .venv/bin/activate`
- Windows (Command Prompt):  `.venv\Scripts\activate`
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Windows (Git Bash / MINGW64): `source .venv/Scripts/activate`

Verify:
- Run `python --version` → should report a version starting with **Python 3.13**
- Run `which python` (Mac/Linux) or `where python` (Windows) → should show a path inside `.venv`

## Step 4: Open the first notebook

In your terminal, run:
```sh
jupyter notebook 1-intro.ipynb
```

This should open a browser tab showing the first notebook in the course. The first cell loads the dataset we'll use throughout the workshop - click "Run" (or press Shift+Enter) to execute it. You should see a preview of the data appear below the cell.

That's the whole exercise - once it runs without errors, you're all set for the workshop 🎉

If you hit any issues, reach out in the course chat.

