@echo off
@rmdir /q /s temp 2>NUL
@mkdir temp

@echo Extracting firmare...
python qsfirm.py unpack k5_v2.01.31_publish.bin temp\fw.dec.bin temp\fw.ver.bin

:: here comment or uncomment mods
:: start of mods
:: mods implying firmware grow
:: please choose only one of them and always 
:: place as first mod in this batch file

rem python mod_custom_bootscreen_narrow.py temp\fw.dec.bin
python mod_more_freq_steps_and_backlight_duration.py temp\fw.dec.bin

REM python mod_051f_ramreader.py 	temp\fw.dec.bin
python mod_2to1_compressor.py 		temp\fw.dec.bin
REM python mod_battery_icon.py 		temp\fw.dec.bin
python mod_change_burst_tones.py 	temp\fw.dec.bin
python mod_change_contrast.py 		temp\fw.dec.bin
python mod_change_freq_scan_timeout.py temp\fw.dec.bin
python mod_change_RF_switch_threshold.py temp\fw.dec.bin
python mod_change_tx_limits.py 		temp\fw.dec.bin
rem python mod_remove_tx_limits.py 	temp\fw.dec.bin
python mod_custom_ctcss_codes.py 	temp\fw.dec.bin

REM python mod_custom_font_VCR.py	temp\fw.dec.bin
REM python mod_custom_font_DO7OO.py	temp\fw.dec.bin
python mod_custom_digits.py 		temp\fw.dec.bin
python mod_custom_font.py 			temp\fw.dec.bin
python mod_custom_mdc_data.py 		temp\fw.dec.bin
python Symbols_encode31.py Symbols_mod.bmp mod_custom_symbols.py
python mod_custom_symbols.py 		temp\fw.dec.bin

python mod_custom_freq_ranges.py 	temp\fw.dec.bin
python mod_custom_noaa_freqs.py 	temp\fw.dec.bin
rem python mod_custom_steps.py 		temp\fw.dec.bin
python mod_disable_1050hz_noaa.py 	temp\fw.dec.bin
REM python mod_disable_tx_completely.py temp\fw.dec.bin
python mod_enable_am_everywhere.py 	temp\fw.dec.bin
python mod_enable_swd_port.py 		temp\fw.dec.bin
REM python mod_enable_tx_50to850.py temp\fw.dec.bin
python mod_enable_tx_50to850_except_limits.py temp\fw.dec.bin
python mod_fm_radio_64-108mhz.py 	temp\fw.dec.bin
REM python mod_fm_radio_88-108mhz.py temp\fw.dec.bin
REM python mod_fm_radio_87-108mhz.py temp\fw.dec.bin
python mod_increase_backlight_timeout.py temp\fw.dec.bin
REM python mod_instant_on.py 		temp\fw.dec.bin
python mod_menu_strings.py 			temp\fw.dec.bin
rem python mod_menu_strings_org.py	temp\fw.dec.bin
python mod_mic_gain.py 				temp\fw.dec.bin
REM python mod_negative_screen.py 	temp\fw.dec.bin
rem python mod_ota_qrg.py 			temp\fw.dec.bin
python mod_roger_beep.py 			temp\fw.dec.bin
python mod_rssibars.py 				temp\fw.dec.bin
python mod_widen_scr_range.py 		temp\fw.dec.bin
python mod_bugspatch.py 			temp\fw.dec.bin
python mod_universal_version.py 	temp\fw.ver.bin

:: end of mods

@echo Repacking firmware...
python qsfirm.py pack temp\fw.dec.bin temp\fw.ver.bin k5_v2.01.31_MODDED.bin

cmd /k