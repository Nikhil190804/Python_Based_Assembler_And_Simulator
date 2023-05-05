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
def type_A():
    print()
def type_B():
    print()
def type_C():
    print()



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


    



def find_type_of_instruction (instruct[0]):          # func to find the type of instruction 
    if(instruct[0] in possible_instructuion):
        return possible_instructuion[instruct[0]]
    else:
        return -1
    



# main


with open("instructions.txt", "r") as file:
    instructions = file.readlines()
print(instructions)



count=-1
for j in instructions:
    if j[0]!=var:
        count +=1


line_counter=0

for instruction in instructions:

    instruct = instruction.strip().split()
    result=find_type_of_instruction(instruct[0])


    if ((instruct[0])=="hlt"):
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
        if result !=-1:
            if(result=="A"):
                type_A(instruct)
            elif result=='B' or result=='C' or result=='B&C':
                #pinkykocall
                print("b&c")
            elif result=='D':
                type_D(instruct)
            elif result=='E':
                type_E(instruct,line_counter)
        else:
            print("error has occurred in line:",end="")
            print(line_counter,end="")
            break
    line_counter+=1

    

    
    
        
        







