##Change RSSI meter behaviour - 7 possible step bars - a maths linear approach
##VHF: @14B2 origin offset, @14B4 slope, @14B6 s=0 limit. UHF: @14CE origin offset, @14D0 slope, @14D2 s=0 limit.
##NEED to change Symbols font: 7 bars+eliminate antenna icon
#Some spare bytes are used to make visible flash alert when ringing

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x855E:0x855E+8] == b'\x43\xD0\x05\x22\x26\x49\x20\x46':
    print('Modding RSSI display routine...')
    fw[0x855E:0x855E+46] = b'\x11\xD0\x26\x49\x03\x22\x6A\x43\x20\x46\xF7\xF7\x1A\xFE\x00\x20\x23\x46\x00\x90\x17\x22\x31\x46\x00\x20\x03\xF0\x54\xF8\xF8\xBD\x03\x26\x1F\x4C\xE7\xE7\x01\x20\x00\x23\x00\x90\xF2\xE7'

    fw[0x8542:0x8542+1] = b'\x1B'
    fw[0x854A:0x854A+1] = b'\x17'
    fw[0x854E:0x854E+1] = b'\x16'
    ##fw[0x14B2:0x14B2+32] = b'\x00\x23\x00\x24\x1A\x33\x98\x42\x03\xD3\x01\x34\x09\x2C\x04\xD0\xF8\xE7\x02\x2C\x01\xD2\x00\x20\x06\xE0\x02\x3C\x20\x1C\x03\xE0'
    ##fw[0x14B2+32:0x14DA] = b'\x00'*8     #Freed bytes to 00
    ##fw[0x14B2:0x14B2+26] = b'\x00\x24\x5C\x28\x07\xD3\x43\x38\x00\x23\x19\x33\x98\x42\x02\xD3\x01\x34\x07\x2C\xF9\xD3\x20\x1C\x05\xE0'     #better formula
    ##fw[0x14B2+26:0x14DA] = b'\x00'*14     #Freed bytes to 00
    #FINAL routine with 2 customisable linear functions
    fw[0x14AC:0x14AC+46] = b'\x00\x24\x03\x29\x0D\xD2\x43\x21\x19\x22\x5C\x28\x07\xD3\x40\x1A\x00\x23\x9B\x18\x98\x42\x02\xD3\x01\x34\x07\x2C\xF9\xD3\x20\x00\x05\xE0\x64\x21\x0A\x22\x6E\x28\xF9\xD3\xF0\xE7\x00\x00'
    # fw[0x14B6:0x14B6+2] = b'\x07\x20'  #Step 7 of calibrated RSSI, OLD stuff
    # fw[0x14C0:0x14C0+2] = b'\x05\x20'  #Step 5 of calibrated RSSI, OLD stuff
    # fw[0x14CA:0x14CA+2] = b'\x03\x20'  #Step 3 of calibrated RSSI, OLD stuff
    print('RSSI/screen refresh routines gaps creating...')
    ## New patch, let alarm to blink alerting LED
    fw[0x1152:0x1152+18] = b'\x0F\x48\x00\x24\x04\x70\x18\x38\x04\x70\x04\x21\x0D\x48\x0A\xF0\x54\xFF'   #alarm off > blinking off: make room
    fw[0x118A:0x118A+14] = b'\x07\xF0\x11\xFA\x10\xBD\x83\x03\x00\x20\x00\x10\x06\x40'		#alarm off, now set blinking off
    fw[0x56E8:0x56E8+48] = b'\x00\xB5\x01\x28\x03\xD0\x02\xF0\x5B\xFF\x01\x20\x00\xE0\x03\x20\x06\x49\x08\x70\x9F\x31\x00\x20\x08\x80\x3C\x39\x08\x70\x4D\x39\x08\x70\x07\x31\x01\x20\x08\x70\x00\xBD\x00\x00\x83\x03\x00\x20'
    fw[0x853C:0x853C+1] = b'\x13'
    fw[0x8544:0x8544+1] = b'\x12'
    fw[0x8550:0x8550+1] = b'\x10'
    fw[0x8560:0x8560+1] = b'\x0D'
    fw[0x8580:0x8580+1] = b'\x06'
    fw[0x858C:0x858C+20] = b'\xD8\x03\x00\x20\xD9\x03\x00\x20\x04\x0A\x00\x20\xBC\xD3\x00\x00\x04\x08\x00\x20'
    fw[0x92F4:0x92F4+14] = b'\x66\x49\x03\x22\x17\x39\x72\x43\x20\x46\xf6\xf7\x4F\xff'    #in disp refresh routine
    fw[0x92F4+14:0x9366] = b'\x00'*100    #Freed bytes to 00
    print('Adding flash alert when ringing...')
    ##fw[0x23FE:0x23FE+1] = b'\x0B'        #minimal DT Expiry timeout in menu
    fw[0x26B0:0x26B0+4] = b'\x05\xF0\x7E\xFF'        #cutting flash alert when ptt
    fw[0x4C60:0x4C60+2] = b'\x21\xD0'                #because dont need check if auto_reset_time=0
    fw[0x4C9E:0x4C9E+8] = b'\x3D\x4A\x11\x78\x03\xF0\x7D\xFC'       #redir to function
    fw[0x81D4:0x81D4+1] = b'\x20'        #time *500ms to ring (no more need to be less than DT_Exp.)
    fw[0x85A0:0x85A0+52] = b'\x00\x29\x05\xD0\x00\x28\x03\xD0\x07\x49\x02\x20\x08\x70\x70\x47\x05\x48\x00\x21\x01\x70\x05\x48\x01\x70\x05\x4A\x10\x68\x08\x21\x88\x43\x10\x60\x01\x20\x70\x47\xB3\x03\x00\x20\xC1\x03\x00\x20\x00\x10\x06\x40'
    fw[0x85A0+52:0x8604] = b'\x00'*48    #Freed bytes to 00

else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
