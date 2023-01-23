# asdict変換 #
import dataclasses

@dataclass(frozen=True)
class User:
    name: str
    age: int

user = User('kato', 20)
result = dataclasses.asdict(user)
print(result)