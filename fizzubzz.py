def dodawanie(a,b):
    return a+b

c=dodawanie(10,7)

print(c)


def fizzbuzz(x):

    if x%15==0:
        print("fizzbuzz")

    elif x%3==0:
        print("fizz")

    elif x%5==0:
        print("buzz")


for liczba in range(100):
    print(liczba)
    fizzbuzz(liczba)