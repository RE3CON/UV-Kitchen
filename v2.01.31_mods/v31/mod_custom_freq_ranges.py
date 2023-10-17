#Change values below (Hz)
new_freq_low_limit =   [18_000_000,  76_000_000, 136_000_000, 174_000_000, 350_000_000, 400_000_000,  470_000_000]
new_freq_high_limit =  [75_999_900, 135_999_900, 173_999_900, 349_999_900, 399_999_900, 469_999_900, 1300_000_000]

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if len(new_freq_low_limit)!=7: print('Do not change number of entries! Exiting'); sys.exit(1)
if len(new_freq_high_limit)!=7: print('Do not change number of entries! Exiting'); sys.exit(1)

current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE100) ; print('Old Lofreq ranges:', [f'{i*10} Hz' for i in current_steps])
current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE11C) ; print('Old Hifreq ranges:', [f'{i*10} Hz' for i in current_steps])

if fw[0xE100:0xE100+(4*7)] == bytearray(struct.pack('<IIIIIII', *[5000000, 10800000, 13600000, 17400000, 35000000, 40000000, 47000000])):
    fw[0xE100:0xE100+(4*7)] = bytearray(struct.pack('<IIIIIII', *[i//10 for i in new_freq_low_limit]))
    print('LoFreq table found, updated OK')
else:
    print('Error: original LoFreq table doesnt match default values!');sys.exit(1)

if fw[0xE11C:0xE11C+(4*7)] == bytearray(struct.pack('<IIIIIII', *[7600000, 13599990, 17399990, 34999990, 39999990, 46999990, 60000000])):
    fw[0xE11C:0xE11C+(4*7)] = bytearray(struct.pack('<IIIIIII', *[i//10 for i in new_freq_high_limit]))
    print('HiFreq table found, updated OK')
else:
    print('Error: original HiFreq table doesnt match default values!');sys.exit(1)

current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE100) ; print('New Lofreq ranges:', [f'{i*10} Hz' for i in current_steps])
current_steps = struct.unpack_from('<IIIIIII', fw, offset=0xE11C) ; print('New Hifreq ranges:', [f'{i*10} Hz' for i in current_steps])

open(sys.argv[1],'wb').write(fw)
