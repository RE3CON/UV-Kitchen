##Ported to v2.00.31
shellcode = b'\x10\xB5\x0A\x4B\x1A\x88\x01\x2A\x0D\xD1\x09\x4A\x51\x88\x10\x88\x09\x04\x01\x43\x07\x4A\x50\x88\x14\x88\x00\x04\x20\x43\x0B\xF0\xB3\xF8\x00\x20\x10\xBD\x08\x21\x03\x48\xF8\xE7\x88\x05\x00\x20\x8E\x05\x00\x20\x8A\x05\x00\x20\x68\x0D\x00\x00\x55\x6E\x6B\x6E\x20\x72\x65\x71'

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

fw[0x0D2C:0x0D2C+68] = shellcode
fw[0x0D2C+68:0x0E20] = b'\x00'*176   #Freed bytes to 00

open(sys.argv[1],'wb').write(fw)

