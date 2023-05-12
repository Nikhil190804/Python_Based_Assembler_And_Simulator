'''def find_type_of_instruction(str):          # func to find the type of instruction 
    instruction=str.split()[0]
    if(instruction in possible_instructuion):
        return possible_instructuion[instruction]
    else:
        return -1
    
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
file_reader=[]          # a list to store all the lines as a string of input.txt
file_handle=open("input.txt","r")
file_reader=file_handle.readlines()
line_counter=1
for i in file_reader:
    if(len(i)==1): # the line is empty
        pass
    else: # line may be valid
        clean_string=i.strip()
        result=find_type_of_instruction(clean_string)
        if(result!=-1):
            if(result=="A"):
                #mohitkocall
                print('a type')
            elif result=='B' or result=='C' or result=='B&C':
                #pinkykocall 
                print("b&c")
            elif result=='D' or result=='E' or result=='F':
                #nikkocall
                print("d&e&f")
        else:
            print(f"error has occurred in line: {line_counter} !!!\nInstruction code is wrong ".title())
            exit(1)
    line_counter+=1'''



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
    s += d[instruct[1]]
    s += d[instruct[2]]
    s += d[instruct[3]]
    list_output.append(s)



    

def type_B(instruct,list_output):
    s=""
    if instruct[0]=="mov":
        s += movi
    elif instruct[0]=="ls":
        s += lsi
    elif instruct[0]=="rs":
        s += rsi
    s += "0"
    s += d[instruct[1]] 
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
    s += d[instruct[1]]
    s += d[instruct[2]]

    instruct.append(s)

def type_D(instruct,list_output):
    s=""
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

def error_has_occurred(string):
    file_handle=open("output.txt","w")
    file_handle.write(string+"\n")
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


line_counter=0
is_error=False
for instruction in instructions:
    if(len(instruction)<=1):
        pass
    else:
        instruct = instruction.strip().split()
        result=find_type_of_instruction(instruct[0])
        temp_s=""
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
        else:
            temp=str(instruct[-1])
            if result !=-1:
                if(result=="A"):
                    type_A(instruct,list_output)
                elif result=='B' and temp[0]=="$":
                    type_B(instruct,list_output)
                elif result=='C' and temp[0]!="$":
                    type_C(instruct,list_output)
                elif result=='B&C':
                    if temp[0]=="$":
                        type_B(instruct,list_output)
                    else:
                        type_C(instruct,list_output)

                elif result=='D':
                    type_D(instruct,list_output)
                elif result=='E':
                    type_E(instruct,line_counter,list_output)
            else:
                is_error=True
                temp_s=""
                temp_s += "error has occurred in line: ".title()
                temp_s += str(line_counter+1)
                temp_s+="\n"
                temp_s+="wrong instruction!!!".title()
                break
    line_counter+=1

'''
print(list_output)
output function here 
'''
print(var)
if(is_error==True):
    error_has_occurred(temp_s)
else:
    file_output(list_output)   #output function here

