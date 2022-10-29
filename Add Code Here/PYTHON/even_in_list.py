numList = []
print("Enter 10 Numbers: ")
for i in range(10):
  numList.insert(i, int(input()))

print("\nEven Numbers:")
for i in range(10):
  if numList[i]%2==0:
    print(numList[i])
