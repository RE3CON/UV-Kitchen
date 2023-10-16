#This script can be used to change the threshold frequencies for VHF/UHF switch of the RF path and output amplifier bias.
#Factory setting is 280 MHz for both of them.
#In my unit, changing the RF path cutoff frequency to 250 MHz produces a dramatic improvement in sensitivity and power, in the 250-280 MHz band.

# change below sets to new ones, values are in Hz
rf_path_threshold = 250_000_000
power_amplifier_gain_threshold = 280_000_000

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

print('Old RF path threshold frequency:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1EA8)[0]*10))
print('Old Power Amplifier gain threshold frequency: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0xAB6C)[0]*10))

fw[0x1EA8:0x1EA8+4] = struct.pack('<I',rf_path_threshold//10) 
fw[0xAB6C:0xAB6C+4] = struct.pack('<I',power_amplifier_gain_threshold//10)

print('New RF path threshold frequency:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1EA8)[0]*10))
print('New Power Amplifier gain threshold frequency: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0xAB6C)[0]*10))

open(sys.argv[1],'wb').write(fw)
