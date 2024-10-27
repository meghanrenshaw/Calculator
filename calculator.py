
### CHALLENGE 
import re
### iterate through input

def equation():
    expression = (input("write your problem: "))
    pattern = r"([0-9]+\.?[0-9]*)([+*/-])([0-9]+\.?[0-9]*)"

    while re.search(pattern, expression):
        match = re.search(pattern, expression)
        if not match:
            break

        numberone = float(match.group(1))
        symbol = match.group(2)
        numbertwo = float(match.group(3))
        
        if symbol == "+":
            result = numberone + numbertwo
        elif symbol == "-":
            result = numberone - numbertwo
        elif symbol == "*":
            result = numberone * numbertwo
        elif symbol == "/":
            result = numberone / numbertwo        

        expression = expression[:match.start()] + str(result) + expression[match.end():]
    print(expression)
    
equation()