# Code to help me in Cryptography class

## Extended euclidean algorithm for GCD

```
$ python eea.py 2021 1972

Q	A1	A2	A3	B1	B2	B3
-	1	0	2021	0	1	1972
1	0	1	1972	1	-1	49
40	1	-1	49	-40	41	12
4	-40	41	12	161	-165	1

gcd(2021,1972) = 1
inverse = -165 mod 2021 = 1856
```

## Euclidean algorithm for GCD
```
$ python gcd.py 2021 1972
2021 = 1972 * 1 + 49
1972 = 49 * 40 + 12
49 = 12 * 4 + 1
12 = 1 * 12 + 0

gcd:  1
```
