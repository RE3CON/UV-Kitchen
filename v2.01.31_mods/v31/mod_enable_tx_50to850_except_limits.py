#Set below frequency range to be TX blocked
block_freq_lo = 24_890_000
block_freq_hi = 136_999_900

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

shellcode = b'\xF0\xB5\x01\x46\x49\x69\x09\x68\x05\x4A\x91\x42\x05\xD3\x05\x4A\x91\x42\x02\xD2\x00\x20\xC0\x43\x01\xE0\x00\x20\xFF\xE7\xF0\xBD'+bytearray(struct.pack('<II', block_freq_lo//10, block_freq_hi//10))
fw[0x182C:0x182C+len(shellcode)] = shellcode

if len(fw)<0xEFFF:
    print('TX range',block_freq_lo,'Hz to',block_freq_hi,'Hz blocked successfully')
    open(sys.argv[1],'wb').write(fw)
else:
    print('Error: Firmware file got too big!')
