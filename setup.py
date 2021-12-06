import setuptools

dependencies = ["wheel", "recordclass", "numpy"]
tests_dependencies = ["pytest", "pytest_cov"]
extras = {"test": tests_dependencies}

setuptools.setup(
    name="aoc2021",
    version="0.0.1",
    description="Advent of Code 2021 Solutions",
    author="Vance Morris",
    author_email="vmorris@us.ibm.com",
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    tests_require=tests_dependencies,
    extras_require=extras,
)
