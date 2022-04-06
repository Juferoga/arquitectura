import Register
import pyqt5_tools
import pyqt5_plugins
import Memory
import test





if __name__ == "__main__":
    main()
    window = test

    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
    
    """
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
    for i in range(103, 99, -1): #Little endian !
        print(hex(memory.byte[i]), end=" ")
    else:
        print()
 
    # register to register
    xmm[1].unsigned32[:] = xmm[0].unsigned32[:]
    xmm[1].float64[0] = xmm[0].float32[3]
 
    # mem to register
    xmm[0].unsigned32[0] = memory.unsigned32[100]
    print(hex(xmm[0].unsigned32[0])) # 0x882233FF
    """

