# registers binary code

d={"R0":"000",
"R1":"001",
"R2":"010",
"R3":"011",
"R4":"100",
"R5":"101",
"R6":"110",
"FLAGS":"111"
}

#  type D instructions and opcode store
ld="00100"
st="00101"
add="00000"
sub="00001"
mul="00110"
xor="01010"
Or="01011"
And="01100"
movi="00010"
rsi="01000"
lsi="01001"
mov="00011"
div="00111"
Not="01101"
com="01110"

# # type f
hlt="11010"

# 
var = {}
register=["R0","R1","R2","R3","R4","R5","R6","FLAGS"]

# a string of special chars for type b instn.
special_chars="~`!@#$%^&*()_-=+{|}|:;'\"<>,.?/[]/*"

#
possible_instructuion={              #dict for type of instruction
   "add": "A",
   "sub": "A",
   "mov": "B&C",
   "ld": "D",
   "st": "D",
   "mul": "A",
   "div": "C",
   "rs": "B",
   "ls": "B",
   "xor": "A",
   "and": "A",
   "or": "A",
   "not": "C",
   "cmp": "C",
   "jmp": "E",
   "jlt": "E",
   "jgt": "E",
   "hlt": "F"
}
list_output=[]
#  
list_of_errors=[]


def error_has_occurred():
    file_handle=open("output.txt","w")
    file_handle.write(f"Error Has Occurred In Line:{line_counter+1}\n")
    file_handle.write(list_of_errors[0])
    file_handle.close()
    print(list_of_errors)
    exit(0)


def check_for_valid_registers(string):
    if(string in register):
        return 1
    else:
        return -1
    

def type_A(instruct,list_output):
    s=""
    if instruct[0]=="add":
        s += add
    elif instruct[0]=="sub":
        s += sub
    elif instruct[0]=="mul":
        s += mul 
    elif instruct[0]=="xor":
        s += xor
    elif instruct[0]=="or":
        s += Or
    elif instruct[0]=="and":
        s += And 
    s += "00"
    value1=check_for_valid_registers(instruct[1])
    value2=check_for_valid_registers(instruct[2])
    value3=check_for_valid_registers(instruct[3])
    if(value1==-1 or value2==-1 or value3==-1):#register is wrong
        error_string="register is invalid".title()
        list_of_errors.append(error_string)
        error_has_occurred()
    else:
        s += d[instruct[1]]
        s += d[instruct[2]]
        s += d[instruct[3]]
    list_output.append(s)


def check_for_valid_immediate_value(string):
    symbol=string[0]
    int_value=string[1:]
    if(symbol=="$"):
        if(0<=int(int_value)<=127):
            return 1
        else:
            return -2
    else:
        return -1

def type_B(instruct,list_output):
    s=""
    if instruct[0]=="mov":
        s += movi
    elif instruct[0]=="ls":
        s += lsi
    elif instruct[0]=="rs":
        s += rsi
    s += "0"
    value1=check_for_valid_registers(instruct[1])
    if(value1==-1): #register is worng
        error_string="register is invalid".title()
        list_of_errors.append(error_string)
        error_has_occurred()
    else:
        s += d[instruct[1]]
    result=check_for_valid_immediate_value(instruct[2])
    if(result==-1):
        list_of_errors.append("syntax error: invalid symbol!!!".title())
        error_has_occurred()
    elif (result==-2):
        list_of_errors.append("invalid immediate value!!!".title())
        error_has_occurred()
    else:
        string=instruct[2]
        number = int(''.join(filter(str.isdigit, string)))
        fg = format(number, '07b')
        s += fg
        list_output.append(s)


def type_C(instruct,list_output):
    s=""
    if instruct[0]=="mov":
        s += mov
    elif instruct[0]=="div":
        s += div 
    elif instruct[0]=="not":
        s += Not
    elif instruct[0]=="cmp":
        s += com
    
    s += "00000"
    value1=check_for_valid_registers(instruct[1])
    value2=check_for_valid_registers(instruct[2])
    if(value1==-1 or value2==-1):
        error_string="register is invalid".title()
        list_of_errors.append(error_string)
        error_has_occurred()
    else:
        s += d[instruct[1]]
        s += d[instruct[2]]
    list_output.append(s)

def type_D(instruct,list_output):
    s=""
    value1=check_for_valid_registers(instruct[1])
    if(value1==-1):
        error_string="register is invalid".title()
        list_of_errors.append(error_string)
        error_has_occurred()
    else:
        try:
            if instruct[0]=="ld":
                s += ld 
                s += "0" #unused bit
                s += d[instruct[1]] #register
                s += var[instruct[2]]
            else:
                s += st
                s += "0" #unused bit
                s += d[instruct[1]] #register
                s += (var[instruct[2]])
                list_output.append(s)
        except:
            list_of_errors.append("variable is not declared!!!".title())
            error_has_occurred()


def type_E(instruct,line_counter,list_output):
    s=""
    binary_line = format(line_counter-1, '07b')
    if instruct[0]=="jmp":
        s += "01111"
        s += "0000"
        s += binary_line
    elif instruct[0]=="jlt":
        s += "11100"
        s += "0000"
        s += binary_line
    elif instruct[0]=="jgt":
        s += "11101"
        s += "0000"
        s += binary_line
    else:
        s += "11111"
        s += "0000"
        s += binary_line
    list_output.append(s)


    
def find_type_of_instruction (instruct):          # func to find the type of instruction 
    if(instruct in possible_instructuion):
        return possible_instructuion[instruct]
    else:
        return -1
    


def file_output(list_output):
    file_handle=open("output.txt","w")
    for i in list_output:
        file_handle.write(i)
        file_handle.write('\n')
        file_handle.flush()
    file_handle.close()

# main
with open("input.txt", "r") as file:
    instructions = file.readlines()


count=0
for j in instructions:
    ins = j.strip().split()
    if(len(ins)<=1):
        pass
    elif( ins[0]!="var"):
        count +=1
    else:
        pass
print(count)
print(var)


line_counter=0
is_error=False
is_variable=True
for instruction in instructions:
    if(len(instruction)<=1 or len(instruction.strip())<=1):
        pass
    else:
        instruct = instruction.strip().split()
        print(instruct)
        result=find_type_of_instruction(instruct[0])
        temp_s=""
        if instruct[0]!="var":
            is_variable=False
        if ((instruct[-1])=="hlt"):
            temp_s += hlt
            temp_s += ("0"*11)
            list_output.append(temp_s)
            break
        elif instruct==[]:
            pass
        elif instruct[0]=="var":
            if instruct[1] not in var:
                binary = format(count, '07b')
                var[instruct[1]]=binary
                count +=1
            if (is_variable==False):
                # var is defined later 
                list_of_errors.append("variable not declared in the beginning!!!".title())
                error_has_occurred()
        else:
            temp=str(instruct[-1])
            if result !=-1:
                if(result=="A"):
                    type_A(instruct,list_output)
                elif result=='B' and temp[0] in special_chars:
                    type_B(instruct,list_output)
                elif result=='C' and temp[0] not in special_chars:
                    type_C(instruct,list_output)
                elif result=='B&C':
                    if temp[0] in special_chars:
                        type_B(instruct,list_output)
                    else:
                        type_C(instruct,list_output)
                elif result=='D':
                    type_D(instruct,list_output)
                elif result=='E':
                    type_E(instruct,line_counter,list_output)
            else:
                # instrution not found
                list_of_errors.append("wrong instruction!!!".title())
                error_has_occurred()
                break
    line_counter+=1

'''
output function here 
everthing has worked correctly
'''
file_output(list_output)   #output function here
