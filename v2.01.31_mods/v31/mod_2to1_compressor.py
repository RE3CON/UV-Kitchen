##Activates compander 4/3:1 (only compressor) when VOX is OFF
##Courtesy of LarSeN

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xA688:0xA688+2] == b'\xFB\xFF':
    print('Compressor OFF in Vox mode, for digital modes...')
    fw[0xA5F6:0xA5F6+72] = b'\x04\x46\x0D\x46\x60\x05\x44\x0D\x68\x05\x45\x0D\x05\x21\x49\x03\x21\x43\x46\x20\x00\xF0\xB1\xFC\x03\x21\xC9\x02\x29\x43\x79\x20\x00\xF0\xAB\xFC\x07\x49\x7A\x20\x00\xF0\xA7\xFC\x31\x20\x00\xF0\xD4\xF9\x08\x21\x88\x43\x04\x21\x01\x43\x31\x20\x00\xF0\x9D\xFC\x70\xBD\x9A\x28\x00\x00\x00\x00'
    print('Compressor ON anywhere else...')
    fw[0x1DBC:0x1DBC+4] = b'\x0A\xF0\xB2\xF9'	#Bork useless double-call
    fw[0x1CAA:0x1CAA+4] = b'\x08\xF0\xDD\xFC'	#Adjust call offset
    fw[0x5078:0x5078+4] = b'\x05\xF0\xF6\xFA'	#Adjust call offset
    fw[0x797C:0x797C+4] = b'\x02\xF0\x74\xFE'	#Adjust call offset
    fw[0xA668:0xA668+36] = b'\x10\xB5\x07\x49\x28\x20\x00\xF0\x7F\xFC\x31\x20\x00\xF0\xAC\xF9\x04\x21\x88\x43\x08\x21\x01\x43\x31\x20\x00\xF0\x75\xFC\x10\xBD\x38\x16\x00\x00'

else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
