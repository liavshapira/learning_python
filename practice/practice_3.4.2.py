string_to_change=(input("Please enter a string:"))
letter_to_change=string_to_change[0]
trimmed_string=string_to_change[1:]
new_string=trimmed_string.replace(letter_to_change,"e")
print(letter_to_change+new_string)