from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="json-schema-for-humans",
    version="0.2",
    license="Apache License 2.0",
    author="Denis Blanchette, AbdulRahman Al Hamali",
    author_email="tools@coveo.com",
    description="Generate static HTML documentation from JSON schemas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coveooss/json-schema-for-humans",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Documentation",
    ],
    python_requires=">=3.6",
    install_requires=["click", "htmlmin", "jinja2", "markdown2"],
    entry_points={"console_scripts": ["generate-schema-doc = json_schema_for_humans.generate:main"]},
)
