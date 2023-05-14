from setuptools import setup, find_packages

setup(
    name="visualization_simple",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    package_data={'visualize': ['templates/*.html']},
    entry_points={
        'visualization_metadata':
            ['path=simple'],
        'visualization':
            ['visualize_code_simple=visualize.apps.SimpleVisualizationConfig'],
        'urls':
            ['path=visualize.urls']
    },
    zip_safe=True
)
