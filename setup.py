import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setuptools.setup(
    name="discord-py-interactions",
    version="1.2.0",
    author="hpenney2",
    author_email="hpenney1010@gmail.com",
    description="A fork of discord-py-slash-command for all interaction types.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hpenney2/discord-py-interactions",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
