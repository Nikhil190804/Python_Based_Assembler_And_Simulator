opcode_b={"mov":"00010","rs":"01000","ls":"01001","not":"01101"}
reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
def decimalToBinary(n):#decimal conversions
    return bin(n).replace("0b", "").zfill(7) #converting it to 7 bit binary also convert decimal to binary
def type_b(command):
    try:
        opcode, operands,numbers= command.split(' ')#splitting into diffrents bit instructions
    except ValueError:
        raise ValueError('Invalid instruction: {}'.format(command)) #error if incoreect format
    if opcode in opcode_b.keys(): # checking the opcode instruction present in dictionary for grtting error
        op_b = opcode_b.get(opcode)
            
    else:
        raise ValueError('Unsupported opcode: {}'.format(opcode)) #error if incoreeect opcode'''
    
    if operands in reg.keys() :
        operands_bin = reg.get(operands) #getting resister code
    else:
        raise ValueError('incorrect registor: {}'.format(operands)) #error if incoreeect register number'''
    if numbers[0]=="$":
        s1=numbers.replace("$","") #removing dollar symbol
        
    else:
        raise ValueError('error,it should be $') #error if incoreeect symbol'''
    if int(s1)<=127 and int(s1)>=0: 
        s2=s1
    else:
        raise ValueError('error,it should be less than 128') #error if incoreeect decimal input'''
    return op_b + '_0_'+ operands_bin+ '_' + decimalToBinary(int(s2)) #combining all
assembly_code = 'ls R5 $11'
print(type_b(assembly_code))
