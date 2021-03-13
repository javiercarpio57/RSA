import random

letters = 'abcdefghijklmnopqrstuvwxyz ,.'

def inverso_modulo(num, modulo):
    while True:
        for i in range(modulo):
            if (num * i) % modulo == 1:
                print("El inverso de " + str(num) + " es: " + str(i))
                return i

def mcd(a, b):
    aux = 0

    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a

def check_prime(a, b):
    try:
        a = int(a)
        b = int(b)
        a_divisor = get_divisors(a)
        b_divisor = get_divisors(b)

        if len(a_divisor) == 2 and len(b_divisor) == 2 and a != b:
            return True

        return False
    except:
        return False

def get_divisors(a):
    for i in range(a):
        x = [i for i in range(1, a + 1) if not a % i]
    return x

def get_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    mcd_value = 0
    while mcd_value != 1:
        e = random.randint(0, phi)
        mcd_value = mcd(phi, e)

    d = inverso_modulo(e, phi)
    
    return (e, n), (d, n)

def cipher(frase, e, n):
    cifrado = []
    for f in frase:
        M_i = letters.index(f)

        cifrado.append((M_i ** e) % n)
        
    return cifrado

def descipher(frase, d, n):
    descifrado = []
    for f in frase:
        c = (f ** d) % n
        descifrado.append(letters[c])
        
    return descifrado



opcion = 0
menu = '''
    1. Creación de llaves (pública, privada).
    2. Cifrado de mensaje dado una llave pública y el mensaje a cifrar.
    3. Descifrado de mensaje dado un ciphertext y una llave privada.
    4. Salir

'''

while opcion != '4':
    opcion = input(menu)

    if opcion == '1':
        correcto = False

        while not correcto:
            p = input('Ingrese un numero primo: ')
            q = input('Ingrese un segundo numero primo: ')

            correcto = check_prime(p, q)

            if not correcto:
                print(' -- Numeros ingresados no son validos -- \n')

        p = int(p)
        q = int(q)
        publica, privada = get_keys(p, q)

        print('-------------------------------')
        print('LLAVE PUBLICA', publica)
        print('LLAVE PRIVADA', privada)
        print('-------------------------------')

    elif opcion == '2':
        mensaje = input('Ingrese el mensaje a encriptar: ')
        llave_publica_e = int(input('Ingrese llave publica e: '))
        llave_publica_n = int(input('Ingrese llave publica n: '))

        cifrado = cipher(mensaje, llave_publica_e, llave_publica_n)

        print('-------------------------------')
        print('CIFRADO:', ' '.join([str(c) for c in cifrado]))
        print('-------------------------------')

    elif opcion == '3':
        mensaje = input('Ingrese el mensaje a desencriptar (ej. 20 25 32 1): ')
        d = int(input('Ingrese llave privada d: '))
        n = int(input('Ingrese llave privada n: '))

        descifrado = descipher([int(m) for m in mensaje.split(' ')], d, n)

        print('-------------------------------')
        print('DESCIFRADO:', ''.join([str(c) for c in descifrado]))
        print('-------------------------------')






