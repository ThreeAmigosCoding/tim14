from setuptools import setup, find_packages

setup(
    name="parser_xml",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    entry_points = {
        'parsers_xml':
            ['parse_code=parse.code.parse_code_xml:XmlParser'],
    },
    zip_safe=True
)