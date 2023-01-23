# ==でフィールド値の検証false版 #
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('kato', 20)
user2 = User('kato', 20)
print(user1 == user2)