
# Esto es un proyecto de prueba en el que se crea una calculadora simple pero efectiva que opera con dos valores

print("\nVamos a operar con dos números\n")
num1 = int(input("\n¿Cúal es el primer valor? \n"))
num2 = int(input("\n¿Cuál es el segundo valor? \n"))
condi = input("\n¿Qué operación quieres realizar?(suma, resta, multiplica o divide) \n")

if condi == "suma":
    print("\nEl resultado de la suma entre ", num1 ,"y ", num2, "es: ", num1 + num2, "\n")
elif condi == "resta":
    print("\nEl resultado de la resta entre ", num1 , "y ", num2, "es", num1 - num2, "\n")
elif condi == "multiplica":
    print("\nEl resultado de la multiplicación entre", num1, "y ", num2, "es", num1 * num2, "\n")
elif condi == "divide":
    print("\nEl resultado de la división entre", num1 , "y " , num2 , "es ", num1 / num2, "\n")