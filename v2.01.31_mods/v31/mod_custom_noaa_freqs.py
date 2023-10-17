#Change below frequencies to new ones, values are in Hz. Keep in mind that deviation is forced to WIDE!

#stock values
#new_noaa_table = [162_550_000, 162_400_000, 162_475_000, 162_425_000, 162_450_000, 162_500_000, 162_525_000, 161_525_000, 161_775_000, 163_275_000 ]

#first PMR446 channels (warning Narrow required!)
new_noaa_table = [446_006_250, 446_018_750, 446_031_250, 446_043_750, 446_056_250, 446_068_750, 446_081_250, 446_093_750, 446_106_250, 446_118_750 ]

#first 1-7 GMRS channels and 22-20 GMRS call/repeater channels
#new_noaa_table = [462_562_500, 462_587_500, 462_612_500, 462_637_500, 462_662_500, 462_687_500, 462_712_500, 462_725_000, 462_700_000, 462_675_000 ]

#freeNet 6 analogue channels (warning Narrow required!)
#new_noaa_table = [149_025_000, 149_037_500, 149_050_000, 149_087_500, 149_100_000, 149_112_500, 000_000_500, 000_000_000, 000_000_000, 000_000_000 ]

#test 7 GMRS + call channel GMRS20 (fail: les zeros restent. La saisie 1 <= X <= 10 est dans main.c)
#new_noaa_table = [462_562_500, 462_587_500, 462_612_500, 462_637_500, 462_662_500, 462_687_500, 462_712_500, 462_725_000, 000_000_000, 000_000_000 ]

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if len(new_noaa_table)!=10: print('Invalid number of entries! Exiting'); sys.exit(1)

current_noaa = struct.unpack_from('<10I', fw, offset=0xE180) ; print('Old NOAA freqs:', [f'{i*10} Hz' for i in current_noaa])
fw[0xE180:0xE180+(4*10)] = bytearray(struct.pack('<10I', *[i//10 for i in new_noaa_table]))
current_noaa = struct.unpack_from('<10I', fw, offset=0xE180) ; print('New NOAA freqs:', [f'{i*10} Hz' for i in current_noaa])

open(sys.argv[1],'wb').write(fw)
