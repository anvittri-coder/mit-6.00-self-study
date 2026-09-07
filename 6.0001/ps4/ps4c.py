# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import re
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        trans_dict = {}
        # lowercase letters
        for i in range(len(CONSONANTS_LOWER)):
            trans_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]

        # uppercase letters
        for i in range(len(CONSONANTS_UPPER)):
            trans_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]

        # vowels
        for i in range(len(VOWELS_LOWER)):
            trans_dict[VOWELS_LOWER[i]] = vowels_permutation[i].lower()
            trans_dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()

        return trans_dict


        

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypt_msg = ""
        for char in self.message_text:
            if char in transpose_dict:
                encrypt_msg += transpose_dict[char]
            else:
                encrypt_msg += char    
        return encrypt_msg
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
     # initialize what needs to be tracked

    # for every vowel permutation:
        # build transpose dictionary
        # decrypt message
        # split into words
        # count valid words
        # update best if necessary
    # return best message
    # WHICH VOWEL PERMUTATION GETS THE MOST WORDS???
    # EACH PERMUTATION DECRYPTS THE MESSAGE
    # UNDERSTAND EACH FUNC NEEDED

        best = ""
        no_words = 0
        max_corr = 0
        word_list = self.get_valid_words()

        for perm in get_permutations(VOWELS_LOWER):
            encrypt_dict = self.build_transpose_dict(perm)
            encrypt_message = self.apply_transpose(encrypt_dict)
            for word in re.split(r'[^a-zA-Z]', encrypt_message):
                if is_word(word_list, word):
                    no_words += 1
            if no_words > max_corr:
                max_corr = no_words
                best = encrypt_message
            no_words = 0
        if best == "":
            return self.message_text
        else:
            return best


        

if __name__ == '__main__':

    # Example test case
    
     
    

    print("--------------------------------------")
    # Test case 1
    # with uppercase vowel permutation
    message = SubMessage('hElLO WORld!')
    permutation = "UEIAO"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message: {0}, Permutation: {1}".format(
        message.get_message_text(), permutation))
    print("Expected encryption: hElLA WARld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(
        message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print("--------------------------------------")
    # Test case 2
    # with 3 individual valid words
    
    #  Test case 3
    #  with 2 valid words connected as one 'unstressed-waterproof'
    message = SubMessage('unstressed-waterproof watersheds')
    permutation = "uoeia"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message: {0}, Permutation: {1}".format(
        message.get_message_text(), permutation))
    print("Expected encryption: anstrossod wutorpriif wutorshods")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(
        message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
