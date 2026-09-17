def countdown(n):
 if n==0:
  print("Done")
  return 0
 else:
  print(n)
  return 1 + countdown(n-1)
countdown(10)