# change below sets to new ones, values are in Hz
tx_low_limit  = 118_000_000
tx_high_limit = 629_999_900

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

print('Old tx low limit:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1534)[0]*10))
print('Old tx high limit: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1538)[0]*10))

fw[0x1534:0x1534+4] = struct.pack('<I',tx_low_limit//10) 
fw[0x1538:0x1538+4] = struct.pack('<I',tx_high_limit//10)

print('New tx low limit:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1534)[0]*10))
print('New tx high limit: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1538)[0]*10))

##--------------------- Portugal patch (pour invalider except_limits) --------------------------------------------
##if fw[0x1836:0x1836+2] == b'\xCF\x2A':
##    fw[0x1836:0x1836+2] = b'\x5D\xE0'
##else:
##    print('Function not found @0x1836. Wrong FW version or already patched')

open(sys.argv[1],'wb').write(fw)
