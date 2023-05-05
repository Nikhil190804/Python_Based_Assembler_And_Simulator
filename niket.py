# registers binary code
# R0="000"
d={"R1":"001",
"R2":"010",
"R3":"011",
"R4":"100",
"R5":"101",
"R6":"110",
}

# # type D instructions and opcode store
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
hlt=11010

# 
var = {}
register=["R0","R1","R2","R3","R4","R5","R6"]

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
#  
def type_A(instruct):
    if instruct[0]=="add":
        print(add,end="")
    elif instruct[0]=="sub":
        print(sub,end="")
    elif instruct[0]=="mul":
        print(mul,end="")
    elif instruct[0]=="xor":
        print(xor,end="")
    elif instruct[0]=="or":
        print(Or,end="")
    elif instruct[0]=="and":
        print(And,end="")
    print("00",end="")
    print(d[instruct[1]],end="")
    print(d[instruct[2]],end="")
    print(d[instruct[3]])
    

def type_B(instruct):
    if instruct[0]=="mov":
        print(movi,end="")
    elif instruct[0]=="ls":
        print(lsi,end="")
    elif instruct[0]=="rs":
        print(rsi,end="")
    print("0",end="")
    print(d[instruct[1]],end="")
    string=instruct[2]
    number = int(''.join(filter(str.isdigit, string)))
    fg = format(number, '07b')
    print(fg)


def type_C(instruct):

    if instruct[0]=="mov":
        print(mov,end="")
    elif instruct[0]=="div":
        print(div,end="")
    elif instruct[0]=="not":
        print(Not,end="")
    elif instruct[0]=="cmp":
        print(com,end="")
    
    print("00000",end="")
    print(d[instruct[1]],end="")
    print(d[instruct[2]])



def type_D(instruct):
    
    if instruct[0]=="ld":
        print(ld,end="")
        print(0,end="")#unused bit
        print(d[instruct[1]],end="")#register
        print(var[instruct[2]])
    else:
        print(st,end="")
        print(0,end="")#unused bit
        print(d[instruct[1]],end="")#register
        print(var[instruct[2]])

def type_E(instruct,line_counter):
    binary_line = format(line_counter-1, '07b')
    if instruct[0]=="jmp":
        print("01111",end="")
        print("0000",end="")
        print(binary_line)
    elif instruct[0]=="jlt":
        print("11100",end="")
        print("0000",end="")
        print(binary_line)
    elif instruct[0]=="jgt":
        print("11101",end="")
        print("0000",end="")
        print(binary_line)
    else:
        print("11111",end="")
        print("0000",end="")
        print(binary_line)


    



def find_type_of_instruction (instruct):          # func to find the type of instruction 
    if(instruct in possible_instructuion):
        return possible_instructuion[instruct]
    else:
        return -1
    



# main


with open("instructions.txt", "r") as file:
    instructions = file.readlines()




count=0
for j in instructions:
    ins = j.strip().split()
    if ins[0]!="var":
        
        count +=1


line_counter=0

for instruction in instructions:

    instruct = instruction.strip().split()
    result=find_type_of_instruction(instruct[0])


    if ((instruct[-1])=="hlt"):
        print(hlt,end="")
        print("0"*11)
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
                type_A(instruct)
            elif result=='B' and temp[0]=="$":
                type_B(instruct)
            elif result=='C' and temp[0]!="$":
                
                type_C(instruct)
            elif result=='B&C':
                if temp[0]=="$":
                
                    type_B(instruct)
                else:
                    type_C(instruct)

            elif result=='D':
                type_D(instruct)
            elif result=='E':
                type_E(instruct,line_counter)
        else:
            print("error has occurred in line:",end="")
            print(line_counter,end="")
            break
    line_counter+=1


    

    
    
        
        






