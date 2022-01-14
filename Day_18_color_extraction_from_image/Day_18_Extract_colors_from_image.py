import colorgram
colors = colorgram.extract("hello.jpg", 6)
for i in colors:
    print(i.rgb)
    print(i.hsl)
    print(i.proportion)
    print("\n")