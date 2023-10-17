echo off
py batt_calibrator.py COM8 read
pause
py batt_calibrator.py COM8 calibrate
pause
echo off
rem To calibrate ADC so battery voltage display more accurately run cmd: py batt_calibrator.py COM8 calibrate
rem "************************************************************************"
rem "**       Enter voltage from multimeter and press enter:               **"
rem "**  follow steps:                                                     **"
rem "**  1. - connect radio to PC                                          **"
rem "**  2. - power on radio                                               **"
rem "**  3. - lay your radio with display to the bottom and battery up     **"
rem "**  4. - measure voltage on two exposed pad on bottom of the battery  **"
rem "**  5. - wait till voltage stabilizes                                 **"
rem "**  6. - write measured voltage in format `1.23` or `1,23`            **"
rem "**  7. - hit enter                                                    **"
rem "**  8. - reboot the radio by power off and on                         **"
rem "************************************************************************"
rem "*Backup the current calibration values: py batt_calibrator.py COM8 read*"
rem "************************************************************************"
rem OPTION ARGUMENTS:
rem batt_calibrator.py <COMx> <read | write  val0 val1 val2 val3 val4 val5 | calibrate>
rem "************** The Serial Module must be installed into Python!!! *****************"
rem Install on command prompt the serial module run: py -m pip install serial
rem 
rem to install pyserial module py -m pip install --upgrade pyserial-3.5b0-py2.py3-none-any.whl
rem 
echo off
rem finished
cmd /k