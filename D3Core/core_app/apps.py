import pkg_resources
from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    name = 'core_app'
    json_parser_plugin = []
    xml_parser_plugin = []
    visualization_plugins = []

    def ready(self):
        self.json_parser_plugin = load_plugins("parsers_json")
        self.xml_parser_plugin = load_plugins("parsers_xml")
        self.visualization_plugins = load_visualization_plugins("visualization_metadata")


def load_plugins(mark):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=mark):
        # with open("log.txt", "a") as f:
        #     f.write(str(ep.load) + "\n")
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins


def load_visualization_plugins(path):
    result = []
    for ep in pkg_resources.iter_entry_points(group=path):
        result.append(str(ep).split("=")[1].strip())
        with open("log.txt", "w") as f:
            f.write(str(ep) + "\n")
    return result
