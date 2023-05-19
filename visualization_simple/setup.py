from setuptools import setup, find_packages

setup(
    name="visualization_simple",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    package_data={'visualization_simple': ['templates/*.html']},
    entry_points={
        'visualization_metadata':
            ['path=simple'],
        'visualization':
            ['visualize_code_simple=visualization_simple.apps.SimpleVisualizationConfig'],
        'urls':
            ['path=visualization_simple.urls']
    },
    zip_safe=True
)
