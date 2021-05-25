#Enrique made this.
##Dredcode command class definition
class command:
    def __init__(self, I,Am,A,Bm,B,O):
        self.instruct = I
        self.Asmode   = Am
        self.Afield   = A
        self.Bsmode   = Bm
        self.Bfield   = B 
        self.owner    = O
#loads the constants from config
with open(config.txt , 'r') as f:
     *coresiz* = int(f.readline())
     *timelim* = int(f.readline())
     *sizelim* = int(f.readline())
     *Dprefix* = f.readline()
#this sets up the rules for Dredcode     
legalCommands = ['dat','mov','add','sub','mod',
                 'jmp','jmz','jmn','seq','sne',
                 'slt','nop','spl']
legalModes = ['~','#']
##this converts a string to a command
def untypedSTC(temp, owner):
    output = command(temp[0],temp[1],temp[2],temp[3],temp[4],owner)
    return output
def stringToCommand(string, owner):
    temp = string.split()
    if temp[0] in legalCommands:
        if temp[1] and temp[3] in legalModes:
            if isinstance(temp[2], int) and isinstance(temp[4], int)
                temp[2] = int(temp[2]) % *core*
                temp[4] = int(temp[4]) % *core*
                untypedSTC(temp, owner)
            else:
                print('adress not number')
                return 'error'
        else:
            print('one of the adressing modes is invalid')
            return 'error'
    else:
        print(temp[0] + ' is not a valid command')
        return 'error'
        
#get the file to load
#the prints are UI(not stricly needed)
print('Type the name of a warrior in the current directory,')
print('it should be a DREDCODE program with the line "Dredcode" attached.')
warrior = input()
#actually loading the thing now that we know what it is
with open(warrior, 'r') as f:
    #check if the warrior is viable(some how bugged)
    if f.readline() == *Dprefix*:
        #the file loading
        f.seek(2)
        warrior = f.readline()
        for i in range f.length():
            temp = f.readline()
            result = stringToCommand(temp, [0,0,0])
            append(result, warrior)
            if i > *sizelim*:
                break
    else:
        print('It\'s not a redcode file.')
