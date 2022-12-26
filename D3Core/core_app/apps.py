import pkg_resources
from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    name = 'core_app'
    parser_plugins = []
    visualization_plugins = []

    def ready(self):
        # Prilikom startovanja aplikacije, ucitavamo plugine na
        # vec poznati nacin.
        self.parser_plugins = []
        self.visualization_plugins = []


def load_plugins(mark):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=mark):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
