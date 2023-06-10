from setuptools import setup, find_packages

setup(
    name="parser_json",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    entry_points = {
        'parser_metadata':
            ['extension=json', 'name=json'],
        'parse':
            ['parse=parser_json.apps.JsonParserConfig'],
        'urls':
            ['path=parser_json.urls']
    },
    zip_safe=True
)