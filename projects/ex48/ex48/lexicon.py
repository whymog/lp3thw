lexicon = [('direction', 'north'),
           ('direction', 'south'),
           ('direction', 'east'),
           ('direction', 'west'),

           ('verb', 'go'),
           ('verb', 'stop'),
           ('verb', 'kill'),
           ('verb', 'eat'),

           ('stop', 'the'),
           ('stop', 'in'),
           ('stop', 'of'),
           ('stop', 'from'),
           ('stop', 'at'),
           ('stop', 'it'),

           ('noun', 'door'),
           ('noun', 'bear'),
           ('noun', 'princess'),
           ('noun', 'cabinet')]
            

def scan(stuff):
    # Split the user's query up into an array
    words = stuff.split(" ")

    # Creates an empty array of results to return
    result = []
    
    # Takes a query word and scans the lexicon for a match
    for word in words:
        found = False

        for term in lexicon:
            if word.lower() == term[1].lower():
                result.append(term)
                found = True

        if not found:
            # Test to see if it's a number
            if convert_number(word) is not None:
                result.append(('number', convert_number(word)))
            else:
                # If it's not a number append as an error
                result.append(('error', word))

    print(result)

    # Return the result
    return result

# NOTE: nosetests is old af and doesn't seem to like importing files like 
# this, so I've just copied it over into here for ease of use. 

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
