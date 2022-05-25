def karatsuba_multiplication(x,y):
    if len(str(x))==1 and len(str(y)) == 1:
        return x*y
    
    n1, n2 = len(str(x)), len(str(y))
    b, d = x % (10**(n1//2)), y % (10**(n2//2))
    a, c = x // (10**(n1//2)), y // (10**(n2//2))

    ac = karatsuba_multiplication(a,c)
    bd = karatsuba_multiplication(b,d)
    ab_cd = karatsuba_multiplication(a+b, c+d)
    s3 = ab_cd - ac - bd
    result = (ac * (10 ** n1)) + (s3 * (10**(n1//2))) + bd
    
    return result

def main():
    x = 1234
    y = 5678
    print(karatsuba_multiplication(x,y))

if __name__ == '__main__':
    main()
