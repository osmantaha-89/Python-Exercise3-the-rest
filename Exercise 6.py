str = "a"
print(6* str)

string = "at" 
char_list = list(string) 
char_list[0], char_list[1] = char_list[1], char_list[0] 
new_string = "".join(char_list)
print(new_string)  

string="Dog"
x=list(string)
tex=x[0]
x[0]=x[-2]
x[1]=tex
print("".join(x))

string="wait"
x=list(string)
tex=x[0]
x[0]=x[-1]
x[-1]=tex
print("".join(x))

word = "Btrtatitn"
letter_to_remove = "t"
result = word.replace(letter_to_remove, "")
print(result)

