import os
from pathlib import Path
import logging

# Set up logging to print messages with timestamps for tracking the script’s actions
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the main project folder name
project_name = "TextSummarizer"

# List of directories and files to create for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",                 # GitHub workflows folder with a placeholder file
    f"src/{project_name}/__init__.py",            # Init file for the main project package
    f"src/{project_name}/components/__init__.py", # Init file for the components module
    f"src/{project_name}/utils/__init__.py",      # Init file for the utils module
    f"src/{project_name}/utils/common.py",        # Common utilities file
    f"src/{project_name}/logging/__init__.py",    # Init file for logging module
    f"src/{project_name}/config/__init__.py",     # Init file for config module
    f"src/{project_name}/config/configuration.py",# Configuration settings file
    f"src/{project_name}/entity/__init__.py",     # Init file for entity module
    f"src/{project_name}/constants/__init__.py",  # Init file for constants module
    "config/config.yaml",                         # General config file in a separate config folder
    "params.yaml",                                # Parameters file for the project
    "app.py",                                     # Main application file
    "main.py",                                    # Entry point for the project
    "Dockerfile",                                 # Docker configuration for containerization
    "requirements.txt",                           # Requirements file listing dependencies
    "setup.py",                                   # Setup file for packaging the project
    "research/trials.ipynb"                       # Jupyter notebook for experimentation and research
]

# Loop through each path in the list to create the necessary folders and files
for filepath in list_of_files:
    filepath = Path(filepath)                # Convert the string path to a Path object
    filedir, filename = os.path.split(filepath) # Separate the directory path and filename

    # Create the directory if it doesn't already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory and any necessary parent directories
        logging.info(f"Creating directory: {filedir} for the file {filename}") # Log directory creation

    # Create the file if it doesn't exist or if it’s empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:       # Open the file in write mode to create an empty file
            pass                             # Do nothing; just create the empty file
        logging.info(f"Creating empty file: {filepath}")  # Log file creation
    else:
        logging.info(f"{filename} already exists")        # Log if the file already exists
