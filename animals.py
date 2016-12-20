card_arrays = [['a', 'a', 'b', 'c'],
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


class Card:
    def __init__(self, sides):
        self.sides = sides

    sides = ['x', 'x', 'x', 'x']

    def get_side(s):
        return sides[s]


cards = []

for array in card_arrays:
    cards.append(Card(array))

valid_cards = [Card(['a', 'a', 'a', 'a']), Card(['a', 'a', 'a', 'a'])]    


def rotate_card(card):
    return card[1:] + card[:1]

def check_fit(grid):
    for position, card in enumerate(grid):
        neighbours = get_neighbours(grid, position)
        for side, value in enumerate(card):
            if (neighbours[side] != value and neighbours[side] != None):
                print neighbours[side]
                print value
                return False
    
    return True

# Bollocks at the moment, need to integrate Cards class
def get_neighbours(grid, index):
    grid_size = len(grid)
    neighbour_indices = [(index - 4),
                        (index + 1),
                        (index + 4),
                        (index - 1)]
    
    neighbours = [-1, -1, -1 ,-1]

    for index, val in enumerate(neighbour_indices):
        if (val < 0 or val > (grid_size - 1)):
            neighbours[index] = None
        else:
            neighbours[index] = grid[val]

    return neighbours
