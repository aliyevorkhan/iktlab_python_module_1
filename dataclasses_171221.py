from dataclasses import *

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts)
print(queen_of_hearts.rank)
print(queen_of_hearts.suit)

print(queen_of_hearts == DataClassCard('Q', 'Hearts'))

queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}