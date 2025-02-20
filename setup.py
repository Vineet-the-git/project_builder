# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="project_builder",
    version="0.1.0",
    author="Vineet Kumar",
    author_email="vineet.kmr1708@gmail.com",
    description="This package generates an ML project structure which is production-ready.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vineet-the-git/project_builder",
    packages=setuptools.find_packages(),  # Fix: Automatically detects `project_builder`
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "pyyaml",
    ],  # Add dependencies later
    include_package_data=True,
)
