from logging_helpers import _L
from microdrop.plugin_manager import (PluginGlobals, Plugin, IPlugin,
                                      implements)
import trollius as asyncio

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

PluginGlobals.push_env('microdrop.managed')


class {{cookiecutter.plugin_name.split('_')|map('title')|join('')}}(Plugin):
    implements(IPlugin)

    plugin_name = '{{cookiecutter.plugin_name}}'
    version = __version__

    @property
    def name(self):
        return self.plugin_name

    @name.setter
    def name(self, value):
        pass

    @asyncio.coroutine
    def on_step_run(self, plugin_kwargs, signals):
        _L().debug('doing some work when a step is run')
        raise asyncio.Return()


PluginGlobals.pop_env()
