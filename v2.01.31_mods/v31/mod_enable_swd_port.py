#Enables SWD debugging port which is normally disabled during normal firmware boot
#thanks for https://github.com/manujedi

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xB994:0xB994+2] == b'\xC8\x60':
    fw[0xB994:0xB994+2] = b'\x00\xBF'
else:
    print('Function not found @0xB994. Wrong FW version or already patched');sys.exit(1)

if fw[0xBA22:0xBA22+2] == b'\x48\x60':
    fw[0xBA22:0xBA22+2] = b'\x00\xBF'
else:
    print('Function not found @0xBA22. Wrong FW version or already patched');sys.exit(1)

if fw[0xB994:0xB994+2] == b'\x00\xBF' and fw[0xBA22:0xBA22+2] == b'\x00\xBF':
    print('SWD port enabled successfully')

open(sys.argv[1],'wb').write(fw)
