"""Generate Markov text from text files."""

from random import choice
import sys



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)

    return file.read()


def make_chains(text_string, n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for index, word in enumerate(words):
        n_gram_list = []
        # print(word, index)
        for idx in range(index, index + n_gram):
            n_gram_list.append(words[idx])


        # print('n_gram_list is', n_gram_list)
        chains_key = tuple(n_gram_list)
        # print('chains key is', chains_key, 'type is', type(chains_key))

        if index == len(words) - (n_gram + 1):
            chains[chains_key] = [words[-1]]
            last_tuple = tuple(words[-n_gram:])
            chains[last_tuple] = None
            break
        
        # print(chains.get(chains_key, []))
        chains[chains_key] = chains.get(chains_key,[]) + [(words[index + n_gram])]
    
    return chains


def make_text(chains, n_gram):
    """Return text from chains."""

    words = []

    start_key = choice(list(chains.keys()))

    words.extend(start_key)

    index = 0

    while True:
        try:
            # chains_key = tuple([word for word in words[-n_gram:]])
            next_word = choice(chains[tuple(words[-n_gram:])])
            words.append(next_word)
            index += 1

        except TypeError:
            break    

    # print(words)

    return " ".join(words)


input_path = "green-eggs.txt"
# input_path2 = sys.argv[1]
input_path3 = 'gettysburg.txt'
# print(input_path2)

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path3)
# print(input_text)

# Get a Markov chain
chains = make_chains(input_text, 7)
# print(chains)

# Produce random text
random_text = make_text(chains, 7)

print(random_text)
