import os.path


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        if not os.path.exists(self.__file_name):
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self) -> str:
        file = open(self.__file_name, 'r')
        products_in_file = file.read()
        file.close()
        return products_in_file

    def add(self, *products: Product):
        for i in products:
            if i.name in self.get_products():
                print(f'Продукт {i.name} уже есть в магазине')
                continue
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{str(i)}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')


print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
