from setuptools import setup, find_packages

setup(
    name="parser_json",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    entry_points = {
        'parsers_json':
            ['parse_code_json=parse.code.parse_code_json:JsonParser'],
    },
    zip_safe=True
)