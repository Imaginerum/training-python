class User:
    name = "Arkadiusz" #zmienna klasowa/statyczna
    id = 0

    def __int__(self, name):
        self.name = name
        User.id += 1
        self.id = User.id



print(User.name)