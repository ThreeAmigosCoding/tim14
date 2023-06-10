import pkg_resources
from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    name = 'core_app'
    parser_plugins = []
    visualization_plugins = []

    def ready(self):
        self.parser_plugins = load_parser_plugins("parser_metadata")
        self.visualization_plugins = load_visualization_plugins("visualization_metadata")


def load_visualization_plugins(path):
    result = []
    for ep in pkg_resources.iter_entry_points(group=path):
        result.append(str(ep).split("=")[1].strip())
        # with open("log.txt", "w") as f:
        #     f.write(str(ep) + "\n")
    return result


def load_parser_plugins(path):
    result = {}
    names = []
    extensions = []
    for ep in pkg_resources.iter_entry_points(group=path):
        if str(ep).split("=")[0].strip() == "name":
            names.append(str(ep).split("=")[1].strip())
        elif str(ep).split("=")[0].strip() == "extension":
            extensions.append(str(ep).split("=")[1].strip())

    for i in range(len(names)):
        result[extensions[i]] = names[i]
    return result
