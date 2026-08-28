from random import randrange

# Public files (challenge specific)
from machine import Machine
from assembly import assembly

def FizzBuzz(start, stop):
    res = b""
    for i in range(start, stop):
        if (i%3) == 0:
            res += b"Fizz"
        if (i%5) == 0:
            res += b"Buzz"
        if (i%3) != 0 and (i%5)!=0:
            res += str(i).encode("ascii")
        res += b" "
    res = res[:-1]
    return res

def testCode(machine, start, stop):
    machine.reset()
    machine.R1 = start
    machine.R2 = stop
    machine.runCode()

    expected = int.from_bytes(FizzBuzz(start, stop))

    if expected != machine.R0:
        print("Nope!")
        exit(1)

def easy(code):
    # Initialize
    machine = Machine(code)

    testCode(machine, 1, 100)

    flag = open("flag_easy.txt").read().strip()
    print(f"[+] Congrats! Here is the easy flag: {flag}")

def medium(code):
    # Initialize
    machine = Machine(code, banned=["DIV", "MOD", "FP", "POW", "GCD"])

    if len(machine.code) > 1024:
        print("Less code please")
        exit()

    testCode(machine, 0, 100)
    for _ in range(100):
        stop = randrange(1,1000)
        start = randrange(stop)
        testCode(machine, start, stop)

    flag = open("flag_medium.txt").read().strip()
    print(f"[+] Congrats! Here is the medium flag: {flag}")

if __name__ == "__main__":
    try:
        print("Enter you bytecode in hexadecimal:")
        code = input(">>> ")

        while True:
            print("Which flag do you want to grab?")
            print(" 0. Quit.")
            print(" 1. Easy Flag")
            print(" 2. Medium Flag")
            choice = int(input(">>> "))

            if   choice == 0: exit()
            elif choice == 1: easy(code)
            elif choice == 2: medium(code)
    except:
        print("Please check your inputs.")
