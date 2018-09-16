class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

if __name__ == '__main__':
    my_first_dog = Dog("Annie")
    my_second_dog = Dog("Wyatt")

    print(my_first_dog.name)
    print(my_second_dog.name)

    my_first_dog.bark()
    my_second_dog.bark()
