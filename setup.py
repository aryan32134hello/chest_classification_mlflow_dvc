import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chest_classification_mlflow_dvc"
AUTHOR_USER_NAME = "aryan32134hello"
SRC_REPO = "CNNChestClassifier"
AUTHOR_EMAIL = "12115118@nitkkr.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com.{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug_Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)