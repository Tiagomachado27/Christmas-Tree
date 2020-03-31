num_ast = 1
space_num = 0

space_num = int(input("Escolhe um número: "))

print(" ")


while space_num != 0:
    print(" "*int(space_num) + "*"*num_ast)
    space_num-= 1
    num_ast += 2

print ("Feliz Natal!")

input()
