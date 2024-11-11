import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"  # Define the version here

REPO_NAME = "TextSummarizerAWShuggingface"
AUTHOR_USER_NAME = "shreeanantbharadwaj"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "bharadwaj.shr@northeastern.edu"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,  # Ensure double underscores here
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
