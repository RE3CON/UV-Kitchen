#Allows to increase display backlight timeout by provided multiplicand. Also puts ABR=5 to backlight forever.
#LarSeN: old mod was ovrting R0=R0+1 because of int.. patching by MULS only

#multi=int(64) #old mod:genuine
#multi=int(128) #old mod:(1 is 2sec, 2 is 4sec...etc)
#multi=int(192) #old mod:(1 is 4sec, 2 is 8sec...etc)
#multi=int(256) #old mod:(1 is 8sec, 2 is 16sec...etc)
multi=int(15)  #(=7,5s x ABR)

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x59E6:0x59E6+2] == b'\x40\x00' and multi < 51:
    print('Maxxing backlight timeout values...')
    fw[0x2634:0x2634+2] = b'\x04\xD0'       #because backlight when TX is derp
    fw[0x4A68:0x4A68+6] = (4*multi+1).to_bytes(1,'big')+b'\x29\x06\xD2\x49\x1E'     #qd gBacklightCountdown > 60 : always on (corresp a 30s)
    fw[0x59E6:0x59E6+4] = multi.to_bytes(1,'big')+b'\x24\x60\x43'
    ##fw[0x59E6:0x59E6+4] = struct.pack('<I',multi)    #old mod

else:
    print('ERROR: Cant find function or parametric error');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
