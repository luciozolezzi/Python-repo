from functools import lru_cache

fibonacci_cache={}

def fibonacci_sin_opt(n):
    if type(n) != int:
        raise TypeError("n tiene que ser entero positivo")
    if n<0:
        raise ValueError("n tiene que ser entero positivo")
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci_sin_opt(n-1) + fibonacci_sin_opt(n-2)


def fibonacci_con_opt_sin_lru(n):
    if type(n) != int:
        raise TypeError("n tiene que ser entero positivo")
    if n<0:
        raise ValueError("n tiene que ser entero positivo")
    #En vez de ir buscando recursiones de valores que ya se calcularon, se cachean
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n==1:
        value=1
    elif n==2:
        value=1
    elif n>2:
        value=fibonacci_con_opt_sin_lru(n-1)+fibonacci_con_opt_sin_lru(n-2)
    fibonacci_cache[n]=value    #Paso a a cache el valor resuelto
    return value



@lru_cache(maxsize=1000)   #Defino limite de la cache (def = 128)
def fibonacci_con_opt_y_lru(n):
    if type(n) != int:
        raise TypeError("n tiene que ser entero positivo")
    if n<0:
        raise ValueError("n tiene que ser entero positivo")
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci_con_opt_y_lru(n-1) + fibonacci_con_opt_y_lru(n-2)


if __name__ == "__main__":
    
    print("Fibonacci de 32 numeros con recursion sin optimizar")
    for i in range (1,33):
        print('{}: {}'.format(i,fibonacci_sin_opt(i)))
    print("Fibonacci de 32 numeros con recursion optimizado con cache manual")
    for j in range (1,33):
        print('{}: {}'.format(j,fibonacci_con_opt_sin_lru(j)))
    print("Fibonacci de 32 numeros con recursion optimizado con lru_cache")
    for k in range (1,33):
        print('{}: {}'.format(k,fibonacci_con_opt_y_lru(k)))