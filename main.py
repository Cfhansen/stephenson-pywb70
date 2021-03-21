###solution to problem 70 in ben stephenson's "the python workbook".

letters_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letters_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

message = input('Enter a message to be enciphered:')
shift = int(input('Enter the amount of the shift:'))
newmessage = ''

for l in message:
  mydict = []
  if not (l in letters_lower) and not (l in letters_upper):
    newmessage = newmessage + l
  elif l in letters_lower:
    mydict = letters_lower
  else:
    mydict = letters_upper
  
  if mydict != []:
    target = mydict.index(l) + shift
    if target > 25:
      target = target % 26
    newmessage = newmessage + mydict[target]

print(newmessage)
