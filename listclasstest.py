#classtest

test_list = []

class Fish:
     def __init__(self, name):
         self.name = name

         test_list.append(self)

class Fruit:
     def __init__(self, name):
         self.name = name

         test_list.append(self)


trout = Fish("trout")
salmon = Fish("salmon")
herring = Fish("herring")

apple = Fruit("apple")
orange = Fruit("orange")
banana = Fruit("banana")

for Fruit in test_list:
    print(Fruit.name)
