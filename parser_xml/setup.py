from setuptools import setup, find_packages

setup(
    name="parser_xml",
    version="0.1",
    packages=find_packages(),
    install_requires=['core-app>=0.1'],
    entry_points={
        'parser_metadata':
            ['extension=xml', 'name=xml'],
        'parse':
            ['parse=parser_xml.apps.XmlParserConfig'],
        'urls':
            ['path=parser_xml.urls']
    },
    zip_safe=True
)