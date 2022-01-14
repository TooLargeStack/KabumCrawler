from dataclasses import dataclass


@dataclass
class Home:
    
    name = 'home'

    categories: str
    link: str
    name: str


@dataclass
class Category:

    name = 'category'

    pages: str
    products: str
    products_links: str


@dataclass
class Product:

    name = 'product'

    unavailable: str
    values_block: str
    original: str
    main: str
    deferred: str
    title: str


@dataclass
class SiteMap:

    name = 'sitemap'

    home: Home
    category: Category
    product: Product
    # ...


# TODO: make this dynamic
all_dataclasses = [
    Home,
    Category,
    Product,
    SiteMap
]

# End Of File