from setuptools import setup, find_packages

setup(
    name="Superlib",
    version="0.0.1",
    author="Don Erhan",
    author_email="docker.andrei@gmail.com",
    url="",
    description="Description of lib",
    packages=find_packages(),
    py_modules=['src'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["tqdm"],
    entry_points={"console_scripts": ["Superlib = src.main:main"]},
)