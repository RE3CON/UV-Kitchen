# After applying this mod, the FREQ CLONE and CTC/DCS SCAN function ([F]+4, [F]+Scan) will run till given timeout or if user press [Exit] button
# LarSeN: Le bargraph '.' de progression est bloque apres ce mod, c'est dommage. TODO: Modifier le timeout uniquement
# actuel: Timeout 1 minute 0x20 > 0x78
# 0x40 dure 8 bargraphs complets soit 32s

fc_delay = 60 # change to any value <= 127s

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

##if fw[0x4C2C:0x4C2C+2] == b'\x52\x1C':   #Increment NOP'ed = Runs for infinity
##    fw[0x4C2C:0x4C2C+2] = b'\x00\xBF'
##if fw[0x4C34:0x4C34+2] == b'\x07\xD9':   #Unconditional jump = Runs for infinity with bargraph (overflow issue?)
##    fw[0x4C34:0x4C34+2] = b'\x07\xE0'
if fw[0x4C32:0x4C32+2] == b'\x20\x2A':
##    fw[0x4C32:0x4C32+2] = b'\x78\x2A'   #0xFE is absolute MAX here (127s)
      fw[0x4C32] = 2*fc_delay & 0xFE
      print(f'Setting new FC timeout value = {int(fw[0x4C32])//2}')
      print('Scan Freq feature timeout delay successfully maxxed')
else:
    print('Value not found @0x4C32. Maybe wrong FW version or other issue!')
    sys.exit(1)

open(sys.argv[1],'wb').write(fw)
