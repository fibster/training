from setuptools import setup, find_packages

setup(
    name='traininng',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project's dependencies here.
        # Example: 'requests>=2.20.0',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here.
            # Example: 'your_command=your_module:main_function',
        ],
    },
)