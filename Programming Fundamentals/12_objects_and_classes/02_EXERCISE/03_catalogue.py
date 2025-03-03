from numpy.ma.core import append, product


class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, name: str):

        self.products.append(product)

    def get_by_letter(self, first_letter: str):
        