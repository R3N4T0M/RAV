def somaip(ip):
        a,b,c,d= ip.split('.')
        primeiro= (int(a) << 8) + int(b)
        segundo = (int(c) << 8) + int(d)
        binpri = bin(primeiro)
        binseg = bin(segundo)
        if len(binseg)<18:
                y=18-len(binseg)
                z='0'*y
                total=z+binseg
        return binpri, total

a= input()

print (somaip(a))
