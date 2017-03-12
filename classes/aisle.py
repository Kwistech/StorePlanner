class Aisle(object):

    def __init__(self, num_sections, names=None):
        self.num_sections = num_sections
        self.names = names

        self.name = None
        self.sections = []

    def __str__(self):
        string = "Aisle name(s): {}, number of sections per aisle: {}"
        return string.format(self.names, self.num_sections)
