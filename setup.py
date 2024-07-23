import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__= "0.0.0.0"

REPO_NAME = "https://github.com/amithansani/Text-Summarizer"
AUTHOR_USER_NAME = "amithansani"
SRC_REPO = "textsummerizer"
AUTHOR_EMAIL="amit.hansani@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_NAME,
    project_urls={
        "Bug Tracker": f"{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    

)


