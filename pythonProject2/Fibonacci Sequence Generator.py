n = int(input("Enter a number: "))
fib = [0, 1]
for i in range(0, n+1):
    fib.append(fib[i-1] + fib[i-2])
    print(fib[i],end=" ")