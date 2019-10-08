print("let's practice everything.")
print('you\'d need to know\'about escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem="""
\tThe lovely word
with logic so firmly planted
can not discern \n the need of love
nor comprehend passions from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")


five=10 - 2 + 3 - 6
print(f"this should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 1000
    return jelly_beans, jars, crates


start_point = 100000
beans, jars, crates = secret_formula(start_point)
# remember that this is another way to formate a string
print("with a starting point of: {}".format(start_point))
#it's like with an f"" starting
print(f"we'd j=have {beans} beans,{jars} jars, and {crates} crates.")

start_point = start_point / 10
print("we can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a formate starting
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
