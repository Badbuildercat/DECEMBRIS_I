s = int(input("Ievadiet veselu pozitīvu skaitli: "))

def faktorials(s):
    resault = 1
 
    for i in range(1, s + 1):
        resault *= i
 
    return resault

print(f"Faktoriāls ir {faktorials(s)}.")