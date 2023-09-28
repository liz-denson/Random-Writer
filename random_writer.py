######################################
# Random Writer programming assignment
# Liz Denson & Connor Loudermilk
# 2023-09-11
######################################

# import libraries
from random import randint, choice

###########
# FUNCTIONS
###########

# returns a random seed of length level (or k) from the book
def get_seed(book, k):
    # pick a random index that represents the beginning of the seed in the book
    index = randint(0, len(book) - k)
    # return the random seed of length level (or k)
    return book[index:index + k]
    
# returns a random next character given a seed from the book
def get_nxt_char(book, seed, k):
    # initialize the list of characters
    chars = []
    # initialize the current index (where we begin to look in the book)
    index = 0
    # continually find the seed in the book
    while (index < len(book) - k):
        # find the index of the seed in the book beginning at the current index
        index = book.find(seed, index)
        # abort if the seed is not found (or it's at the end of the book)
        if (index == -1 or index + k >= len(book)):
            break
        # otherwise, add the next character to the list
        chars.append(book[index + k])
        # and update the index in the book
        index += 1
    # if there is at least one next character in the list of characters, return a randomly chosen one
    if (len(chars) > 0):
        return choice(chars)
    # otherwise, return some appropriate trigger (e.g., None)
    else:
        return None

######
# MAIN
######

# grab command line arguments (or manually set the parameters)
# k (or level) -> the level of analysis performed on the book
# length -> the length of output to generate
# filename -> the filename that contains the text of the book
k = 1
length = 150
filename = "hg-wells_the-time-machine.txt"
    
# grab the book
with open(filename, "r") as f: ## line 58-59 based on posted assignment
    book = f.read()
        
# initialize the output
output = []
    
# pick a random seed of length level (or k)
seed = get_seed(book, k)
    
# repeat as long as there isn't enough output yet
while (len(output) < length): ## line 68-70 class example
    # get a random next character
    nxt_char = get_nxt_char(book, seed, k)
        
    # if one exists
    if (nxt_char != None):
        # add it to the output
        output += nxt_char
        # and recalculate the seed
        seed = seed[1:] + nxt_char
    # otherwise
    else:
        # pick another random seed
        seed = get_seed(book, k)
            
# display the output
print(''.join(output))
