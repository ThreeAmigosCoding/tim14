from core_app.models import TestModel
from core_app.services.load import LoadService
from visualization_simple.visualize import views


class SimpleVisualization(LoadService):

    def name(self):
        return "Simple visualization"

    def identifier(self):
        return "visualization_simple"

    def load(self):
        views.simple_visualization()

        # TestModel.objects.all().delete()
        #
        # test1 = TestModel(name="Test num 1", greeting="Hello from Simple")
        # test1.save()
        #
        # test2 = TestModel(name="Test num 2", greeting="Hello from Simple")
        # test2.save()



