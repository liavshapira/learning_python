string_to_check=(input("Please enter a string:"))
string_to_check=string_to_check.lower()
string_to_check=string_to_check.replace(" ","")
reverse_string=string_to_check[::-1]
print(reverse_string)
print(string_to_check)
if (string_to_check == reverse_string):
    print("OK")
else:
    print("NOT")
