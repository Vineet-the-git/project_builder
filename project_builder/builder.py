import os

from project_builder import utils
from project_builder.templates import ProjectTemplate
# from project_builder.llm_interface import LLMInterface

class ProjectGenerator:
    def __init__(self):
        # self.llm = LLMInterface()
        self.project_name = None
        self.project_desc = None
        self.data_desc = None
        self.basic_code = False
        self.model_type = None
        self.project_template = ProjectTemplate()

        # variables for automated code generation
        self.code_plan = None

    # Function to trigger project creation
    def generate_project(self):
        """Generate a project structure and basic code."""
        # got user inputs
        self.get_user_inputs()

        # created a basic file structure
        self.create_project_structure(project_name=self.project_name)

        # get the project structure
        self.project_structure = self.project_template.visualize_structure()

        # if self.basic_code:
            # create a basic code for each file using LLM
            # self.code_plan = self.llm.generate_plan(self.project_desc, self.project_structure, self.data_desc, self.model_type)

            # create code for each file
        print("Project structure:")
        print(self.project_structure)

    # Function to get user inputs
    def get_user_inputs(self):
        """Force user to enter details for project creation."""
        while not self.project_name:
            self.project_name = input("Enter project name: ")

        basic_code = input("Would you like some basic code (y/n): ")
        self.basic_code = True if 'y' in basic_code.lower() else False

        if self.basic_code:
            while not self.model_type:
                self.model_type = input("Enter the type of model you would like to use (eg, Linear Regression, RNN, DNN, CNN etc): ")

            while not self.project_desc:
                self.project_desc = input("Enter a detailed project description: ")

            while not self.data_desc:
                self.data_desc = input("Enter a detailed data description: ")

    # Function to create a project structure
    def create_project_structure(self, project_name, neural=False):
        # Create project directory
        os.makedirs(project_name, exist_ok=True)
        os.chdir(project_name)

        # Create directories and files
        for directory in self.project_template.directories:
            os.makedirs(directory, exist_ok=True)

        for file_path, content in self.project_template.files.items():
            with open(file_path, 'w') as file:
                file.write(content)

        # Create a .gitignore file
        gitignore_content = utils.get_gitignore_content()
        with open('.gitignore', 'w') as gitignore_file:
            gitignore_file.write(gitignore_content)

        print(f"Project '{project_name}' created successfully.")

