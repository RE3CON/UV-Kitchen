# Custom MDC data. Sent if MDC1200 roger beep is chosen
# Courtesy of LarSeN

#genuine values
##mdc_data = bytearray.fromhex("F1A2744661A465444E8AE044EA84")

#PTTID 0001
# 0xBC, 0x26, 0x4C, 0xC0, 0xFA, 0x33, 0xE4, 0xD1, 0xF0, 0xF7, 0x7C, 0x27, 0xF9, 0x06
mdc_data = bytearray.fromhex("26BCC04C33FAD1E4F7F0277C06F9")

##Motorola sync. sync_bytes[0,1] et [2,3] sont tous deux @AEAC..il ajoute 0x55 au 2e pour faire 55AA
patchcode = bytearray.fromhex("15495B2000F091F818495C2000F08DF8002407E06000154A115A5F2000F085F8601CC4B2072CF5DB142002F076F91049592000F07AF8B42002F06FF96821592000F073F80021702000F06FF80021582000F06BF810BD")
sync1 = b'\x09\x07'
sync2 = b'\x44\x2A'
sync3 = b'\x30\x6F'  #swap 0x30 with 0x70 to include CRC

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct,array

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if len(mdc_data)!=14: print('Do not change number of entries! Exiting'); sys.exit(1)

cur_mdc_data = struct.unpack_from('<7H', fw, offset=0xD358) ; print('Old MDC EOT data:', '[{}]'.format(','.join(hex(x) for x in cur_mdc_data)))

if fw[0xD358:0xD358+7] == b'\xA2\xF1\x46\x74\xA4\x61\x44':
    mdc_datale=array.array('H', mdc_data)
    mdc_datale.byteswap()
    fw[0xD358:0xD358+14]=mdc_datale
    print('MDC EOT data found, updated OK')
    fw[0xAE46:0xAE46+86]=patchcode
##    fw[0xAEA0:0xAEA0+2]=b'\xF3\x37'   #choose AA pattern for preamble. genuine: pattern depends on Syncbyte 0's MSB
    fw[0xAE9C:0xAE9C+2]=sync2
    fw[0xAEAC:0xAEAC+2]=sync1
    fw[0xAEB0:0xAEB0+2]=sync3
else:
    print('Error: original MDC data doesnt match default values!');sys.exit(1)

cur_mdc_data = struct.unpack_from('<7H', fw, offset=0xD358) ; print('New MDC EOT data:', '[{}]'.format(','.join(hex(x) for x in cur_mdc_data)))
open(sys.argv[1],'wb').write(fw)
