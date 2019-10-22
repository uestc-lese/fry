ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list.Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee",
              "Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop(0) #pop()默认从最后 pop(0)默认从第一开始
    print('adding: ',next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print('there we go: ',stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print('  '.join(stuff))
print('#'.join(stuff[3:5]))
