clean.sh

rem install D3Core
cd D3Core
pip install .
cd ../

rem install ParserJson
cd parser_json
pip install .
cd ../

rem install ParserXML
cd parser_xml
pip install .
cd ../

rem install VisualizationComplex
cd visualization_complex
pip install .
cd ../

rem install VisualizationSimple
cd visualization_simple
pip install .
cd ../

rem runServer
cd django_project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver