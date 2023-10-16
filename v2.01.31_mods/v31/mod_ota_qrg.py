#Sets new frequency for OTA codeplug transfer, by DO7OO
#default is 410.025 MHz

AIR_COPY_FREQ_HZ = 433_600_000

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x55D8:0x55D8+4] == b'\x04\xa6\x71\x02':
    print('Set new AIRCOPY frequency to {:.3f} MHz ...'.format(AIR_COPY_FREQ_HZ/1000/1000))
    fw[0x55D8:0x55D8+4] = struct.pack('<I',AIR_COPY_FREQ_HZ//10)
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
