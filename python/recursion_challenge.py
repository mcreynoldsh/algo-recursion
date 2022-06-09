import re
from unittest import result 
def factorial(x):
	if x == 1:
		return 1
	return x * factorial(x-1)	

def palindrome(string):
	string= re.sub("[\s\W]","",string)
	string = string.lower()
	if len(string) < 2:
		return True
	if string[0] != string[-1]:
		return False
	return palindrome(string[1:-1])		

def bottle_song(orig_num,num_bottles):
	next_bottle= num_bottles-1
	body_str= f"""	{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.
	Take one down and pass it around, {next_bottle} bottles of beer on the wall."""
	end_str = f"""	2 bottles of beer on the wall, 2 bottles of beer. 
	Take one down and pass it around, 1 bottle of beer on the wall.
	1 bottle of beer on the wall, 1 bottle of beer.
	Take one down and pass it around, no more bottles of beer on the wall.
	No more bottles of beer on the wall, no more bottles of beer.
	Go to the store and buy some more, {orig_num} bottles of beer on the wall."""
	only_one_str = """1 bottle of beer on the wall, 1 bottle of beer.
	Take one down and pass it around, no more bottles of beer on the wall.
	No more bottles of beer on the wall, no more bottles of beer.
	Go to the store and buy some more, 1 bottle of beer on the wall."""
	if num_bottles == 2:
		return print(end_str)
	elif num_bottles == 1:
		return print(only_one_str)
	else:
		print(body_str)
		return bottle_song(orig_num,next_bottle)

pattern = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
return_str = ""
def to_roman(num,pattern,return_str):
	
	last_item = pattern.popitem()
	
	if(num >= last_item[1]):
		return_str += last_item[0]
		pattern.update({last_item[0]: last_item[1]})
		num -= last_item[1]
		if num == 0:
			print(return_str)
			return
		to_roman(num,pattern,return_str)
		
	else:
		to_roman(num,pattern,return_str)


to_roman(3003,pattern,return_str)