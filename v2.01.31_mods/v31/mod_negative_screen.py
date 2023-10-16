#Inverts LCD display. Good to be used with a rotated polarizer

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xB808] == 0xA6:
    print('Inverting LCD')
    fw[0xB808] = 0xA7
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
