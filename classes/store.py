class Store(object):

    def __init__(self, store_data):
        self.name = store_data["name"]
        self.num_aisles = store_data["aisles"]

        self.aisles = []
        self.sections = []
        self.shelves = []
        self.obj_products = []
        self.products = []

        self.sales_floor = [self.aisles,
                            self.sections,
                            self.shelves]

    def __str__(self):
        string = "\nName: {}\nAisles: {}\nSections: {}" \
                 "\nShelves: {}\nProducts: {}\n"
        return string.format(self.name, self.num_aisles,
                             len(self.sections), len(self.shelves),
                             self.products)

    def build(self, setter, class_info):
        # Get, set, and create aisles
        aisle_data = class_info["Aisles"]
        for i, aisle in enumerate(range(self.num_aisles)):
            aisle = setter.aisle(aisle_data)
            aisle.name = str(i)
            self.aisles.append(aisle)

        # Get, set and create sections
        section_data = class_info["Sections"]
        for i, aisle in enumerate(self.aisles):
            for j, section in enumerate(range(aisle_data["sections"])):
                section = setter.section(section_data)
                section.name = str(j)
                aisle.sections.append(section)
                self.sections.append(section)

        # Get, set, and create shelves
        shelf_data = class_info["Shelves"]
        for i, section in enumerate(self.sections):
            for j, shelf in enumerate(range(section_data["shelves"])):
                shelf = setter.shelve(shelf_data)
                shelf.name = str(j)
                section.shelves.append(shelf)
                self.shelves.append(shelf)

        return self.sales_floor

    def fill(self, products):
        for product in products:
            name = product.name
            amount = product.amount
            shelf = product.shelf

            self.shelves[shelf].place(product, number=amount)
            shelf_amount = self.shelves[shelf].products[name]
            self.obj_products.append(product)
            self.products.append({name: shelf_amount})
