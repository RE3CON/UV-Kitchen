## Changes the scrambler inversion frequency range. Step mod from 100Hz to 115.5Hz, in order to reach theorical scrambling maximum at 3730Hz (~step/2).
## Courtesy of LarSeN

scrstart = 2632 # SCR=1 lowest frequency. Change 2600 to any frequency in Hz

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())
 
if fw[0xA5D8] == 0x81 and fw[0xA5F0] == 0xDC :
    print('Changing scrambling freq step to 115.5Hz')
    fw[0xA5D8:0xA5D8+4] = b'\x95\x20\xC0\x00'
    print('Changing scrambling base freq to',scrstart,'Hz')
    fw[0xA5F0:0xA5F0+4] = struct.pack('<I',int(round(10.32444 * scrstart)))
    
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)

