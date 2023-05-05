opcode={"add":"00000","sub":"00001","mul":"00110","xor":"01010","or":"01011","and":"01100"}
registers={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}

def assemble(instruction):

    try:
        opcode, operands1,operands2,operands3 = instruction.split(' ')
    except ValueError:
        raise ValueError('Invalid instruction: {}'.format(instruction))

    if opcode == 'add':
        opcode_bin = '00000_00'
    elif opcode=='sub':
        opcode_bin='00001_00'
    elif opcode=='mul':
        opcode_bin='00110_00'
    elif opcode=='xor':
        opcode_bin='01010_00'
    elif opcode=='or':
        opcode_bin='01011_00'
    elif opcode=='and':
        opcode_bin='01100_00'            
    else:
        raise ValueError('Unsupported opcode: {}'.format(opcode))
    if operands1 in registers.keys() :
        operands_bin = registers.get(operands1) #getting register code
    else:
        raise ValueError('incorrect registers: {}'.format(operands1)) #error if incorrect register number'''
    if operands2 in registers.keys() :
        operands_bin = registers.get(operands2) #getting register code
    else:
        raise ValueError('incorrect registers: {}'.format(operands2)) #error if incorrect register number'''
    if operands3 in registers.keys() :
        operands_bin = registers.get(operands3) #getting register code
    else:
        raise ValueError('incorrect registers: {}'.format(operands3)) #error if incorrect register number'''

    return opcode_bin + '_' + operands_bin
assembly_code = 'mul R0 R1 R2'
binary_code = assemble(assembly_code)
print(binary_code)


