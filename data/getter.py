import json


class Getter(object):

    def __init__(self, *args):
        pass

    def get_data(self):
        filenames = self.get_datum("filenames.json")

        data = {}
        for filename in filenames["Filenames"]:
            datum = self.get_datum(filename)
            data[filename] = datum
        return data

    @staticmethod
    def get_datum(filename, data_dir=True):
        if data_dir:
            filename = "data/" + filename

        with open(filename) as f:
            data = json.load(f)

        return data
