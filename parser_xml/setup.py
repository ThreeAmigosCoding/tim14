from setuptools import setup, find_packages

setup(
    name="parser_xml",
    version="0.1",
    packages=find_packages(),
    install_requires=['core_app>=0.1'],
    entry_points = {
        'parsers':
            ['parse=parse.code.parse_code'],
    },
    zip_safe=True
)