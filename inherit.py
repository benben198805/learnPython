class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    def __len__(self):
        return 100

dog = Dog()
dog.run()

cat = Cat()
cat.run()
print(len(cat))