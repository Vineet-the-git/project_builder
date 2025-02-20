import os

def display_tree(directory, exclude_dirs=None):
    """
    Display directory structure in tree format.
    
    Args:
        directory (str): Path to the directory
        exclude_dirs (list): List of directory names to exclude (default: ['venv'])
    """
    # Set default exclude directories if none provided
    if exclude_dirs is None:
        exclude_dirs = ['venv']
    
    # Get the base name of the directory
    base_name = os.path.basename(os.path.abspath(directory))
    print(f"{base_name}/")
    print("│")
    
    def _display_tree(directory, prefix=""):
        # Get and sort directory contents
        entries = sorted(os.scandir(directory), key=lambda e: e.name)
        # Filter out excluded directories
        entries = [e for e in entries if e.name not in exclude_dirs]
        entries = list(entries)
        
        # Process each entry
        for i, entry in enumerate(entries):
            # Check if this is the last entry
            is_last = i == len(entries) - 1
            # Select the connector symbol
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{entry.name}")
            
            # If it's a directory, recurse with updated prefix
            if entry.is_dir():
                # Extend prefix: use space for last item, │ for others
                extension = "    " if is_last else "│   "
                _display_tree(entry.path, prefix + extension)
    
    _display_tree(directory)

# Example usage
if __name__ == "__main__":
    # You can exclude additional directories by adding them to the list
    display_tree(".", exclude_dirs=['venv', '.git', '__pycache__'])