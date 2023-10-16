##Disables 1050 Hz tone detection for NOAA SQ opening
##Courtesy of LarSeN
#Appel a FUNCTION_Init(void) en @1CD2 (sub_696C)
#  MOVS R1, #1  >  #0 : @697C: 00 21 , sinon il attend un CTCSS a 1050Hz
#BUG QS: Si VIS actif en DW, ca le laisse en RX..
#_Cause: Le test en @1C3E n'est fait que si IS_NOAA_CHANNEL=0
#_Patch: @1BFA 3D E0 > 20 E0 (goto test @1C3E avant retour @1C78)

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xAB20:0xAB20+2] == b'\x4A\x94':
    print('Disabling 1050 Hz tone for NOAA SQ opening...')
    fw[0xAB20:0xAB20+2] = b'\x4A\x10'   #REG_51 disable CTC1 1050hz tone squelch
    fw[0x1BF8:0x1BF8+2] = b'\x4C\x4D'   #INT: sqfound + sqlost + 55HzTail
#    fw[0x1BF8:0x1BF8+2] = b'\x0C\x25'   #INT: sqfound + sqlost (NO ctcss)
    fw[0x1BFA:0x1BFA+2] = b'\x20\xE0'   #derpy QS bugfix
    fw[0x697C:0x697C+2] = b'\x00\x21'   #si NOAA : code_type=OFF a la place de Continuous_tone
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
