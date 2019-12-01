def somaip(ip):
        a,b,c,d= ip.split('.')
        primeiro= (int(a) << 8) + int(b)
        segundo = (int(c) << 8) + int(d)
        binpri = bin(primeiro)
        binseg = bin(segundo)
        return binpri, binseg

a= input()

print (somaip(a))
