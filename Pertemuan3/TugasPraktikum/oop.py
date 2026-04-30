# Class Didefinisikan sebagai berikut
class MyClass:
    x = 5

# Membuat Objek dari class tersebut
p1 = MyClass()
print(p1.x)

# Multiple Object
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#__init method__
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Suki", 30)

print(p1.name)
print(p1.age)

# Tanpa __init__
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# Self Parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

# create class method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()


# Method Modifying Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

# multiple method
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()    