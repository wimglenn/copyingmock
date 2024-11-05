from setuptools import setup


setup(
    name="copyingmock",
    version="0.2",
    description="A subclass of MagicMock that copies the arguments",
    long_description=open("README.md").read(),
    py_modules=["copyingmock"],
    author="Wim Glenn",
    author_email="hey@wimglenn.com",
    license="MIT",
    url="https://github.com/wimglenn/copyingmock",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
    ],
    install_requires=["mock ; python_version<'3.3'"],
    options={"bdist_wheel": {"universal": True}},
)
