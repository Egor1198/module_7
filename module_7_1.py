from pprint import pprint


class Product():
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return str_product


class Shop():
    __file_name = 'products_1.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        for i in products:
            p = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if p in f:
                print(f'Продукт {p} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{p}')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
