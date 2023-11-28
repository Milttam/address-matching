import random
import string
from faker import Faker
fake = Faker()



def scramble_street_name(original_address):
    """
    Given parameter "original_address" representing a standardized American 
    street address (all uppercase), takes street name field and scrambles some 
    of the letters. Separates the original address into a list and scrambles 
    the address field. Returns full modified address with scrambled letters. 

    """
    components = original_address.split(",") #Splitting address by commas
    components = components[0].split(" ",1) + components[1:] #Splitting house number
    
    street_name = components[1]
    iteration = iterations(street_name) #Getting number of iterations
    
    #generating random indices to scramble and putting them into list form
    random_index = random_indexes(street_name, iteration)
  
    #scrambling letters based on generated random indices
    for i in random_index:
        letter = random.choice(string.ascii_letters).upper()
        street_name = street_name[: i] + letter + street_name[i + 1 :]
        
    return street_name

def random_indexes(field, iteration):
    """
    Given two parameters "field" and "iteration", generates a list of integers
    that represents the indices of characters to scramble in "field". Iteration
    indicates size of the list returned based on the length of String "field".
    """
    random_index = []
    for i in range(iteration):
        random_index.append((int)(len(field) * random.random()))
        
    return random_index
    
def iterations(field):
    """
    Given one parameter "field", returns an integer to represent the number of 
    characters in String "field" that should be scrambled. If length of "field"
    is <= 5, returns 1. If length is between 5 and 15, returns 2. If greater
    than 15, returns 3
    """
    size = len(field)
    if size <= 5: 
        iteration = 1
    elif size <=15: 
        iteration = 2
    else:
        iteration = 3
   
    return iteration
    
    
    

#TESTING
original_address = "8 CORNELL COURT, Princeton Junction, NJ, 08550"
print(scramble_street_name(original_address))
    
#randomizer for deleting letters
#randomizer for 