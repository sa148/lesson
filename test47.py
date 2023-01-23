# ==でフィールド値の検証false版 #
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('kato', 20)
user2 = User('kato', 20)
print(user1 == user2)

# ==でフィールド値の検証true版 #
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

user1 = User('kato', 20)
user2 = User('kato', 20)
print(user1 == user2)