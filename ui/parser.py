from argparse import ArgumentParser
from data.getter import Getter
from ui.display import Display


class CommandLineParser(object):

    def __init__(self, store):
        self.display = Display(store)
        self.parser = ArgumentParser()
        self.getter = Getter()

        self.commands = self.getter.get_datum("commands.json")
        self.args = self.set_args()

    def set_args(self):
        choices = list(self.commands.keys())
        self.parser.add_argument("--option", help="option", choices=choices)
        self.parser.add_argument("--full", help="full percentage")
        args = self.parser.parse_args()
        return args

    def switch(self):
        if self.args.option == "tree":
            self.display.tree()
        elif self.args.option == "full":
            if self.args.full:
                full_p = int(self.args.full)
                self.display.full_shelves(full_percentage=full_p)
            else:
                self.display.full_shelves()
        elif self.args.option == "empty":
            self.display.empty_shelves()
        elif self.args.option == "quit":
            quit()
