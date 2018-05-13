import setuptools

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries",
]

setup_requires = [
    "setuptools-scm",
]
install_requires = []
extras_require = {}

with open("README.rst") as fd:
    long_description = fd.read()


def main():
    setuptools.setup(
        name="mink",
        description="mink: make sense of schemaless data dictionaries",
        long_description=long_description,
        license="MIT license",
        platforms=["unix", "linux", "osx", "cygwin", "win32"],
        author="Paulius Maruška",
        author_email="paulius.maruska@gmail.com",
        classifiers=classifiers,
        keywords="dict schema",
        url="https://github.com/Paulius-Maruska/mink",
        project_urls={
            "Source":  "https://github.com/Paulius-Maruska/mink",
            "Tracker": "https://github.com/Paulius-Maruska/mink/issues",
        },
        use_scm_version=True,
        packages=setuptools.find_packages("src"),
        package_dir={
            "": "src"
        },
        setup_requires=setup_requires,
        install_requires=install_requires,
        extras_require=extras_require,
        python_requires=">=3.5.*",
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
