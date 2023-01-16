from setuptools import setup, find_packages

setup(
    name="parser_json",
    version="0.1",
    packages=find_packages(),
    install_requires=['core_app>=0.1'],
    entry_points = {
        'parsers_json':
            ['parse=parse.code.parse_code:JsonParser'],
    },
    zip_safe=True
)