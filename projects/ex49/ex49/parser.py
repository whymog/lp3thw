class ParserError(Exception):
    pass
    
def loop(self, word_list):
    # Loops through the list of scanned words
    pass

def match(word_list, expecting):
    # Matches words to our Subject Verb Object setup
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else: 
            return None
    else:
        return None

def peek(word_list):
    # Looks ahead to a potential tuple to make decisions accordingly
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def skip(word_list, word_type):
    # Skips things we don't care about, like stop words
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


class Sentence(object):
     # Composes our results into a new Sentence object
     
     def __init__(self, subject, verb, obj):
         # remember we take ('noun','princess') tuples and convert them
         self.subject = subject[1]
         self.verb = verb[1]
         self.object = obj[1]
