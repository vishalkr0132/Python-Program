'''WAP using functions accept a dictionary with  N numner of key or values and display the 
output as following

inputs : a = 1,b = 2,c = 1,d = 3,e = 2, f = 4, g = 3

output : {
    1: [a,c],
    2:[b,e]
    3:[d,g]
    4:[f]
}
'''

def fun(**param):
    d1 = {}
    for key, value in param.items():
        if value not in d1:
            d1[value] = []  # Initialize the list if value is not already a key
        d1[value].append(key)  # Append the key to the list
    print(d1)

# Call the function with the correct syntax
fun(a=1, b=2, c=1, d=3, e=2, f=4, g=3)

