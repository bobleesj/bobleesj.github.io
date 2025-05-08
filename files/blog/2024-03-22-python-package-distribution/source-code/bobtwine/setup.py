from setuptools import find_packages, setup

setup(
    name="bobtwine",
    version="0.4",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        # Your dependencies here
    ],
)
