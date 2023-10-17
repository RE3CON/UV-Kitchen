# Changes the PTT+F2 and long-F1 tones, used to open HAM Repeaters and NOAA Channels. The default is 1750 Hz. To open NOAA Tone Squelch set 1050 Hz.
# Other not so common repeater tone pulse freq are 1000Hz, 1450Hz, 1750Hz, 2100Hz

toneptt = int(1750) # change to any frequency in Hz
toneside = int(1050)


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x2A3C] == 0xd6 and fw[0x2A3D] == 0x06 :
    print('Changing by-PTT+F2 tone burst frequency to',toneptt,'Hz')
    fw[0x2A3C:0x2A3C+4] = struct.pack('<I',toneptt)
    print('Changing by-longF1 alternate tone burst frequency to',toneside,'Hz')
    fw[0x7BDC:0x7BDC+4] = struct.pack('<I',toneside)
    ##fw[0x7B22:0x7B22+6] = b'\x12\xD0\x03\x28\x12\xD0' #inverts PTT check for side F2
    
else:
    print('ERROR: Cant find function');sys.exit(1)


open(sys.argv[1],'wb').write(fw)

