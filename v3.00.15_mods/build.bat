@echo off
@rmdir /q /s temp 2>NUL
@mkdir temp

@echo Extracting Firmware...
python qsfirm.py unpack K6_V3.00.15.bin temp\fw.dec.bin temp\fw.ver.bin

:: comment or uncomment the mods you want to apply. With the word REM at the beginning of each line deaktivates mods.

python mod_custom_freq_ranges.py temp\fw.dec.bin
python mod_remove_tx_limits.py   temp\fw.dec.bin
python mod_universal_version.py  temp\fw.ver.bin
python mod_battery_icon.py       temp\fw.dec.bin
python mod_increases_abr_values.py temp\fw.dec.bin
python mod_custom_steps.py       temp\fw.dec.bin

:: end of mods

@echo Repacking Firmware binary ready to flash...
python qsfirm.py pack temp\fw.dec.bin temp\fw.ver.bin K6_V3.00.15-MODDED.bin

cmd /k