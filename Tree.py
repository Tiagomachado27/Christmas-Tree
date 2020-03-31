line_num = 0
num_ast = 1
space_num = 0

line_num = space_num = int(input("Escolhe um número: "))

print(" ")


while space_num != 0:
    print(" "*int(space_num) + "*"*num_ast)
    space_num-= 1
    num_ast += 2
    line_num += 1
print ("Feliz Natal!")

input()
