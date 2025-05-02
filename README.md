🗂 Aman's Filesystem Simulator
A simple in-memory filesystem simulator written in Python. This tool allows you to interact with a virtual file structure using basic commands like mkdir, ls, cd, rm, and more.

📁 Features
Simulate folder creation and deletion

Navigate through folders (like cd and cd..)

Display current path (pwd)

List all subfolders (ls)

Search for a folder recursively

Interactive CLI interface

🚀 Getting Started
Prerequisites
Python 3.x

Run the Script
bash
Copy
Edit
python filesystem.py
💻 CLI Commands
Command	Description
mkdir <name>	Create a folder
ls	List folders in the current directory
cd <name>	Navigate into a folder
cd..	Go back to the parent folder
rm <name>	Delete a folder
pwd	Show current folder path
search <name>	Search for a folder by name
exit	Exit the CLI

🧠 How It Works
The FileSystem class manages the tree of folders using FileNode objects.

Each FileNode represents a folder with its name, path, parent, and children.

The program maintains a reference to the current working folder (current_node) and updates it as users navigate.
