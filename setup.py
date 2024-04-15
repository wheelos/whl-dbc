import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adbctool",
    version="0.1.0",
    author="daohu527",
    author_email="daohu527@gmail.com",
    description="apollo dbc tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daohu527/adbctool",
    project_urls={
        "Bug Tracker": "https://github.com/daohu527/adbctool/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    package_data={"": [
        'template/*.tpl',
    ]},
    install_requires=[
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'adbctool = adbctool.gen:main',
        ],
    },
    python_requires=">=3.6",
)
