def find_type_of_instruction(str):          # func to find the type of instruction 
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
    line_counter+=1