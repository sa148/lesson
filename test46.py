# dataclass #
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User('sato', 20)
print(user.name)
print(user.age)

# items追加 #
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    items: list[int] = field(default_factory=lambda: ['note', 'pen'])

user = User('sato', 20)
print(user.items)

# frozen #
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

user = User('kato', 20)
user.age = 21