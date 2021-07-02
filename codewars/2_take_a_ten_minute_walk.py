"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

"""

valid_action = ['n', 's', 'w', 'e']
action_value = {
    'n': [1, 1],
    's': [1, -1],
    'w': [0, -1],
    'e': [0, 1]
}

def is_valid_walk(walk):
    position = [0, 0]
    
    if(len(walk) is not 10):
        return False

    if(not all(x in valid_action for x in walk)):
        return False

    for x in walk:
        value = action_value[x]
        position[value[0]] += value[1]

    if(position[0] is not 0 or position[1] is not 0):
        return False

    return True


"""
Tests
"""
test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
test.expect(not is_valid_walk(['w']), 'should return False');
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');