
def process(i):
    return i*2


# 1: 1, 2 et 3 sont équivalents
print('\n11111111111')
for i in range(0, 10):
  if (i == 4):
      continue

  j = process(i)
  if (j == 0):
      continue

  print(j)

# 2: 1, 2 et 3 sont équivalents
print('\n22222222222222')
for i in range(0, 10):
  if (i == 4):
      pass
  else:
      j = process(i)
      if (j == 0):
          pass
      else:
          print(j)

# 3: 1, 2 et 3 sont équivalents
print('\n3333333333333')
for i in range(0, 10):
  if (i != 4):
      j = process(i)
      if (j != 0):
          print(j)
