from dataclasses import dataclass
from os.path import abspath

import toml

from crawler.sitemap.dataclasses import SiteMap, Category, all_dataclasses

# TODO: import "data type" classes

__sitemap_data: dict = toml.load(abspath('crawler/sitemap/sitemap.toml'))


def sitemap_constructor(sitemap_data: dict) -> SiteMap:
    """
    Get a site map object.

    :param sitemap_data: loaded value from the sitemap.toml file.

    :return: SiteMap object.
    """
    # recursive check on classes and attributes.
    # _sitemap = SiteMap.__setattr__()

    # first or second?

    data_map = {}
    # key: dict
    # for key in sitemap_data.keys():
    for _class in all_dataclasses:
        data_for_class = sitemap_data.get(_class.name)
        if data_for_class:
            data_map.update({
                _class.name: _class(**data_for_class)
            })
            # break

    return SiteMap(**data_map)


        # if type(key) is dict:
        #     sitemap_constructor(key)


sitemap: SiteMap = sitemap_constructor(sitemap_data=__sitemap_data)

# End Of File