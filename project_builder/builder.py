import os

from project_builder import utils
from project_builder.templates import ProjectTemplate

class ProjectGenerator:
    def __init__(self):
        self.project_name = None
        self.project_desc = None
        self.data_desc = None
        self.basic_code = False
        self.model_type = None

        # got user inputs
        self.get_user_inputs()

        self.project_template = ProjectTemplate(self.basic_code, self.model_type)

    # Function to trigger project creation
    def generate_project(self):
        """Generate a project structure and basic code."""
        # created a basic file structure
        self.create_project_structure(project_name=self.project_name)

        # get the project structure
        self.project_structure = self.project_template.visualize_structure()

    # Function to get user inputs
    def get_user_inputs(self):
        """Force user to enter details for project creation."""
        while not self.project_name:
            self.project_name = input("Enter project name: ")

        basic_code = input("Would you like some basic code (y/n): ")
        self.basic_code = True if 'y' in basic_code.lower() else False

        if self.basic_code:
            while not self.model_type:
                model_type = input("Enter the type of model you would like to use \n 1. Neural Networks \n 2. Classical ML. \n (Choose: 1 or 2): ")
                if '1' in str(model_type):
                    self.model_type = 'neural'
                elif '2' in str(model_type):
                    self.model_type = 'classical'
                else:
                    print("Invalid input. Please try again.")

    # Function to create a project structure
    def create_project_structure(self, project_name, neural=False):
        # Create project directory
        os.makedirs(project_name, exist_ok=True)
        os.chdir(project_name)

        # Create directories
        for directory in self.project_template.directories:
            os.makedirs(directory, exist_ok=True)

        for file_path, content in self.project_template.files.items():
            print("Creating file: ", file_path)
            with open(file_path, 'w') as file:
                file.write(content)

        # Create a .gitignore file
        gitignore_content = utils.get_gitignore_content()
        with open('.gitignore', 'w') as gitignore_file:
            gitignore_file.write(gitignore_content)

        print(f"Project '{project_name}' created successfully.")

