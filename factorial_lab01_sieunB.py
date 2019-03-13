# factorial.py
#    Program to compute the factorial of a number by 2016310153 Sieun Bae 
#    Illustrates for loop with an accumulator

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
       fact = fact * factor
    print("The factorial of", n, "is", fact)

main()

