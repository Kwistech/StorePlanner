class Product(object):

    def __init__(self, name=None, amount=None, width=None, height=None,
                 depth=None, aisle=None, section=None, shelf=None):
        self.name = name
        self.amount = amount
        self.width = width
        self.height = height
        self.depth = depth
        self.aisle = aisle
        self.section = section
        self.shelf = shelf

    def __str__(self):
        string = "{} {} {} {}"
        return string.format(self.name, self.width,
                             self.height, self.depth)

    @staticmethod
    def groups(product_data):
        grocery = product_data["Grocery"]
        dairy = product_data["Dairy"]

        product_groups = grocery, dairy
        return product_groups

    @staticmethod
    def create_products(product_groups):
        products = []
        for group in product_groups:
            for item in group:
                amount = group[item]["amount"]
                height = group[item]["height"]
                width = group[item]["width"]
                depth = group[item]["depth"]
                aisle = group[item]["aisle"]
                section = group[item]["section"]
                shelf = group[item]["shelf"]
                product = Product(name=item, amount=amount,
                                  width=width, height=height,
                                  depth=depth, aisle=aisle,
                                  section=section, shelf=shelf)
                products.append(product)
        return products
