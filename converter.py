
#Voy a intentar hacer una herramienta para convertir divisas

dinero = int(input("\nIndica la cantidad que quieres convertir: \n"))
moneda = input("\nIndica el tipo de moneda actual: (euros, dolares, libras, yenes, francos, yuanes)\n")
out = input("\n¿A qué quieres convertirlo? (euros, dolares, libras, yenes, francos, yuanes)\n")
print("\nVamos a convertir", dinero, moneda, "\n")

if moneda == "euros" and out == "dolares":
    print(dinero, moneda, "equivalen a ", dinero * 1.1036, "dólares\n")
elif moneda == "euros" and out == "libras":
    print(dinero, moneda, "equivalen a ", dinero * 0.8667, "libras\n")
elif moneda == "euros" and out == "yenes":
    print(dinero, moneda, "equivalen a ", dinero * 155.6300, "yenes\n")
elif moneda == "euros" and out == "francos":
    print(dinero, moneda, "equivalen a ", dinero * 0.9287, "francos\n")
elif moneda == "euros" and out == "yuanes":
    print(dinero, moneda, "equivalen a ", dinero * 7.8331, "yuanes\n")
elif moneda == "euros" and out == "euros":
    print("¿De verdad quieres convertir", moneda, "a ", moneda, "\n")

if moneda == "dolares" and out == "euros":
    print(dinero, moneda, "equivalen a ", dinero * 0.9058, "euros\n")
elif moneda == "dolares" and out == "libras":
    print(dinero, moneda, "equivalen a ", dinero * 0.7854, "libras\n")
elif moneda == "dolares" and out == "yenes":
    print(dinero, moneda, "equivalen a ", dinero * 141.0200, "yenes\n")
elif moneda == "dolares" and out == "francos":
    print(dinero, moneda, "equivalen a ", dinero * 0.8415, "francos\n")
elif moneda == "dolares" and out == "yuanes":
    print(dinero, moneda, "equivalen a ", dinero * 7.0978, "yuanes\n")

if moneda == "libras" and out == "euros":
    print(dinero, moneda, "equivalen a ", dinero * 1.1532, "euros\n")
elif moneda == "libras" and out == "dolares":
    print(dinero, moneda, "equivalen a ", dinero * 1.2729, "dólares\n")
elif moneda == "libras" and out == "yenes":
    print(dinero, moneda, "equivalen a ", dinero * 179.5600, "yenes\n")
elif moneda == "libras" and out == "francos":
    print(dinero, moneda, "equivalen a ", dinero * 1.0711, "francos\n")
elif moneda == "libras" and out == "yuanes":
    print(dinero, moneda, "equivalen a ", dinero * 9.0481, "yuanes\n")

if moneda == "yenes" and out == "euros":
    print(dinero, moneda, "equivalen a ", dinero * 0.0064, "euros\n")
elif moneda == "yenes" and out == "dolares":
    print(dinero, moneda, "equivalen a ", dinero * 0.7090, "dólares\n")
elif moneda == "yenes" and out == "libras":
    print(dinero, moneda, "equivalen a ", dinero * 0.5567, "libras\n")
elif moneda == "yenes" and out == "francos":
    print(dinero, moneda, "equivalen a ", dinero * 0.5965, "francos\n")
elif moneda == "yenes" and out == "yuanes":
    print(dinero, moneda, "equivalen a ", dinero * 0.0503, "yuanes\n")

if moneda == "francos" and out == "euros":
    print(dinero, moneda, "equivalen a ", dinero * 1.0761, "euros\n")
elif moneda == "francos" and out == "dolares":
    print(dinero, moneda, "equivalen a ", dinero * 1.1878, "dólares\n")
elif moneda == "francos" and out == "libras":
    print(dinero, moneda, "equivalen a ", dinero * 0.9328, "libras\n")
elif moneda == "francos" and out == "yenes":
    print(dinero, moneda, "equivalen a ", dinero * 167.5500, "yenes\n")
elif moneda == "francos" and out == "yuanes":
    print(dinero, moneda, "equivalen a ", dinero * 8.4307, "yuanes\n")

if moneda == "yuanes" and out == "euros":
    print(dinero, moneda, "equivalen a ", dinero * 0.1275, "euros\n")
elif moneda == "yuanes" and out == "dolares":
    print(dinero, moneda, "equivalen a ", dinero * 0.1408, "dólares\n")
elif moneda == "yuanes" and out == "libras":
    print(dinero, moneda, "equivalen a ", dinero * 0.1106, "libras\n")
elif moneda == "yuanes" and out == "yenes":
    print(dinero, moneda, "equivalen a ", dinero * 19.8567, "yenes\n")
elif moneda == "yuanes" and out == "francos":
    print(dinero, moneda, "equivalen a ", dinero * 0.1185, "francos\n")