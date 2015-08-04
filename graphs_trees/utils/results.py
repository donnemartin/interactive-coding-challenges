class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def clear_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)