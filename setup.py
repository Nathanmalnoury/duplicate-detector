import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="duplicate-detector-malnoury",  # Replace with your own username
    version="0.0.1",
    author="Nathan Malnoury",
    author_email="n.malnoury@gmail.com",
    description="A small duplicate handler CLI tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nathanmalnoury/duplicate-detector",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "tqdm",
        "Pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Console",

    ],
    python_requires='>=3.8',
)
