from classes.aisle import Aisle
from classes.section import Section
from classes.shelf import Shelf


class Setter(object):

    def __init__(self):
        self.products_filename = "products.json"
        self.class_info_filename = "class_info.json"

    @staticmethod
    def aisle(aisle_data):
        names = aisle_data["names"]
        sections = aisle_data["sections"]
        aisle = Aisle(names=names, num_sections=sections)
        return aisle

    @staticmethod
    def section(aisle_data):
        names = aisle_data["names"]
        shelves = aisle_data["shelves"]
        section = Section(names=names, num_shelves=shelves)
        return section

    @staticmethod
    def shelve(shelf_data):
        height = shelf_data["height"]
        width = shelf_data["width"]
        depth = shelf_data["depth"]
        shelf = Shelf(height=height, width=width, depth=depth)
        return shelf
