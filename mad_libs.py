###########################################################
######### use the open func to read the txt file ###########
###########################################################
with open("story.txt", "r") as f: # "r" stands for read mode. and the "f" is a var which means we can do any file operations inside the block
    story = f.read() # all it does print out or read all the text inside of this file
# print(story)

words = set() # we store values in set to eliminate duplicates i.e make the items unique 
start_of_word = -1 # to check if we have found the starting index of a word

######## var for brackets 
target_start = "<" 
target_end = ">"

# Loop through the story with enumerate function which access all the individual char as an index. what enumerate does is give us access to that position as well as the element at that position
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i # if we find the start of a word and its equal to our target start! we reassign that to to loop variable "i"


    if char == target_end and start_of_word != -1: # condition for if we the current char is equal to the target end and making sure the start of a word is found by checking if its not equal to -1
        word = story[start_of_word: i + 1] # slicing from the story 
        words.add(word) #add our word to our set
        start_of_word = -1 # resetting the start of word again

# print(words)


answers = {} # set a dictionary, in other word set up an object: key value pairs

for word in words: # loop through words
    answer = input("Enter a word for " + word + ": ") # ask user to input the word for each key(from the dictionary) that was found
    answers[word] = answer # creating a key value pair with the key(from the dictionary) and assigning a value to it from the user input

# print(answers)

for word in words: # loop through the words 
    story = story.replace(word, answers[word]) # now we replace every single word we found within the angle bracket with our answers


print(story)

