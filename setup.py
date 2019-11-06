from setuptools import setup, find_packages

setup(
    name = "packaging_treasure",
    version = "0.1.0",
    author = "L. Castro, K. Goldmann, T. Oruc, O. Sargoni"
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse', 'copy', 'random'],
    entry_points={
        'console_scripts': [
            'hunt = packaging_treasure.command:process'
        ]})
