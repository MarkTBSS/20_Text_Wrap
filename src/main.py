import textwrap
string = "This is a very very very very very long string."
print(textwrap.wrap(string,8))
print("===================================")
string = "This is a very very very very very long string."
print(textwrap.fill(string,8))
print("===================================")
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
print(textwrap.fill(string,4))