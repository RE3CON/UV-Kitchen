#Disables any TX capability

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x1836:0x1836+2] == b'\xCF\x2A':
    print('Disabling TX capability completely!')
    fw[0x1836:0x1836+2] = b'\xF0\xBD'
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
