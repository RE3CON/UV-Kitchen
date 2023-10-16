# Custom CTCSS (PL). Genuine (ordered) PL numbers dont comply with legacy 38 codes/UHF CB.
# Courtesy of LarSeN

#genuine values
##new_ctcss_freqs =   ['67.0', '69.3', '71.9', '74.4', '77.0', '79.7', '82.5', '85.4', '88.5', '91.5', '94.8', '97.4', '100.0', '103.5', '107.2', '110.9', '114.8', '118.8', '123.0', '127.3', '131.8', '136.5', '141.3', '146.2', '151.4', '156.7', '159.8', '162.2', '165.5', '167.9', '171.3', '173.8', '177.3', '179.9', '183.5', '186.2', '189.9', '192.8', '196.6', '199.5', '203.5', '206.5', '210.7', '218.1', '225.7', '229.1', '233.6', '241.8', '250.3', '254.1']
##new_ctcss_freqs =     ['67.0', '71.9', '74.4', '77.0', '79.7', '82.5', '85.4', '88.5', '91.5', '94.8', '97.4', '100.0', '103.5', '107.2', '110.9', '114.8', '118.8', '123.0', '127.3', '131.8', '136.5', '141.3', '146.2', '151.4', '156.7', '162.2', '167.9', '173.8', '179.9', '186.2', '192.8', '203.5', '210.7', '218.1', '225.7', '233.6', '241.8', '250.3', '69.4', '159.8', '165.5', '171.3', '177.3', '183.5', '189.9', '196.6', '199.5', '206.5', '229.1', '254.1']

#Change values below (10*n Hz!)
#genuine values
##new_ctcss_freqs = [670, 693, 719, 744, 770, 797, 825, 854, 885, 915, 948, 974, 1000, 1035, 1072, 1109, 1148, 1188, 1230, 1273, 1318, 1365, 1413, 1462, 1514, 1567, 1598, 1622, 1655, 1679, 1713, 1738, 1773, 1799, 1835, 1862, 1899, 1928, 1966, 1995, 2035, 2065, 2107, 2181, 2257, 2291, 2336, 2418, 2503, 2541]

#Legacy assignment / UHF CB
new_ctcss_freqs = [670, 719, 744, 770, 797, 825, 854, 885, 915, 948, 974, 1000, 1035, 1072, 1109, 1148, 1188, 1230, 1273, 1318, 1365, 1413, 1462, 1514, 1567, 1622, 1679, 1738, 1799, 1862, 1928, 2035, 2107, 2181, 2257, 2336, 2418, 2503, 694, 1598, 1655, 1713, 1773, 1835, 1899, 1966, 1995, 2065, 2291, 2541]

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if len(new_ctcss_freqs)!=50: print('Do not change number of entries! Exiting'); sys.exit(1)

##current_ctcss = struct.unpack_from('<50H', fw, offset=0xDFCA) ; print('Old CTCSS table:', [f'{i/10} Hz' for i in current_ctcss])

if fw[0xDFCA:0xDFCA+(2*7)] == bytearray(struct.pack('<7H', *[670, 693, 719, 744, 770, 797, 825])):
    fw[0xDFCA:0xDFCA+(2*50)] = bytearray(struct.pack('<50H', *[i for i in new_ctcss_freqs]))
    print('CTCSS table found, updated OK')
else:
    print('Error: original CTCSS freq table doesnt match default values!');sys.exit(1)

current_ctcss = struct.unpack_from('<50H', fw, offset=0xDFCA) ; print('New CTCSS table:', [f'{i/10} Hz' for i in current_ctcss])
open(sys.argv[1],'wb').write(fw)
