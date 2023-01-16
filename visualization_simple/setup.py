from setuptools import setup, find_packages

setup(
    name="visualization_simple",
    version="0.1",
    packages=find_packages(),
    install_requires=['core_app>=0.1'],
    entry_points={
        'visualization_simple':
            ['visualize=visualize.code.visualize_code:SimpleVisualization'],
    },
    zip_safe=True
)