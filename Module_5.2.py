class House:
    def __init__(self, name,numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def go_to(self,new_floor):
        if self.numbers_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
            return None
        for i in range(new_floor+1):
            print(i)
    def __len__(self):
        return self.numbers_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей {self.numbers_of_floors}'





House_1 = House('Rafinad',21)
House_2 = House('GoPro',33)

#House_1.go_to(13)
#House_2.go_to(34)

# __str__
print(str(House_1))
print(str(House_2))

# __len__
print(len(House_1))
print(len(House_2))