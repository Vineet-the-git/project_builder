from setuptools import setup, find_packages

setup(
    name="project_builder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'cookiecutter',
        'click',
        'pyyaml',
        'groq'
    ],
    entry_points={
        'console_scripts': [
            'mlgen=project_builder.main:main',
        ],
    },
    author="Vineet Kumar",
    description="A tool to generate ML project structure with basic code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)