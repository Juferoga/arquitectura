from atexit import register
import opcode
from pickletools import opcodes
import struct

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
        'JOF' : 0xd,
        'JN'  : 0xe,
        'BRK' : 0xf,
        'HLT' : 0x10,
        'AND' : 0x11,
        'OR'  : 0x12,
        'XOR' : 0x13,
        'CLR' : 0x14 
    }

    def __init__(self,  ):
        pass
    
    def instrucion(opcode):
        switcher = {
        1: ,
        2: ,
        3: ,
        4: ,
        5: ,
        6: ,
        7: ,
        8: ,
        9: ,
        10: ,
        11: ,
        12: ,
        13: ,
        14: ,
        15:,
        16:,
        17:,
        18:,
        19:,
        20:

    }
        





      }  
        
       


# Registros 
# Contador de programa (PC, program counter).
# Registro de entrada y de dirección de memoria (input and MAR, input and memory address register).
# Registro de instrucción (IR, instruction register).

proConter = Register()
registerMar = Register()
registerIR = Register()

registerOut = Register()
registerStatus = Register()
registerA = Register()
registerB = Register()

# Memorias
# Memoria de acceso aleatorio (RAM, random-access memory)
#tam 16×8 (16 posiciones de 8 bits cada una)

MemoryRam = Memory(8) 


MemoryRam = []


def ALU():
    


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