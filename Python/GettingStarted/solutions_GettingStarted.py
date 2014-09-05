# Problem 1
'''
1. Imaginary numbers are written with a suffix of j or J.
	Complex numbers can be created with the complex(real, imag) function.
	To extract just the real part use .real
	To extract just the imaginary part use .imag
2. float(x) where x is the integer.
3. //
'''

# Problem 2
'''
Integer Division returns the floor.
'''

# problem 3
'''
1. A string is immutable because its content cannot be changed. 
2. my_string[::3] returns every two letters of the string. Io eeAErr!
   my_string[::-1] returns the string in reverse.
3. The entire string in reverse can be accessed by my_string[::-1]
'''

# problem 4
'''
1. Mutable objects can be changed in place after creation. 
   The value stored in memory is changed.
   Immutable objects cannot be modified after creation. 
2.  my_list[4] = "yoga"
	my_list[:] is a copy of the entire list
	my_list[:] = [] clears the list (del a[:] is also an option)
	len(my_list) returns the list size. 
	my_list[0], my_list[1] = "Peter Pan", "camelbak"
	my_list.append("Jonathan, my pet fish")
3. 
my_list = []
my_list = [i for i in range(5)]
my_list[3] = float(my_list[3])
del my_list[2]
my_list.sort(reverse=True)
'''

# Problem 5
'''
1. set() (must be used to create an empty set) and {}
2. 
union = set.union(setA, setB)
or union = setA | setB
3. Trick question! sets don't support indexing, slicing, or any other 
sequence-like behavior. Works because sets are unordered and don't allow duplicates.
'''

# problem 6
'''	
1. dict() and {} (must be used to create an empty dictionary), {key:value}
2. sq = {x: x**2 for x in range(2,11,2)}
3. del(dict[key])
4. dict.values(), dict.items()
'''

# problem 7
'''
Adds n into a list (the same list)
def track(n, a=None):
    if a = None:
        a = []
    a.append(n)
    return a
'''

#problem 8
'''
1. 	The print statement writes the value of the expression(s) it's given 
	to the standard output. The return statement allows a function to specify 
	a return value to be passed back to the calling function. 
2. Grocery List cannot have a space. It is also important NOT to call your list "list". 
Doing so shadows Python's built in list constructor. 
	for loop and if statement require a colon and nested indentation
	i%2 == 0. Not an assignment. 
	Grocery List[i]. Needs brackets.
'''
