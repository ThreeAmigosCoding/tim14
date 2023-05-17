from setuptools import setup, find_packages

setup(
    name="visualization_complex",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    package_data={'visualization_complex': ['templates/*.html']},
    entry_points={
        'visualization_metadata':
            ['path=complex'],
        'visualization':
            ['visualize_code_complex=visualization_complex.apps.ComplexVisualizationConfig'],
        'urls':
            ['path=visualization_complex.urls']
    },
    zip_safe=True
)
