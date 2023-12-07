def multiple_returns(sentence):
    
    if len(sentence) == 0:
        return (0, None)  
    else:
        return (len(sentence), sentence[0]) 


sentence = "Holberton"
length, first_char = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first_char))

