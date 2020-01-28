import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
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

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

def decrypt_story():
    
    encrypted_story = CiphertextMessage(get_story_string())
    decrypted_story = encrypted_story.decrypt_message()
    
    return decrypted_story

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        
        dictionary = {}
        dictionary_lower = {}
        dictionary_upper = {}
        dictionary_list_lower = list(string.ascii_lowercase)
        dictionary_list_upper = list(string.ascii_uppercase)
        
        for i in range(len(string.ascii_lowercase)):
            dictionary_lower[string.ascii_lowercase[i]] = dictionary_list_lower[(i+shift)%26]
        
        for i in range(len(string.ascii_uppercase)):
            dictionary_upper[string.ascii_uppercase[i]] = dictionary_list_upper[(i+shift)%26]
        
        dictionary.update(dictionary_lower)
        dictionary.update(dictionary_upper)
        
        return dictionary
            
        


    def apply_shift(self, shift):
        
        messageText = self.get_message_text()
        shifted_message_list = []
        shift_dictionary = self.build_shift_dict(shift)
        
        
        for i in messageText:
            if i in string.ascii_letters:
                shifted_message_list.append(shift_dictionary[i])
            else:
                shifted_message_list.append(i)
        
        shifted_message = ''.join(shifted_message_list)
        
        return shifted_message
            

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        
        return self.shift

    def get_encrypting_dict(self):
        
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        
        return self.message_text_encrypted

    def change_shift(self, shift):
        
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        
        Message.__init__(self, text)
        

    def decrypt_message(self):
        
        highest_word_count = 0
        best_shift = 0
        
        for i in range(26):
            word_count = 0
            target_message = Message.apply_shift(self, i)
            final_target_message = target_message.split(' ')
            for j in final_target_message:
                if is_word(self.valid_words, j) == True:
                    word_count += 1
            if word_count > highest_word_count:
                highest_word_count = word_count
                best_shift = i
                deciphered_message = ' '.join(final_target_message)
                
        return(best_shift, deciphered_message)

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
