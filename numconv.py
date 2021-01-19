try:
    decimal = int(input("Integer in decimal: "))
    to_system = int(input("Target numeral system: "))
except:
    print("Invalid number")
else:
    binary = ""
    
    while decimal >= 1:
        binary += str(decimal % to_system) if decimal % to_system < 10 else chr(97 + ((decimal % to_system) - 10))
        decimal //= to_system
        
    print("Result: ", binary[::-1])

