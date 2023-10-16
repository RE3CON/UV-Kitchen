#Changes WFM frequency range from 76–108 MHz to 64-108MHz
#LarSeN: TODO: Also patch F+key presets to act less derpy. F+1 > F+3 , F+2 > F+4, F+3 > F+0 ( *Scan [0x0E] impossible car pas ds le case de fm.c:FM_ProcessKeys) , 
#Possible candidates @30CE (F1), @30D8 (F2), @30DC (F3), @30E0 (F0)

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

fw[0xA364:0xA364+4] = b"\x5F\x20\xC0\x00"  # MOVS R0, #760    -> MOVS R0, #640 (Offset??)
fw[0xA2E4:0xA2E4+4] = b"\x5F\x15\x00\x00"  # Reg05 = 0x0A5F   -> Reg05 = 0x15DF (DF:64-76, 5F:76-108, 1F:87.5-108, 9F:76-90)
                                           # SEEK_TH[15:8]; BAND[7:6]; SPACE[5:4]; VOLUME[3:0]
                                           # @DO7OO said that you can change rise SEEK_TH from 0x0A to 0x20 to lower sensitivity.
                                           # Value depends on antenna your are using. 

fw[0x64BC:0x64BC+4] = b"\x50\x20\xC0\x00"  # MOVS R0, #760    -> MOVS R0, #640  - FM LOW LIMIT  (50: 64, 5F: 76, 6C: 87, 6E: 88). Le seul qui change sur uvmodRU en 64-108
fw[0x64C0:0x64C0+2] = b"\x87\x22"          # MOVS R2, #0x87   -> MOVS R2, #0x87 - FM HIGH LIMIT (87= 108MHz. 71= 90Mhz, 5F= 76MHz). Valeur=insert 3 bits à droite (shift)

if fw[0x30CE:0x30CE+20] == b'\x01\x2C\x11\x70\x4C\x4A\x11\x70\x06\xD0\x02\x2C\x15\xD0\x03\x2C\x15\xD0\x00\x2C':
    fw[0x30CE:0x30CE+20] = b'\x03\x2C\x11\x70\x4C\x4A\x11\x70\x06\xD0\x04\x2C\x15\xD0\x00\x2C\x15\xD0\x0E\x2C'
print('WFM range successfully changed to 64-108MHz')
open(sys.argv[1],'wb').write(fw)
