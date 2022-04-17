#!/usr/bin/python3

def tablas():
    # pedimos datos al usuario
    base = int(input("[*] Dame el numero de la tabla: "))
    limite = int(input("[*] Dame el numero hasta cuanto se le multiplica: "))


    for i in range(1, limite + 1):
        resultado = base * i

        print(f"{base} X {i} = {resultado}")


if __name__=="__main__":
    tablas()
