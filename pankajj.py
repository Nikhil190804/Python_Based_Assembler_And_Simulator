#TYPE B CODE BELOW
opcode_b={"mov":"00010","rs":"01000","ls":"01001"}
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
        raise ValueError('Unsupported opcode: {}'.format(opcode)) #error if incoreeect opcode for finding error'''
    
    if operands in reg.keys() :
        operands_bin = reg.get(operands) #getting resister code
    else:
        raise ValueError('incorrect registor: {}'.format(operands)) #error if incoreeect register number for finding error'''
    if numbers[0]=="$":
        s1=numbers.replace("$","") #removing dollar symbol
        
    else:
        raise ValueError('error,it should be $') #error if incoreeect symbol for finding error'''
    if int(s1)<=127 and int(s1)>=0: 
        s2=s1
    else:
        raise ValueError('error,it should be less than 128') #error if incoreeect decimal input for finding error'''
    return op_b + '_0_'+ operands_bin+ '_' + decimalToBinary(int(s2)) #combining all for proper output
assembly_code = 'mov R4 $100'
print(type_b(assembly_code))

#TYPE C CODE BELOW___________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________

opcode_c={"mov":"00011","div":"00111","not":"01101","cmp":"01110"}
reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}

def type_c(command):
    try:
        opcode, operand1,operand2= command.split(' ')#splitting into diffrents bit instructions for operating them
    except ValueError:
        raise ValueError('Invalid instruction: {}'.format(command)) #error if incoreect format for finfing error
    if opcode in opcode_c.keys(): # checking the opcode instruction present in dictionary for grtting error
        op_b = opcode_c.get(opcode) 
            
    else:
        raise ValueError('Unsupported opcode: {}'.format(opcode)) #error if incoreeect opcode for finding mistakes'''
    
    if operand1 in reg.keys() :
        operands_bin1 = reg.get(operand1) #getting resister code for input
    else:
        raise ValueError('incorrect registor: {}'.format(operand1)) #error if incoreeect register1 number for grtiing error'''
    if operand2 in reg.keys() :
        operands_bin2 = reg.get(operand2) #getting resister code for input
    else:
        raise ValueError('incorrect registor: {}'.format(operand2)) #error if incoreeect register2 number for getting error'''
    
    return op_b + '_00000_'+ operands_bin1+ '_' + operands_bin2 #combining all for proper output
assembly_code = 'mov R5 R6'
print(type_c(assembly_code))
