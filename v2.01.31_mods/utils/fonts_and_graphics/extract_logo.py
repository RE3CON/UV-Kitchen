def bmp(rawdata, w, h):
    rawdata = bytes(reversed(rawdata))
    bitdata = b''
    
    if w<16:
        bitdata = b''.join([ bytes([rawdata[i],0,0,0]) for i in range(0,len(rawdata)) ])
    elif w<24:
        for i in range(len(rawdata)//2):
            bitdata += rawdata[i*2:i*2+2]+b'\x00\x00'

    return (b"BM"                  + #signature 2bytes \x42\x4D
            b"\x00\x00\x00\x00"    + #filesize  (ignored by most editors) 
            b"\x00\x00\x00\x00"    + #reserved
            b"\x3E\x00\x00\x00"    + #bfOffBits
            b"\x28\x00\x00\x00"    + #headerszie always 0x28
            bytes([w%0x100,w//0x100,0,0])+ #biWidth
            bytes([h%0x100,h//0x100,0,0])+ #biHeight
            b"\x01\x00"            + #planes always1
            b"\x01\x00"            + #bitcount 1=monochrome
            b"\x00\x00\x00\x00"    + #compression
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\x00\x00\x00\x00"+
            b"\xff\xff\xff\x00"    + #colors[0]
            b"\x00\x00\x00\x00"    + #colors[1]
            bytes(bitdata)
            )

def mem16toBmp(raw_mem,symbol_width):
    bmp_format = b''
    for s in range(0,len(raw_mem)//(symbol_width*2)):
        symb_offset = s*symbol_width*2
        for i in range(0,symbol_width):
            bmp_format += bytes([raw_mem[symb_offset+i],raw_mem[symb_offset+i+symbol_width],])
    return bmp_format


#===============================================================================================


fw = open('fw_logo.bin','rb').read()


#Logo @0xE5F8 length 0x140
with open('logo.bmp','wb') as f:
    data = fw[0xE5F8:0xE5F8+384] # 384 bytes 128x24
##    data = mem16toBmp(fw[0xE5F8:0xE5F8+384],8)
    f.write(bmp(data,8,len(data)))
