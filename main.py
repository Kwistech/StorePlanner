# StorePlanner - Python 3.5 - Johnathon Kwisses (Kwistech)

# Import main object classes
from classes.store import Store
from classes.product import Product

# Import data class Setter and Getter
from data.setter import Setter
from data.getter import Getter
from ui.parser import CommandLineParser


def main():
    # Create object instances
    getter = Getter()
    setter = Setter()
    product = Product()

    # Get raw data
    data = getter.get_data()
    class_info = data["class_info.json"]
    product_info = data["products.json"]

    # Get, set, and create products
    product_groups = product.groups(product_info)
    products = product.create_products(product_groups)

    # Get, set, and create store object
    store_data = class_info["Store"]
    store = Store(store_data)

    # Set store floor layout
    store.build(setter, class_info)

    # Put products on store shelves
    store.fill(products)
    print(store)

    parser = CommandLineParser(store)
    parser.switch()

if __name__ == "__main__":
    main()
