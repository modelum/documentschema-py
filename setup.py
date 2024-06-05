from setuptools import setup, find_packages

setup(
    name='documentschema-py',
    version='0.3',
    packages=find_packages(),
    package_data={'documentschema-py': ['documentschema.ecore', 'documentschema/*']},
    include_package_data=True,
    install_requires=[
        "pyecore>=0.15.0"
    ]
)
