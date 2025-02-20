from . import boiler_plates

class ProjectTemplate:
    def __init__(self, boiler_plate=False, model_type='classical'):
        self.directories = [
            'config',
            'data',
            'data/raw',
            'data/processed',
            'logs',
            'models',
            'notebooks',
            'src',
            'src/data',
            'src/models',
            'src/vizualizations',
            'src/utils',
            'tests',
        ]
        self.files = {
            'README.md': '# Project Title',
            'requirements.txt': boiler_plates.bp_requirement_txt(),
            'config/config.yaml': boiler_plates.bp_config_yaml(),
            'config/load_config.py': boiler_plates.bp_load_config_py(),
            'logger.py': boiler_plates.bp_logger_py(),
            'exceptions.py': boiler_plates.bp_exception_py(),
            'src/__init__.py': '',
            'src/data/__init__.py' : '',
            'src/data/make_dataset.py' : boiler_plates.bp_make_dataset_py(boiler_plate, model_type),
            'src/data/build_features.py' : '# Create features',
            'src/models/__init__.py' : '',
            'src/models/model.py' : boiler_plates.bp_model_py(boiler_plate, model_type),
            'src/models/train_model.py' : boiler_plates.bp_train_model_py(boiler_plate, model_type),
            'src/models/predict_model.py' : '# Predict model',
            'tests/__init__.py' : '',
            'tests/unit_tests.py' : '# Unit tests',
            'tests/integration_tests.py' : '# Integration tests',
            'src/utils/__init__.py' : '',
            'src/utils/common.py' : '# Common functions',
        }   

    def visualize_structure(self, project_name="project_name"):
        """
        Visualizes the project structure in a tree-like format.

        Args:
            project_name (str): Name of the project root directory

        Returns:
            str: String representation of the project structure
        """

        # 1. Build an empty tree structure with the project name as the root
        tree = {project_name: {}}

        # 2. Helper function to insert directories into the tree
        def insert_directory(path_parts, current_node):
            """
            Recursively insert a list of path parts (directories) into the tree.
            """
            if not path_parts:
                return
            dir_part = path_parts[0]

            # If the directory doesn't exist yet, create it
            if dir_part not in current_node:
                current_node[dir_part] = {}

            # Move deeper into the tree
            insert_directory(path_parts[1:], current_node[dir_part])

        # 3. Helper function to insert a file into the correct directory node
        def insert_file(path_parts, current_node):
            """
            Recursively traverse directories to place the file in the correct node.
            """
            if len(path_parts) == 1:
                # We are at the file
                filename = path_parts[0]
                # Store file as None or some placeholder (since we don't need content for tree display)
                current_node[filename] = None
            else:
                dir_part = path_parts[0]
                if dir_part not in current_node:
                    current_node[dir_part] = {}
                insert_file(path_parts[1:], current_node[dir_part])

        # 4. Insert all directories into the tree
        for directory in self.directories:
            path_parts = directory.split("/")
            insert_directory(path_parts, tree[project_name])

        # 5. Insert all files into the tree
        for file_path in self.files:
            path_parts = file_path.split("/")
            insert_file(path_parts, tree[project_name])

        # 6. Now we have a nested dictionary (tree). Let's define a function to print it recursively.
        lines = []

        def print_tree(node, prefix="", is_last=True):
            """
            Recursively traverse the tree (dict) and build lines for output.
            
            :param node: The current node in the tree (dict)
            :param prefix: The current prefix string with pipes/spaces
            :param is_last: Whether this node is the last in the current level
            """
            # For the root, just print the name (with no '├──' or '└──')
            keys = list(node.keys())
            for index, key in enumerate(keys):
                is_key_last = (index == len(keys) - 1)
                
                # Determine the connector
                connector = "└── " if is_key_last else "├── "
                
                lines.append(f"{prefix}{connector}{key}")
                
                # If the key is a dictionary (i.e., a subdirectory), recurse
                if isinstance(node[key], dict):
                    # If we're not at the last key, we continue the vertical line
                    new_prefix = prefix + ("    " if is_key_last else "│   ")
                    print_tree(node[key], prefix=new_prefix, is_last=is_key_last)

        # 7. Trigger the printing from the top-level (project_name)
        # The top-level "project_name" should print without prefix.
        project_root = list(tree.keys())[0]
        lines.append(f"{project_root}/")
        print_tree(tree[project_root], prefix="", is_last=True)

        return "\n".join(lines)