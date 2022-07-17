# Syntax:
' variable = lambda parameters:expression'
triple = lambda num : num*3 # Assigning the lambda to a variable

print(triple(10))

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("world", "wide", "web"))

#conditionals in lambda
my_func = lambda num: "high" if num>50 else "low"

print(my_func(67))
