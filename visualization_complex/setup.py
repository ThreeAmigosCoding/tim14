from setuptools import setup, find_packages

setup(
    name="visualization_complex",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    entry_points = {
        'visualization_complex':
            ['visualize_code=visualize.code.visualize_code:ComplexVisualization'],
    },
    zip_safe=True
)