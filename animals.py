cards = [['a', 'a', 'b', 'c'],
['d', 'e', 'a', 'f'],
['d', 'f', 'd', 'e'],
['d', 'e', 'f', 'g'],
['b', 'h', 'f', 'f'],
['b', 'f', 'd', 'h'],
['d', 'e', 'd', 'b'],
['a', 'g', 'd', 'e'],
['d', 'f', 'e', 'e'],
['f', 'e', 'd', 'h'],
['c', 'h', 'b', 'b'],
['f', 'e', 'd', 'f'],
['d', 'f', 'f', 'e'],
['d', 'e', 'e', 'a'],
['d', 'e', 'a', 'f'],
['d', 'h', 'e', 'a']]

grid_size = len(cards)

class Card:
    

def rotate_card(card):
    return card[1:] + card[:1]

def check_fit(grid):
    return 0

def get_neighbours(grid, index):
    # Don't want to wrap...
    top = (index - 4) % grid_size
    right = (index + 1) % grid_size
    bottom = (index + 4) % grid_size
    left = (index - 1) % grid_size

    neighbours = [cards[top][2], cards[right][3], cards[bottom][0], cards[left][1]]
    return neighbours
