#Mic gain (changed derpy "OR 1111" which had no sense. Mic levels calibration is in EEPROM, check mic_calibrator.py)

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xA954:0xA954+4] == b'\x40\xe9\x00\x00' and fw[0x1D04:0x1D04+4] == b'\x40\xe9\x00\x00':
    print('Patching QS mic gain bug...')
    fw[0x5F1A:0x5F1A+2] = b'\x10\x20'           #QS Bug fix: Si Mic>31 Mic=16 et non 15. Cas d'un HT encore non-calibre, valeur=255.
    #fw[0xA954:0xA954+4] = b'\x5F\xe9\x00\x00'   #init: Always maxxed
    #fw[0x1D04:0x1D04+4] = b'\x5F\xe9\x00\x00'   #Always maxxed whatever setting
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
