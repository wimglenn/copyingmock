from setuptools import setup


classifiers = [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries',
    'Intended Audience :: Developers',
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name='copyingmock',
    version='0.2',
    description='A subclass of MagicMock that copies the arguments',
    long_description=long_description,
    py_modules=['copyingmock'],
    author='Wim Glenn',
    author_email='hey@wimglenn.com',
    license='MIT',
    url='https://github.com/wimglenn/copyingmock',
    classifiers=classifiers,
    install_requires=["mock ; python_version<'3.3'"],
)
