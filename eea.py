import sys
# print("masukkan angka pertama: ")
# a = int(input())
# print("masukkan angka kedua: ")
# b = int(input())
a = int(sys.argv[1])
b = int(sys.argv[2])
print("Q\tA1\tA2\tA3\tB1\tB2\tB3")
teks = "{}\t{}\t{}\t{}\t{}\t{}\t{}"
q = "-"
a1 = 1
a2 = 0
a3 = a
b1 = 0
b2 = 1
b3 = b
print(teks.format(q,a1,a2,a3,b1,b2,b3))
while (b3!=0 and b3!=1):
    q = a3//b3
    t1 = a1-q*b1
    t2 = a2-q*b2
    t3 = a3-q*b3
    a1 = b1
    a2 = b2
    a3 = b3
    b1 = t1
    b2 = t2
    b3 = t3
    print(teks.format(q,a1,a2,a3,b1,b2,b3))
if(b3 == 1):
    print("gcd({},{}) = {}".format(a,b,b3))
    print("inverse = {} mod {} = {}".format(b2,a,b2%a))
else:
    print("gcd({},{}) = {}".format(a,b,a3))
    print("inverse = {}".format("None"))