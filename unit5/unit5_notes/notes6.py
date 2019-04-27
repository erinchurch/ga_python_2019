# LIST COMPREHENSIONS FOR DATA SCIENCE

#maninpulating lists continues

#usually heavy in data science

#USE FOR DATA SCIENCE AND LINEAR DATA
#NOT APPROPRAITE FOR DOING SOFTWARE DEVELOPMENT

#normally in ipython so it follows line g = ...

#normally done working in IDE,w hich would be the for loops for g1

number = [1,2,3,4]

g = [3 * x for x in number]

print("g", g)


g1 = []
for i in number:
    i *= 3
    g1.append(i)

print("g1", g1)

print(number)

h = [3 * x for x in number if x < 2]

print("h", h)

h1 = []

for i in number:
    if i < 2:
        i *= 3
        h1.append(i)

print("h1", h1)

i = [n + 1 for n in number if n >= 1]
print("i", i)


#the important part is the list [x, x **2]
j = [[x, x ** 2] for x in number]
print("j", j)