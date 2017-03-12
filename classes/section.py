class Section(object):

    def __init__(self, num_shelves, names=None):
        self.num_shelves = num_shelves
        self.names = names

        self.shelves = []
        self.name = None

    def __str__(self):
        string = "Section name(s): {}, number of shelves per section: {}"
        return string.format(self.names, self.shelves)
