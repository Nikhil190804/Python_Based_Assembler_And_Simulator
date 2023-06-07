instructions=[]

memory=[]
#list1=["0001000100001010","0001001001100100","0011000011010001","0010101100000101","1101000000000000"]
registers={"000":"R0",
"001":"R1",
"010":"R2",
"011":"R3",
"100":"R4",
"101":"R5",
"110":"R6","111":"FLAGS",
}

register_value={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}
v_overflow_bit=0
e_equal_bit=0
l_less_than_bit=0
g_greater_than_bit=0

# s="0001000100001010"
# reg_a=registers[s[7:10]]
# reg_b=registers[s[10:13]]
# reg_c=registers[s[13:16]]
    

# print(reg_a,reg_b,reg_c)

#s="0001000100001010"





def adder(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    #overflow
    if(register_value[reg_b]+register_value[reg_c] > 65536):
        v_overflow_bit=1
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
    else:
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
        v_overflow_bit=0
        register_value[reg_a]=register_value[reg_b]+register_value[reg_c]
    # print(reg_a,reg_b,reg_c)
    # print(register_value[reg_a])

def subtract(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    if((register_value[reg_b]-register_value[reg_c] > 65536) or (register_value[reg_c]>register_value[reg_b])):
        v_overflow_bit=1
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
        print("h")
    else:
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
        v_overflow_bit=0
        register_value[reg_a]=register_value[reg_b]-register_value[reg_c]
    # print(reg_a,reg_b,reg_c)
    # print(register_value[reg_a])


def multiply(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    if(register_value[reg_b] * register_value[reg_c] > 65536):
        v_overflow_bit=1
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0

    else:
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
        v_overflow_bit=0
        register_value[reg_a]=register_value[reg_b] * register_value[reg_c]
    # print(reg_a,reg_b,reg_c)
    # print(register_value[reg_a])

def xor(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    register_value[reg_a]=register_value[reg_b] ^ register_value[reg_c]
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0
    # print(reg_a,reg_b,reg_c)
    # print(register_value[reg_a])

def OR(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    register_value[reg_a]=register_value[reg_b] | register_value[reg_c]
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0
    # print(reg_a,reg_b,reg_c)
    # print(register_value[reg_a])

def AND(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    register_value[reg_a]=register_value[reg_b] & register_value[reg_c]
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0
    # print(reg_a,reg_b,reg_c)
    # print(register_value[reg_a])

def move_imm(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global g_greater_than_bit
    global l_less_than_bit
    reg_a=registers[s[6:9]]
    value=int(s[9:16],base=2)
    register_value[reg_a]=value
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0

def move(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit

    reg_a=registers[s[10:13]]
    reg_b=registers[s[13:16]]
    if reg_b=="FLAGS":
        temp=""
        temp += 12*"0"
        temp += str(v_overflow_bit) + str(l_less_than_bit) +  str(g_greater_than_bit) + str(e_equal_bit)
        a=int(temp,base=2)
        value_regb = a
    else:
        value_regb = register_value[reg_b]

    register_value[reg_a]=value_regb
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0

def divide(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    reg_a=registers[s[10:13]]
    reg_b=registers[s[13:16]]
    if(reg_b==0):
        v_overflow_bit=1
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
    else:
        value_rega = register_value[reg_a]
        value_regb = register_value[reg_b]
        q = value_rega // value_regb
        r = value_rega % value_regb
        register_value["R0"] = q
        register_value["R1"] = r
        e_equal_bit=0
        g_greater_than_bit=0
        l_less_than_bit=0
        v_overflow_bit=0

def NOT(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    reg_a=registers[s[10:13]]
    reg_b=registers[s[13:16]]
    
    value_regb = register_value[reg_b]
    temp = ~value_regb
    register_value[reg_a]=temp
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0

def right_shift(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    reg_a=registers[s[6:9]]
    value=int(s[9:16],base=2)
    temp=""
    temp += "0"*value
    binary_num = str(format(register_value[reg_a], 'b'))
    temp += binary_num
    result = format(temp, '016b')
    register_value[reg_a]=int(result,base="2")
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0


def left_shift(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    reg_a=registers[s[6:9]]
    value=int(s[9:16],base=2)
    binary_num = str(format(register_value[reg_a], 'b'))
    binary_num += "0"*value
    result = format(binary_num, '016b')
    register_value[reg_a]=int(result,base="2")
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0


def load(s):
    global register_value
    global memory
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    memory_address=int(s[9:16],base=2)
    mem_to_be_inserted=memory[memory_address]
    reg_a=registers[s[6:9]]
    register_value[reg_a]=mem_to_be_inserted
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0


def store(s):
    global register_value
    global memory
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    memory_address=int(s[9:16],base=2)
    reg_a=registers[s[6:9]]
    memory[memory_address]=register_value[reg_a]
    e_equal_bit=0
    g_greater_than_bit=0
    l_less_than_bit=0
    v_overflow_bit=0


def compare(s):
    global register_value
    global e_equal_bit
    global v_overflow_bit
    global l_less_than_bit
    global g_greater_than_bit
    reg_a=registers[s[10:13]]
    reg_b=registers[s[13:16]]
    if(register_value[reg_a]==register_value[reg_b]):
        e_equal_bit=1
        g_greater_than_bit=0
        l_less_than_bit=0
        v_overflow_bit=0
    elif(register_value[reg_a]<register_value[reg_b]):
        l_less_than_bit=1
        v_overflow_bit=0
        g_greater_than_bit=0
        e_equal_bit=0
    elif(register_value[reg_a]>register_value[reg_b]):
        g_greater_than_bit=1
        v_overflow_bit=0
        l_less_than_bit=0
        e_equal_bit=0


def jmp(s):
    global e_equal_bit
    global v_overflow_bit
    global l_less_than_bit
    global g_greater_than_bit
    global program_counter
    label_address=s[9:16]
    new_pc=int(label_address,base=2)
    g_greater_than_bit=0
    v_overflow_bit=0
    l_less_than_bit=0
    e_equal_bit=0
    print_output()
    program_counter=new_pc

def jlt(s):
    global program_counter
    global e_equal_bit
    global v_overflow_bit
    global l_less_than_bit
    global g_greater_than_bit
    label_address=s[9:16]
    if(l_less_than_bit==1):
        new_pc=int(label_address,base=2)
    else:
        new_pc=program_counter+1
    g_greater_than_bit=0
    v_overflow_bit=0
    l_less_than_bit=0
    e_equal_bit=0
    print_output()
    program_counter=new_pc

def jgt(s):
    global program_counter
    global e_equal_bit
    global v_overflow_bit
    global l_less_than_bit
    global g_greater_than_bit
    label_address=s[9:16]
    if(g_greater_than_bit==1):
        new_pc=int(label_address,base=2)
    else:
        new_pc=program_counter+1
    g_greater_than_bit=0
    v_overflow_bit=0
    l_less_than_bit=0
    e_equal_bit=0
    print_output()
    program_counter=new_pc

def je(s):
    global program_counter
    global e_equal_bit
    global v_overflow_bit
    global l_less_than_bit
    global g_greater_than_bit
    label_address=s[9:16]
    if(e_equal_bit==1):
        new_pc=int(label_address,base=2)
    else:
        new_pc=program_counter+1
    g_greater_than_bit=0
    v_overflow_bit=0
    l_less_than_bit=0
    e_equal_bit=0
    print_output()
    program_counter=new_pc


def end_function():
    for i in memory:
        if(type(i)==str):
            print(i.strip())
        else:
            bin_value=str(format(i,'016b'))
            print(bin_value)

def print_output():
    global program_counter
    global register_value
    binary_num = str(format(program_counter, '07b'))
    print(binary_num,end="        ")
    for value in register_value.values():
        temp=str(format(value, '016b'))
        print(temp,end=" ")
    print("0"*12,end="")
    print(v_overflow_bit,end="")
    print(l_less_than_bit,end="")
    print(g_greater_than_bit,end="")
    print(e_equal_bit,end="\n")
    

'''
here is question 4:-----------------
'''
def clr(s):
    global register_value
    for key in register_value:
        register_value[key] = 0

def add_imm_reg(s):
    global register_value
    global v_overflow_bit
    global e_equal_bit
    global l_less_than_bit
    global g_greater_than_bit
    reg_a=registers[s[6:9]]
    value=int(s[9:16],base=2)
    if(register_value[reg_a]+value > 65536):
        v_overflow_bit=1
        l_less_than_bit=0
        g_greater_than_bit=0
        e_equal_bit=0
    register_value[reg_a] += value
    v_overflow_bit=0
    l_less_than_bit=0
    e_equal_bit=0
    g_greater_than_bit=0


def increment(s):
    global register_value
    global e_equal_bit
    global g_greater_than_bit
    global v_overflow_bit
    global l_less_than_bit
    reg_a=registers[s[13:16]]
    if(register_value[reg_a]+1 > 65536):
        v_overflow_bit=1
        e_equal_bit=0
        l_less_than_bit=0
        g_greater_than_bit=0
    else:
        register_value[reg_a] += 1
        v_overflow_bit=0
        e_equal_bit=0
        l_less_than_bit=0
        g_greater_than_bit=0


def decrement(s):
    global register_value
    global e_equal_bit
    global g_greater_than_bit
    global v_overflow_bit
    global l_less_than_bit
    reg_a=registers[s[13:16]]
    if(register_value[reg_a]+1 > 65536):
        v_overflow_bit=1
        e_equal_bit=0
        l_less_than_bit=0
        g_greater_than_bit=0
    else:
        register_value[reg_a] -= 1
        v_overflow_bit=0
        e_equal_bit=0
        l_less_than_bit=0
        g_greater_than_bit=0


def exponential(s):
    global register_value
    global v_overflow_bit
    global l_less_than_bit
    global g_greater_than_bit
    global e_equal_bit
    reg_a=registers[s[7:10]]
    reg_b=registers[s[10:13]]
    reg_c=registers[s[13:16]]
    #overflow
    if(register_value[reg_b]**register_value[reg_c] > 65536):
        v_overflow_bit=1
        e_equal_bit=0
        l_less_than_bit=0
        g_greater_than_bit=0
    else:
        register_value[reg_a]=register_value[reg_b]**register_value[reg_c]
        v_overflow_bit=0
        e_equal_bit=0
        l_less_than_bit=0
        g_greater_than_bit=0


#main

#take input

while True:
    try:
        line=input()
        line=line.strip()
        if(line!=""):
            instructions.append(line)
    except EOFError:
       break
'''with open("input.txt", "r") as file:
    instructions = file.readlines()'''

for i in instructions:
    memory.append(i)
len_of_mem_now=len(memory)
for i in range(128-(len(instructions))):
    memory.append(0)
max_program_length=len(instructions)


program_counter=0

while((program_counter < max_program_length) and (instructions[program_counter][0:5]!="11010")):
    
    if(instructions[program_counter][0:5]=="00000"):
        adder(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00001"):
        subtract(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00010"):
        move_imm(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00011"):
        move(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00100"):
        load(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00101"):
        store(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00110"):
        multiply(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="00111"):
        divide(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01000"):
        right_shift(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01001"):
        left_shift(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01010"):
        xor(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01011"):
        OR(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01100"):
        AND(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01101"):
        NOT(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01110"):
        compare(instructions[program_counter])
        print_output()
        program_counter+=1
    elif(instructions[program_counter][0:5]=="01111"):
        
        jmp(instructions[program_counter])
        
    elif(instructions[program_counter][0:5]=="11100"):
        
        jlt(instructions[program_counter])
        
    elif(instructions[program_counter][0:5]=="11101"):
        
        jgt(instructions[program_counter])
        
    elif(instructions[program_counter][0:5]=="11111"):
     
        je(instructions[program_counter])
        
    elif(instructions[program_counter][0:5]=="11001"):
        clr(instructions[program_counter])
        print_output()
        program_counter+=1

    elif(instructions[program_counter][0:5]=="11110"):
        add_imm_reg(instructions[program_counter])
        print_output()
        program_counter+=1

    elif(instructions[program_counter][0:5]=="10011"):
        exponential(instructions[program_counter])
        print_output()
        program_counter+=1

    elif(instructions[program_counter][0:5]=="10100"):
        increment(instructions[program_counter])
        print_output()
        program_counter+=1

    elif(instructions[program_counter][0:5]=="10101"):
        decrement(instructions[program_counter])
        print_output()
        program_counter+=1

    
v_overflow_bit=0
e_equal_bit=0
g_greater_than_bit=0
l_less_than_bit=0
print_output()
end_function()