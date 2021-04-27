import sys
import string

n = int(sys.argv[1]) % 26
print(n)
message = input("What is your message? ").upper()
message = message.replace(" ", "")
message = message.translate(str.maketrans('', '', string.punctuation))
print(message)
opp = ""
count = 0

for x in range(len(message)):
  result_ascii = (ord(message[x]) + int(n))
  #print(result_ascii)
    
  if result_ascii > 90:
    result_ascii -= 26
    #print(result_ascii)
  #print(opp)

  if (x % 5 == 0) and (x > 0):
    opp = opp + " "
    count += 1
    #print(opp)
    
  if count == 10:
    print(opp)
    opp = ""
    count = 0
    
  opp += chr(result_ascii)
  
print(opp)
      


