import pkg_resources
from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    name = 'core_app'
    json_parser_plugin = []
    xml_parser_plugin = []
    simple_visualization_plugin = []
    complex_visualization_plugin = []

    def ready(self):
        # Prilikom startovanja aplikacije, ucitavamo plugine na
        # vec poznati nacin.
        self.json_parser_plugin = load_plugins("parsers_json")
        self.xml_parser_plugin = load_plugins("parsers_xml")
        self.simple_visualization_plugin = load_plugins("visualization_simple")
        self.complex_visualization_plugin = load_plugins("visualization_complex")


def load_plugins(mark):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=mark):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
