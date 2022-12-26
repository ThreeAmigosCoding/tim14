from setuptools import setup, find_packages

setup(
    name="visualization_complex",
    version="0.1",
    packages=find_packages(),
    install_requires=['core_app>=0.1'],
    entry_points = {
        'visualization':
            ['visualize=visualize.code.visualize_code'],
    },
    zip_safe=True
)