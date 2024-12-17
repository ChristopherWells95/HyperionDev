#This code demonstrates the manipulation of characters. 

#This line declares the variable a sentence/string; which will the be manipulated through various functions.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#This code replaces the character "!" with a blank space to seperate the words.
new_sentence = sentence.replace("!", " ")
print(new_sentence)

#This code changes the characters of the sentence to all uppercase.
upper_sentence = new_sentence.upper()
print(upper_sentence)

#This code changes the position of the characters, so that the sentence is in reverse.
position = upper_sentence[ : : -1]
print(position)
