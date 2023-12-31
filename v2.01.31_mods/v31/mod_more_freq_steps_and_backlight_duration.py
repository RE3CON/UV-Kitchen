## ATTENTION: Non test sur v31!
# Please note that the number of freq steps and the maximum backlight duration are linked to the same constant in the firmware (probably because of compiler optimization)
# Change below steps to new ones, values are in Hz

new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330, 500000, 10, 1250, 20000]

# the stock firmware limits backlight duration to 5 seconds max. this mod allows to change the maximum limit. 
# the ABR duration can then be changed on the radio using the normal menu, and it will be persistent after reboot
# however, the PC CPS software can only read and write a maximum of 5 for ABR and will simply limit the value back to 5

abr_limit = 5

# keep in mind that a backlight duration higher than (number of freq steps - 1) will add additional empty freq steps
# this bug can only be resolved by reverse engineering and splitting the menu functions.

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

new_freq_array_offset = bytearray(struct.pack('<I',len(fw)))
new_freq_len = len(new_freq_steps)
new_freq_array = bytearray(struct.pack('<'+'H'*new_freq_len, *[i//10 for i in new_freq_steps]))

#append new array to FW
fw += new_freq_array

#replace references
fw[0x62FC:0x62FC+4] = new_freq_array_offset
fw[0x98DC:0x98DC+4] = new_freq_array_offset

#replace table sizes
fw[0x610A] = new_freq_len
fw[0x23C6] = new_freq_len-1
fw[0x23C0] = new_freq_len-1

#patch backlight duration
if(abr_limit < new_freq_len-1):
    print('abr_limit is too small and was automatically increased to allow additional freq steps to work')
else:
    print('Patching backlight duration...')
    fw[0x23C0] = abr_limit

#patch abr boundary check in config loader so backlight setting >5 stays persistent in eeprom
if(fw[0x6400:0x6400+2] == b'\x05\x20'):
    print('Found boundary check. Patching...')
    fw[0x6400:0x6400+2] = b'\x00\xBF' # NOP instruction instead of MOVS

open(sys.argv[1],'wb').write(fw)
