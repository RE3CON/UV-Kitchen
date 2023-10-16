##--------------------- instant on ----------------------------------------------------------------------------
## No long waiting anymore at boot up of ht
# LARSEN: la fonction est differente sur v31, d'ailleurs pas de bootscreen.. (FC F7 A7 FC). Fait: patch B9 > B7...

##--------------------- no warranty by DO7OO ------------------------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xD25A:0xD25A+4] == b'\xFC\xF7\xA7\xFC':
    print('Set branch to jump over bootup screen')
    fw[0xD25A:0xD25A+12] = b'\x00\xBF\x00\xBF\xF8\xF7\xB7\xFB\x00\xF0\x02\xF8'
else:
    print('ERROR: Cant find branch to bootscreen')
    sys.exit(1)

open(sys.argv[1],'wb').write(fw)
