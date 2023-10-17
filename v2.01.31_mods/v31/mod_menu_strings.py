# choose the replacement strings for all of the menu options
# each entry follows the pattern of {address, name, size, string}, where string is what you want to edit and size is the maximum characters allowed

strings = [
    # menu strings
    (0xDD21+7*0 , 'squelch'                         , 6, 'SQL'   ),
    (0xDD21+7*1 , 'step'                            , 6, 'Step'  ),
    (0xDD21+7*2 , 'txpower'                         , 6, 'Power' ),
    (0xDD21+7*3 , 'r dcs'                           , 6, 'DCS Rx'),
    (0xDD21+7*4 , 'r ctcs'                          , 6, 'CTC Rx'),
    (0xDD21+7*5 , 't dcs'                           , 6, 'DCS Tx'),
    (0xDD21+7*6 , 't ctcs'                          , 6, 'CTC Tx'),
    (0xDD21+7*7 , 'tx shift direction'              , 6, 'Shift' ),
    (0xDD21+7*8 , 'tx shift offset'                 , 6, 'Offset'),
    (0xDD21+7*9 , 'wide/narrow'                     , 6, 'Width' ),
    (0xDD21+7*10, 'scramble'                        , 6, 'SCRAMB'),
    (0xDD21+7*11, 'busy channel ptt lock'           , 6, 'BsyLoc'  ),
    (0xDD21+7*12, 'save channel'                    , 6, 'Store' ),
    (0xDD21+7*13, 'battery saver'                   , 6, 'PwSave'),
    (0xDD21+7*14, 'voice activated mode'            , 6, 'Vox'   ),
    (0xDD21+7*15, 'backlight timeout'               , 6, 'Light' ),
    (0xDD21+7*16, 'dual watch - has prio on split'  , 6, 'DW Sby'),
    (0xDD21+7*17, 'TX on selected, RX on other'     , 6, 'Split' ),
    (0xDD21+7*18, 'key beep'                        , 6, 'Beep'  ),
    (0xDD21+7*19, 'tx timeout'                      , 6, 'TOT'   ),
    (0xDD21+7*20, 'voice prompt'                    , 6, 'Speak' ),
    (0xDD21+7*21, 'scan mode'                       , 6, 'Scan'  ),
    (0xDD21+7*22, 'channel display mode'            , 6, 'Disp'  ),
    (0xDD21+7*23, 'auto keypad lock'                , 6, 'KbLock'),
    (0xDD21+7*24, 'ch in scan list 1'               , 6, 'To GS1' ),
    (0xDD21+7*25, 'ch in scan list 2'               , 6, 'To GS2' ),
    (0xDD21+7*26, 'tail noise suppressor'           , 6, 'SQ EOT'),
    (0xDD21+7*27, 'repeater tail noise suppressor'  , 6, 'SQ Rpt'),
    (0xDD21+7*28, 'mic sensitivity'                 , 6, 'Mic'   ),
    (0xDD21+7*29, 'F-9 fast switch channel'         , 6, 'F+9 Ch'),
    (0xDD21+7*30, 'active scan list'                , 6, 'GS Sel'),
    (0xDD21+7*31, 'browse scan list 1'              , 6, 'GS1 {}'),
    (0xDD21+7*32, 'browse scan list 2'              , 6, 'GS2 {}'),
    (0xDD21+7*33, 'alarm mode'                      , 6, 'Panic' ),
    (0xDD21+7*34, 'dtmf radio id'                   , 6, 'DT ID' ),
    (0xDD21+7*35, 'dtmf upcode'                     , 6, 'DT BOT'),
    (0xDD21+7*36, 'dtmf downcode'                   , 6, 'DT EOT'),
    (0xDD21+7*37, 'dtmf key sounds'                 , 6, 'DT Snd'),
    (0xDD21+7*38, 'dtmf answer mode'                , 6, 'DT AA' ),
    (0xDD21+7*39, 'selcall expiry time'             , 6, 'DT Exp'),
    (0xDD21+7*40, 'dtmf preamble time'              , 6, 'DT Pre'),
    (0xDD21+7*41, 'dtmf transmit code on ptt'       , 6, 'AutoDT'),
    (0xDD21+7*42, 'dtmf selective calling system'   , 6, 'SelCal'),
    (0xDD21+7*43, 'dtmf directory'                  , 6, 'PhneBk'),
    (0xDD21+7*44, 'power on screen'                 , 6, 'ONDisp'  ),
    (0xDD21+7*45, 'end of talk tone'                , 6, 'Roger' ),
    (0xDD21+7*46, 'battery voltage'                 , 6, 'Volt'  ),
    (0xDD21+7*47, 'enable AM reception on AM bands' , 6, 'AM Rx' ),
    (0xDD21+7*48, 'enable NOAA background scan'     , 6, 'BG Mon'),
    (0xDD21+7*49, 'delete channel'                  , 6, 'Clear' ),
    (0xDD21+7*50, 'reset radio'                     , 6, 'Reset' ),
    (0xDD21+7*51, 'enable tx on 350mhz band'        , 6, 'F5 Tx' ), # these menu entries are only visible when powering the radio up while holding PTT and side key 1 
    (0xDD21+7*52, 'limit to local ham frequencies'  , 6, 'Region'),
    (0xDD21+7*53, 'enable tx on 200mhz band'        , 6, 'F4 Tx' ),
    (0xDD21+7*54, 'enable tx on 500mhz band'        , 6, 'F7 Tx' ),
    (0xDD21+7*55, 'enable 350mhz band'              , 6, 'F5 En' ),
    (0xDD21+7*56, 'enable scrambler option'         , 6, 'Scramb'),

    # option strings
    (0xDEB0+4*0 , 'battery saver: off'              , 3, 'Off'   ),
    (0xDEB0+4*1 , 'battery saver: 1:1'              , 3, '1/1'   ),
    (0xDEB0+4*2 , 'battery saver: 1:2'              , 3, '1/2'   ),
    (0xDEB0+4*3 , 'battery saver: 1:3'              , 3, '1/3'   ),
    (0xDEB0+4*4 , 'battery saver: 1:4'              , 3, '1/4'   ),
    (0xDEC4+5*0 , 'tx power: low'                   , 4, '1 W'   ),
    (0xDEC4+5*1 , 'tx power: mid'                   , 4, '3 W'   ),
    (0xDEC4+5*2 , 'tx power: high'                  , 4, '5 W'   ),
    (0xDED3+7*0 , 'bandwidth: wide'                 , 6, '25k'   ),
    (0xDED3+7*1 , 'bandwidth: narrow'               , 6, '12,5k' ),
    (0xDEE1+7*0 , 'multiple options 1: off'         , 6, 'Single'),
    (0xDEE1+7*1 , 'multiple options 1: vfo a'       , 6, 'Tx : A'),
    (0xDEE1+7*2 , 'multiple options 1: vfo b'       , 6, 'Tx : B'),
    (0xDEF6+4*0 , 'multiple options 2: off'         , 3, 'No'    ),
    (0xDEF6+4*1 , 'multiple options 2: on'          , 3, 'Yes'   ),
    (0xDEFE+4*0 , 'voice prompt: off'               , 3, '---'   ),
    (0xDEFE+4*1 , 'voice prompt: chinese'           , 3, 'CHN'    ),
    (0xDEFE+4*2 , 'voice prompt: english'           , 3, 'EN'    ),
    (0xDF0A+5*0 , 'dtmf ptt id: off'                , 4, 'None'  ),
    (0xDF0A+5*1 , 'dtmf ptt id: upcode on ptt'      , 4, 'BOT'   ),
    (0xDF0A+5*2 , 'dtmf ptt id: downcode after ptt' , 4, 'EOT'   ),
    (0xDF0A+5*3 , 'dtmf ptt id: both'               , 4, 'Both'  ),
    (0xDF1E+3*0 , 'scan mode: timeout after 5s'     , 2, 'TO'    ),
    (0xDF1E+3*1 , 'scan mode: stay while bearer'    , 2, 'CO'    ),
    (0xDF1E+3*2 , 'scan mode: only seek next'       , 2, 'SE'    ),
    (0xDF27+5*0 , 'channel display mode: freq'      , 4, 'Freq'  ),
    (0xDF27+5*1 , 'channel display mode: chan'      , 4, 'Num'   ),
    (0xDF27+5*2 , 'channel display mode: name'      , 4, 'Name'  ),
    (0xDF36+4*0 , 'tx shift direction: off'         , 3, '---'   ),
    (0xDF36+4*1 , 'tx shift direction: +'           , 3, 'Add'   ),
    (0xDF36+4*2 , 'tx shift direction: -'           , 3, 'Sub'   ),
    (0xDF42+5*0 , 'alarm mode: local'               , 4, 'Buzz'  ),
    (0xDF42+5*1 , 'alarm mode: local + remote'      , 4, 'Xmit'  ),
    (0xDF4C+5*0 , 'power on screen: full'           , 4, 'Logo'  ),
    (0xDF4C+5*1 , 'power on screen: custom message' , 4, 'Text'  ),
    (0xDF4C+5*2 , 'power on screen: batt voltage'   , 4, 'Volt'  ),
    (0xDF5B+4*0 , 'reset: keep channel parameters'  , 3, 'VFO'   ),
    (0xDF5B+4*1 , 'reset: reset everything'         , 3, 'All'   ),
    (0xDF63+6*0 , 'dtmf call autoanswer: nothing'   , 5, 'NOP'   ),
    (0xDF63+6*1 , 'dtmf call autoanswer: ring'      , 5, 'Sound' ),
    (0xDF63+6*2 , 'dtmf call autoanswer: ping back' , 5, 'Echo'  ),
    (0xDF63+6*3 , 'dtmf call autoanswer: ring,ping' , 5, 'Both'  ),
    (0xDF7B+6*0 , 'end of talk tone: off'           , 5, 'Off'   ),
    (0xDF7B+6*1 , 'end of talk tone: classic beep'  , 5, '3Tone' ),
    (0xDF7B+6*2 , 'end of talk tone: MDC1200'       , 5, 'MDC'   ),
    (0xDF8D+4*0 , 'f lock: none'                    , 3, 'WLD'   ),
    (0xDF8D+4*1 , 'f lock: region FCC'              , 3, 'FCC'   ),
    (0xDF8D+4*2 , 'f lock: region Europe'           , 3, 'EUR'   ),
    (0xDF8D+4*3 , 'f lock: region GB'               , 3, 'UK'    ),
    (0xDF8D+4*4 , 'f lock: 430 band'                , 3, '430'   ),
    (0xDF8D+4*5 , 'f lock: 438 band'                , 3, '438'   ),
    (0xDF8D+4*6 , 'selcall: my default number'      , 3, '001'   ),
    (0xDFA9+6*0 , 'selcall: default killcode'       , 5, 'ABD99' ),
    (0xDFA9+6*1 , 'selcall: default revivecode'     , 5, '99DBA' ),
    (0xDFA9+6*2 , 'selcall: default upcode'         , 5, '17' ),
    (0xDFA9+6*3 , 'selcall: default downcode'       , 5, '93' ),
    (0xDFA9+6*4 , 'selcall: suffix for DTMF AA'     , 5, 'AAAAA' ),
    (0xDFC7+3*0 , 'selcall: acknowledge code'       , 2, 'AB' ),

    # misc strings
    (0x8676+0*0 , 'UI: direct entry, C of CH-'      , 1, 'M' ),  ##check, dans ui/helper.c
    (0x867A+0*0 , 'UI: direct entry, H of CH-'      , 1, 'R' ),  ##check, dans ui/helper.c
    (0x867E+0*0 , 'UI: direct entry, - of CH-'      , 1, ' ' ),  ##check, dans ui/helper.c. Utilise pr les espaces
    (0x86B4+0*0 , 'UI: disp channel (wfm)'          , 7, 'M:%02d' ),  ##check, dans ui/helper.c
    (0x8B10+0*0 , 'fm: best stations mem'           ,10, 'BSM [%d]' ),
    (0x8B1C+0*0 , 'fm: save memory'                 , 5, 'Save?' ),
    (0x8B24+0*0 , 'fm: erase memory'                , 4, 'Del?' ),
    (0x8B2C+0*0 , 'fm: seeking'                     , 6, 'SEEK' ),
    (0x8B34+0*0 , 'fm: mem display in MR mode'      ,10, 'MEM %02d' ),
    (0x8B44+0*0 , 'fm: manual freq found mem'       ,11, 'TUN [M%02d]' ),
    (0x8B50+0*0 , 'fm: manual freq'                 , 3, 'TUN' ),
    (0x8B5C+0*0 , 'fm: delete memory'               , 7, 'M:%02d' ),
    (0x8CDC+0*0 , 'fast clone: frequency field'     , 9, 'Freq:%.5f' ),
    (0x8CE8+0*0 , 'fast clone: frequency srch'      ,13, 'Freq:(any)' ),
    (0x8CFC+0*0 , 'fast clone: subtone field'       ,10, 'Sub:------' ),
    (0x8D0C+0*0 , 'fast clone: searching'           , 6, 'Chase ' ),   #needs genuine length=4 patch to 6
    (0x8C20+0*0 , 'fast clone: waiting dot'         , 1, '|' ),
    (0x8D48+0*0 , 'fast clone: VFO goto prompt'     , 5, 'Goto?' ),
    (0x8D50+0*0 , 'fast clone: ch saving progress'  , 5, ' To:' ), ##Displays CH-* if memory is busy, else chNum only. needs genuine length=5 patch to 4
    (0x8D60+0*0 , 'fast clone: fail'                ,10, 'Not found' ),
    (0x8D6C+0*0 , 'fast clone: got it'              , 9, 'Decoded!' ),
    (0x9188+0*0 , 'message: unlock1'                ,12, 'Long Press F' ),
    (0x9198+0*0 , 'message: unlock2'                , 9, 'To Unlock' ),
    (0x91C4+0*0 , 'message: callout'                , 8, 'Calling' ),
    (0x91D0+0*0 , 'message: ping back received'     ,13, 'Echo Received' ),
    (0x91E4+0*0 , 'message: incoming call'          , 7, 'Call:%s' ),
    (0x91EC+0*0 , 'message: dtmf sending'           , 7, 'DTMF Tx' ),
    (0x91F4+0*0 , 'message: dtmf acknowledged'      ,13, 'Acknowledged' ),
    (0x9220+8*0 , 'message: busy channel'           , 7, 'BUSY' ),
    (0x9220+8*1 , 'message: low charge level'       , 7, 'BAT LOW' ),
    (0x9220+8*2 , 'message: tx disabled'            , 7, 'BARRED!' ),
    (0x9220+8*3 , 'message: TOT reached'            , 7, 'TIMEOUT' ),
    (0x9220+8*4 , 'message: panic button pressed'   , 7, 'PANIC' ),
    (0x9220+8*5 , 'message: Vcc exceeded'           , 8, 'CHK VOLT' ),
    (0x98E8+0*0 , 'spacing: step unit'              , 3, 'kHz' ),
    (0x98FA+0*0 , 'dtmf hold time: length'          , 6, '00 ms' ),
    (0x995A+0*0 , 'dtmf preamble time: length'      , 5, '00 ms' ),
    (0x9998+0*0 , 'list: empty or empty record'     , 5, '----'  ),
    (0x99A4+0*0 , 'scan list naming'                , 6, 'GS%d'  ),
    (0x99C0+0*0 , 'confirmation screen: wait'       , 5, 'Wait!' ),
    (0x99C8+0*0 , 'confirmation screen: sure'       , 5, 'SURE?' ),
    (0x9BA0+0*0 , 'message: password request'       , 4, 'CODE'  ),
    (0x9C64+0*0 , 'startup screen: voltage'         , 7, 'Voltage' ),
]


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys

print('* Running', os.path.basename(sys.argv[0]), 'mod...')
fw = bytearray(open(sys.argv[1], 'rb').read())

for address, description, size, string in strings:
    if (fw[address:address+size].decode('ascii').rstrip('\x00') != string.rstrip('\x00')): # only patch strings that are different from the original firmware
        print('Changing string: ', description,', aka', fw[address:address+size].decode('ascii'), '>', string)
        if(len(string) > size):
            raise ValueError(f"String '{string}' is longer than allowed size {size}")
        fw[address:address+size] = string.ljust(size, '\x00').encode()

# Decale 6 au lieu de 4 pour "Wait...." du fast_clone
fw[0x8C28:0x8C28+2] = b'\xB8\x1D'

# Shift a gauche de la valeur apres "SAVE:" du fast_clone (si modif length)
fw[0x8C94:0x8C94+2] = b'\x38\x1D'

open(sys.argv[1], 'wb').write(fw)
