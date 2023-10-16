#Enables AM option on all F* bands (not only F2)
#giant thanks to Gabi Zafiu for discovering the offsets and required patch for this!

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x62A2:0x62A2+1] == b'\x0B' and fw[0x62B6:0x62B6+1] == b'\x01' and fw[0x62BC:0x62BC+2] == b'\xB0\x7B':
    print('Enabling AM anywhere...')
    fw[0x62A2:0x62A2+1] = b'\x0E'
    fw[0x62B6:0x62B6+1] = b'\x04'
    fw[0x62BC:0x62BC+2] = b'\x01\xE0'
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
