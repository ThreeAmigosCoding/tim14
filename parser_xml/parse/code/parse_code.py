from core_app.models import TestModel
from core_app.services.load import LoadService


class XmlParser(LoadService):

    def name(self):
        return "XML parser"

    def identifier(self):
        return "parse_xml"

    def load(self):
        TestModel.objects.all().delete()

        test1 = TestModel(name="Test num 1", greeting="Hello from Xml")
        test1.save()

        test2 = TestModel(name="Test num 2", greeting="Hello from Xml")
        test2.save()



