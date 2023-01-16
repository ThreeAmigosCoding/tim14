from core_app.models import TestModel
from core_app.services.load import LoadService


class JsonParser(LoadService):

    def name(self):
        return "Json parser"

    def identifier(self):
        return "parse_json"

    def load(self):
        TestModel.objects.all().delete()

        test1 = TestModel(name="Test num 1", greeting="Hello from Json")
        test1.save()

        test2 = TestModel(name="Test num 2", greeting="Hello from Json")
        test2.save()

