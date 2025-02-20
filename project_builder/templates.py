from project_builder import boiler_plates

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
        # Initialize the result with the project name
        result = [f"{project_name}/", "│"]
        
        # Get all unique directories from both self.directories and file paths
        all_dirs = set(self.directories)
        for file_path in self.files.keys():
            dir_path = "/".join(file_path.split("/")[:-1])
            if dir_path:
                all_dirs.add(dir_path)
        
        # Sort directories for consistent output
        sorted_dirs = sorted(list(all_dirs))
        
        # Track processed paths to handle directory prefixes
        processed_paths = set()
        
        # Process directories first
        for directory in sorted_dirs:
            depth = directory.count("/")
            parts = directory.split("/")
            
            # Handle directory prefix visualization
            for i in range(depth + 1):
                current_path = "/".join(parts[:i+1])
                if current_path not in processed_paths:
                    prefix = "│   " * i
                    result.append(f"{prefix}├── {parts[i]}")
                    if i < depth:
                        result.append(f"{prefix}│")
                    processed_paths.add(current_path)
        
        # Process files
        sorted_files = sorted(self.files.keys())
        for file_path in sorted_files:
            parts = file_path.split("/")
            depth = len(parts) - 1
            
            # Add file with appropriate prefix
            prefix = "│   " * depth
            result.append(f"{prefix}├── {parts[-1]}")
        
        # Join all lines and return
        return "\n".join(result)