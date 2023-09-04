import random
import string

# Function to generate a random word of a specified length
def generate_random_word(length):
    # Define the set of characters to use for generating words
    characters = string.ascii_lowercase  # You can customize this if needed

    # Generate the random word
    word = ''.join(random.choice(characters) for _ in range(length))
    
    return word

# Number of words to generate
num_words = 5  # Change this to the desired number of words

# Length of each word
word_length = 6  # Change this to the desired length of words

# Generate and print random words
random_words = [generate_random_word(word_length) for _ in range(num_words)]
for word in random_words:
    print(word)
