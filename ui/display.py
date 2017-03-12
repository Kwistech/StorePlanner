class Display(object):

    def __init__(self, store):
        self.store = store
        self.indent = "    "

    def tree(self):
        self.aisles()

    def aisles(self):
        for aisle in self.store.aisles:
            print("Aisle: {}".format(aisle.name))
            self.sections(aisle)

    def sections(self, aisle):
        for section in aisle.sections:
            print("{}Section: {}".format(self.indent, section.name))
            self.shelves(section)

    def shelves(self, section, stage=2):
        for shelf in section.shelves:
            print("{}Shelf: {}".format(self.indent * stage, shelf.name))
            self.products(shelf)

    def products(self, shelf, stage=3):
        for product in shelf.products:
            for i in range(shelf.products[product]):
                print("{}Product: {}".format(self.indent * stage, product))

    def full_shelves(self, full_percentage=10):
        print("\nFull Shelves: \n")

        full_shelves = []
        for shelf in self.store.shelves:
            total_space = shelf.height * shelf.width * shelf.depth
            actual_space = shelf.new_height * shelf.new_width * shelf.depth
            full_at = total_space * (full_percentage / 100)

            if actual_space <= full_at:
                full_shelves.append(shelf)
                print("Shelf: {}".format(shelf.name))
                self.products(shelf, stage=1)

        return full_shelves

    def empty_shelves(self):
        print("\nEmpty Shelves: \n")

        empty_shelves = []
        for shelf in self.store.shelves:
            init_space = shelf.height * shelf.new_width * shelf.new_depth
            new_space = shelf.new_height * shelf.new_width * shelf.new_depth

            if new_space == init_space:
                empty_shelves.append(shelf)
                print("Shelf: {}".format(shelf.name))

        return empty_shelves
