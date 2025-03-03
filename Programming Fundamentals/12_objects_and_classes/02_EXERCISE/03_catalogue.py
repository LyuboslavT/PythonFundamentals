class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, name: str):

        self.products.append(name)

    def get_by_letter(self, first_letter: str):
         return [name for name in self.products if name.startswith(first_letter)]

    def __repr__(self):

        sorted_products = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted_products)



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
