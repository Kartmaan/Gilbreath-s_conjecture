def primeGen(n): #<int>
    """Return the n first prime numbers in a list"""

    primeList = []
    num = 2 

    while len(primeList) < n:
        for x in range(2, num): 
            if (num % x) == 0:
                break
        else:
            primeList.append(num)

        num += 1

    return primeList #<list>

def ratio(x): # <list>
    """Generates the absolute ratio of each pair of numbers 
    contained in a list.
    The function take a list of numbers as parameter and return 
    a list"""

    i = 1
    loop = 0
    L = []

    while loop < len(x) - 1 :
        res = x[i] - x[i - 1]
        res = abs(res)
        L.append(res)
        i += 1
        loop += 1

    return L #<list>

def gilbreath(n):
    """Generate a series of gilbreath lists.
    The first list is made up of n prime numbers
    """

    n = int(n)
    gil_list = []
    gil_list.append(primeGen(n)) # First prime numbers

    while True:
        L = ratio(gil_list[len(gil_list)-1])
        gil_list.append(L)
        if len(L) == 1:
            break

    return gil_list

if __name__ == "__main__":
    gil = gilbreath(5)
    for x in gil:
        print(x)