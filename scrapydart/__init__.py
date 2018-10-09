import pkgutil

__version__ = pkgutil.get_data(__package__, 'VERSION').decode('ascii').strip()
version_info = tuple(__version__.split('.')[:3])

from scrapy.utils.misc import load_object
from scrapydart.config import Config


def get_application(config=None):
    if config is None:
        config = Config()
    apppath = config.get('application', 'scrapydart.app.application')
    appfunc = load_object(apppath)
    return appfunc(config)
