# f = open("123456", "a")
# f.write("     GLC级\n     GLE级")
# f.close()

f = open("123456", "r")

a = f.readlines()
print(a)
for r in a:
    print(r)
