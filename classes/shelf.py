class Shelf(object):
    def __init__(self, height, width, depth, name=None):
        self.name = name
        self.height = height
        self.width = width
        self.depth = depth

        self.new_height = height
        self.new_width = width
        self.new_depth = depth

        self.products = {}

    def __str__(self):
        num_of_products = sum(self.products.values())
        string1 = "Shelf height, width, depth: {}, {}, {}\n"
        string2 = "Shelf name: {}\nNumber of products on shelf: {}\n"
        string3 = "Products: {}"
        string4 = string1 + string2 + string3
        return string4.format(self.height, self.width, self.depth,
                              self.name, num_of_products, self.products)

    def enough_space(self, product, sub=False):
        if 0 <= product.height <= self.new_height:
            if 0 <= product.width <= self.new_width:
                if 0 <= product.depth <= self.new_depth:
                    return True
        if sub:
            self.subtract_space(product)
        return False

    def subtract_space(self, product):
        self.new_height -= product.height
        self.new_width -= product.width
        self.new_depth -= product.depth

    def add_space(self, product):
        self.new_height += product.height
        self.new_width += product.width
        self.new_depth += product.depth

    def place(self, product, number=1):
        for i in range(number):
            if self.enough_space(product):
                product_name = product.name
                if product_name in self.products.keys():
                    self.products[product_name] += 1
                elif product_name not in self.products.keys():
                    self.products[product_name] = 1
                self.subtract_space(product)

                if self.products[product_name] == number:
                    return True, self.products, number
        return False, self.products, number
