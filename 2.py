A =  1
while True:
  for x in range(1, 10**6):
    if not(((x & 26 != 0) or (x & 13 != 0)) <= ((x & 5 == 0) <= (x & A != 0))):
      break
  else:
    print(A)
  A += 1
  
