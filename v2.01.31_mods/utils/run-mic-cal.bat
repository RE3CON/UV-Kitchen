@ECHO ON
@ECHO The default values are: 3 8 14 19 24
@ECHO To read the Mic sensity enties of the 5 Levels run cmd: py mic_calibrator.py COM8 read
@ECHO To calibrate Mic sensity enties in 5 Levels run cmd: py mic_calibrator.py COM8 write 6 14 20 25 31
@ECHO This are the active values:
@echo off
py mic_calibrator.py COM8 read
@ECHO It will be changed now to: 11 16 21 26 31
echo off
py mic_calibrator.py COM8 write 11 16 21 26 31
rem ************************************************************************
rem **  Instruction steps:                                                **
rem **  1. - connect radio to PC                                          **
rem **  2. - power on radio                                               **
rem **  3. - read the value (3 - 31) for each level (0 to 4)              **
rem **  4. - write the 5 values for each level `3` to max `31` in a line  **
rem **  5. - example cmd: py mic_calibrator.py COM8 write 11 16 21 26 31  **
rem **  6. - hit enter                                                    **
rem **  7. - reboot the radio by power off and on                         **
rem ************************************************************************
rem *Backup the current calibration values: py mic_calibrator.py COM8 read *
rem ************************************************************************
rem OPTION ARGUMENTS:
rem read and write the values from '3' to '31' for all 5 Levels (lev0, 1, 2, 3, 4)
rem the default values are:
rem for lev0:'3' lev1:'8' lev2:'14' lev3:'19' lev4:'24'
rem mic_calibrator.py <COMx> <read | write 3 8 14 19 24>
rem ************** The Serial Module must be installed into Python!!! *****************
rem Install on command prompt the serial module run: py -m pip install serial
rem to install pyserial module py -m pip install --upgrade pyserial-3.5b0-py2.py3-none-any.whl
@ECHO !!! THE RADIO WILL NOW REBOOT TO ACTIVATE THE CHANGES !!!
py reboot_radio.py COM8
cmd /k