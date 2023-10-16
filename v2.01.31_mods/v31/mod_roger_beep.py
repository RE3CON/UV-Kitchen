## Opens 3 possible customisable tones for roger beep
## Courtesy of LarSeN
# You can change duration and/or frequency for each tone used. Put 0 in correct duration if single ou dual beep is preferred.

#MotoTrBo
##tone1 = 1540
##tone2 = 1310
##lt1 = 150
##lt2 = 80

#Tones frequencies (Hz)
tone1 = 880
tone2 = 660
tone3 = 1200
#Tones durations (ms. Max=255 ms. End roger beep if 0)
lt1 = 110
lt2 = 70
lt3 = 140

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if lt1 == lt2 or lt1 == lt3 or lt2 == lt3: print('ERROR: Please choose different lt1/2/3 values to prevent issues!');sys.exit(1)
if fw[0xAF40:0xAF40+4] == struct.pack('<I',0x142A) and fw[0xAF44:0xAF44+4] == struct.pack('<I',0x1C3B):
    print('Changing roger Tone1:',tone1,'Hz',lt1,'ms , Tone2:',tone2,'Hz',lt2,'ms , Tone3:',tone3,'Hz',lt3,'ms...')
    fw[0x6FCE:0x6FCE+3] = b'\x00\x28\x07'      #lolpatches to make room, as we only miss 2 bytes
    fw[0x6FD6:0x6FD6+2] = b'\x00\x20'
    ##fw[0xAEDC:0xAEDC+112] = b'\x01\xF0\x1A\xF9\x00\x20\xFF\xF7\x69\xFA\x07\x21\x49\x03\x70\x20\x00\xF0\x40\xF8\xFF\xF7\x38\xFF\x32\x20\x02\xF0\x33\xF9\x10\x49\x8C\x24\x04\xE0\x0F\x49\x46\x24\x01\xE0\x0F\x49\x5A\x24\x00\x2C\x0D\xD0\x71\x20\x00\xF0\x2E\xF8\x01\xF0\x0C\xF9\x20\x46\x02\xF0\x21\xF9\x01\xF0\xF9\xF8\x8C\x2C\xEC\xD0\x46\x2C\xED\xD0\x00\x21\x70\x20\x00\xF0\x1F\xF8\x05\x49\x30\x20\x00\xF0\x1B\xF8\x70\x47\x7D\x23\x00\x00\x9E\x1A\x00\x00\x65\x30\x00\x00\xFE\xC1\x00\x00'
    fw[0xAEDC:0xAEDC+112] = b'\x00\xB5\xFF\xF7\x6A\xFA\x01\xF0\x17\xF9\x07\x21\x49\x03\x70\x20\x00\xF0\x40\xF8\xFF\xF7\x38\xFF\x32\x20\x02\xF0\x33\xF9\x10\x49\x6E\x24\x04\xE0\x0F\x49\x46\x24\x01\xE0\x0F\x49\x8C\x24\x00\x2C\x0D\xD0\x71\x20\x00\xF0\x2E\xF8\x01\xF0\x0C\xF9\x20\x46\x02\xF0\x21\xF9\x01\xF0\xF9\xF8\x6E\x2C\xEC\xD0\x46\x2C\xED\xD0\x00\x21\x70\x20\x00\xF0\x1F\xF8\x05\x49\x30\x20\x00\xF0\x1B\xF8\x00\xBD\x7D\x23\x00\x00\x9E\x1A\x00\x00\x65\x30\x00\x00\xFE\xC1\x00\x00'
    fw[0xAF3C:0xAF3C+4] = struct.pack('<I',int(tone1 * 10.32444))
    fw[0xAF40:0xAF40+4] = struct.pack('<I',int(tone2 * 10.32444))
    fw[0xAF44:0xAF44+4] = struct.pack('<I',int(tone3 * 10.32444))
    fw[0xAEFC] = lt1
    fw[0xAF22] = lt1
    fw[0xAF02] = lt2
    fw[0xAF26] = lt2
    fw[0xAF08] = lt3
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)

