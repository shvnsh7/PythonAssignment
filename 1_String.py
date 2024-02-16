# Given a String of Characters
# 1. Print the three most common characters along with their occurrence count.
# 2. Sort in descending order of occurrence count.
# 3. If the occurrence count is the same for any character, sort the characters in alphabetical order.

def print_common_characters(string):
    character_counts = {}
    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    common_characters = sorted(character_counts.items(), key=lambda x: (-x[1], x[0])) 
                                #returns a list of touples containing key value pair from character_counts dictionary
                                                        #here key function is lambda function
                                                                        #-x[1] the first element of lambda fn sorts 
                                                                                    #descending order hence -ve sign
                                                                                #If two tuples have same x[0] will sort in alphabetical order
    common_characters = common_characters[:3] #using slicing we take 3 most common tuples

    for character, count in common_characters:
        print(f"Character: {character}, Count: {count}")

# Test the program
input_string = "abracadabra"
print_common_characters(input_string)