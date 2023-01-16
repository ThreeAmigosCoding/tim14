from core_app.models import TestModel
from core_app.services.load import LoadService


class ComplexVisualization(LoadService):

    def name(self):
        return "Complex visualization"

    def identifier(self):
        return "visualization_complex"

    def load(self):
        TestModel.objects.all().delete()

        test1 = TestModel(name="Test num 1", greeting="Hello from Complex")
        test1.save()

        test2 = TestModel(name="Test num 2", greeting="Hello from Complex")
        test2.save()



