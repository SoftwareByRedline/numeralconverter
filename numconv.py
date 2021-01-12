try:
    decimal = int(input("Number in decimal: "))
    to_system = int(input("Target numeral system (number <= 10) "))
except:
    print("Invalid number")
if to_system > 10:
    print("Unsupported numeral system. Only supports decimal and \"lower\".")
else:
    target = ""
    
    while decimal >= 1:
        target += str(decimal % to_system)
        decimal //= to_system
        
    print("Result: ", target[::-1])