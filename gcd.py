import sys

teks = "{} = {} * {} + {}"
def gcd(a,b):  
  print(teks.format(a,b,a//b,a%b))
  if(a%b == 0): 
    print("\ngcd: ",a) 
    return 
  else: return gcd(b, a%b)

a = sys.argv[1]
b = sys.argv[2]
gcd(int(a),int(b))