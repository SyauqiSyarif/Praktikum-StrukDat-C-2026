class Film:
    def __init__(self, judul, genre, tahun):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun

    def introduce_self(self):
        print(f'Judul Film ini {self.judul} Genrenya {self.genre} Tahun {self.tahun}')

    def change_genre(self, new_genre):
        self.genre = new_genre
        print(f'New Genre nya adalah {self.genre}')


f1 = Film("Suki", "Horror", 2000)
f2 = Film("Shawn", "Drama", 2001)
f3 = Film("Love", "Romance", 2002)

f1.introduce_self()
f2.introduce_self()
f3.introduce_self()

f2.change_genre("horror")