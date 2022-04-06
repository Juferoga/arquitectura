from atexit import register
from inspect import stack
import opcode
from pickletools import opcodes
from posixpath import split
import struct
import time
import pyautogui as pg
import os


class Register:
    class Wrapper: 
        def __init__ (self, buffer, format_str):
            self.buffer = buffer
            self.st = struct.Struct(format_str)
 
        def __setitem__ (self, slot, value):
            f = list(self.st.unpack(self.buffer))
            f[slot] = value
            self.st.pack_into(self.buffer, 0, *f)
 
        def __getitem__ (self, slot):
            return self.st.unpack(self.buffer)[slot]
 
        def __string__ (self):
            return str(self.st.unpack(self.buffer))
 
        def __repr__ (self):
            return repr(self.st.unpack(self.buffer))
 
    def __init__ (self):
        self.byte = bytearray(16)
        self.float32 = Register.Wrapper(self.byte, "<ffff")
        self.float64 = Register.Wrapper(self.byte, "<dd")
        self.signed8 = Register.Wrapper(self.byte, "<bbbbbbbbbbbbbbbb")
        self.signed16 = Register.Wrapper(self.byte, "<hhhhhhhh")
        self.signed32 = Register.Wrapper(self.byte, "<iiii")
        self.signed64 = Register.Wrapper(self.byte, "<qq")
        self.unsigned8 = Register.Wrapper(self.byte, "<BBBBBBBBBBBBBBBB")
        self.unsigned16 = Register.Wrapper(self.byte, "<HHHHHHHH")
        self.unsigned32 = Register.Wrapper(self.byte, "<IIII")
        self.unsigned64 = Register.Wrapper(self.byte, "<QQ")
 
class Memory:
    class Wrapper:
        def __init__ (self, buffer, format_str):
            self.buffer = buffer
            self.st = struct.Struct(format_str)
 
        def __setitem__ (self, address, value):
            self.st.pack_into(self.buffer, address, value)
 
        def __getitem__ (self, address):
            return self.st.unpack_from(self.buffer, address)[0]
 
    def __init__ (self, size):
        self.size = size
        self.byte = bytearray(size)
        self.float32 = Memory.Wrapper(self.byte, "<f")
        self.float64 = Memory.Wrapper(self.byte, "<d")
        self.signed8 = Memory.Wrapper(self.byte, "<b")
        self.signed16 = Memory.Wrapper(self.byte, "<h")
        self.signed32 = Memory.Wrapper(self.byte, "<i")
        self.signed64 = Memory.Wrapper(self.byte, "<q")
        self.unsigned8 = Memory.Wrapper(self.byte, "<B")
        self.unsigned16 = Memory.Wrapper(self.byte, "<H")
        self.unsigned32 = Memory.Wrapper(self.byte, "<I")
        self.unsigned64 = Memory.Wrapper(self.byte, "<Q")
 
    def __len__ (self):
        return len(self.byte)

class cpu:
    # Dic opCode
    #hexadecimal
    opCode = {
        'NOP' : 0x0,
        'MOV' : 0x1,
        'INCB': 0x2,
        'INCA': 0x3,
        'SUM' : 0x4,
        'SIM' : 0x5,
        'SUB' : 0x6,
        'NOT' : 0x7,
        'PUSH': 0x8,
        'POP' : 0x9,
        'JMP' : 0xa,
        'JZ'  : 0xb,
        'JC'  : 0xc,
        'JOF' : 0xd, # overflow
        'JN'  : 0xe, # negative
        'BRK' : 0xf, # Jump final
        'HLT' : 0x10,
        'AND' : 0x11,
        'OR'  : 0x12,
        'XOR' : 0x13,
        'CLR' : 0x14 
    }

    def __init__(self,  ):
        pass

# Registros 
# Contador de programa (PC, program counter).
# Registro de entrada y de dirección de memoria (input and MAR, input and memory address register).
# Registro de instrucción (IR, instruction register).

programConter = Register()
registerMar = Register()
registerIR = Register()

registerOut = Register()
registerStatus = Register()
registerA = Register()
registerB = Register()

hlt = False
# Memorias
# Memoria de acceso aleatorio (RAM, random-access memory)
#tam 16×8 (16 posiciones de 8 bits cada una)

MemoryRam = Memory = []


    def instrucion(opcode, register):
        stack = [] 
        if opcode == '0':
            print('No operación')
        elif opcode == '1':
            print('Mueve')
        elif opcode == '2':
            print('Incrementa B')
            return registerB+1 
        elif opcode == '3':
            print('Incrementa A')
            return registerA+1 
        elif opcode == '4':
            print('Suma')
            return registerB+registerA
        elif opcode == '5':
            print('suma + incremento')
            return registerB+registerA+1
        elif opcode == '6':
            print('Substracción')
            return registerB-registerA
        elif opcode == '7':
            print('Operación lógica NO')
            def inversa(a):
                if a == 0:
                    return 1
                else:
                    return 0
            registertemp = str(registerB)
            mapObject = map(int,registertemp)
            separate = list(mapObject)
            registerB = map(inversa,separate)
            return registerB 
        elif opcode == '8':
            print('PUSH')
            stack.append(register)
        elif opcode == '9':
            print('POP')
            try:
                return stack.pop()
            except IndexError:
                raise ValueError("La pila está vacía")
        elif opcode == '10':
            print('JUMP')
            return #registerA+1 // binario
        elif opcode == '11':
            print('JUMP ZERO')
            return #registerB suma posicion
        elif opcode == '12':
            print('JUMP CARRIE')
        elif opcode == '13':
            print('JUMP OVER FLOW')
            
        elif opcode == '14':
            print('JUMP N')
            
        elif opcode == '15':
            print('BREAK')
            #break
        elif opcode == '16':
            print('HALT')
            
        elif opcode == '17':
            print('AND')
            
        elif opcode == '18':
            print('OR')
            
        elif opcode == '19':
            print('XOR')
            
        elif opcode == '20':
            print('CLEAR')
            MemoryRam.clear()
        else:
            print("opcode no inscrito")
        

def verifica(numBotton, lines):
    
    if numBotton  == '0':
       for x in range(lines):       
            time.sleep(0.3)
            #pg.press("Enter")
    elif numBotton == '1':
       for x in range(lines):       
            time.sleep(0.3)
            #pg.press("Enter")
    else:
        return "NA"






     
        
       





    


if __name__ == "__main__":
    # 1000 bytes memory
    memory = Memory(1000) 
 
    # 16x 128 bits SSE registers
    xmm = []
    for i in range(16):
        xmm.append(Register())
 
    #test register aliasing    
    xmm[0].unsigned32[:] = (4, 5, 6, 7) # fill the whole register (4 x 32 bits)
    temp = xmm[0].float64[:] # copy as float64 (2 x 64 bits)
    xmm[0].float64[:] = temp # write back
    print("xmm[0]:", xmm[0].unsigned32) # (4, 5, 6, 7)
 
    # memory aliasing
    memory.unsigned32[100] = 0x882233FF
    
    for i in range(103, 1, 99): #Little endian !
        print(hex(memory.byte[i]), end=" ")
    else:
        print()
 
    # register to register
    xmm[1].unsigned32[:] = xmm[0].unsigned32[:]
    xmm[1].float64[0] = xmm[0].float32[3]
 
    # mem to register
    xmm[0].unsigned32[0] = memory.unsigned32[100]
    print(hex(xmm[0].unsigned32[0])) # 0x882233FF