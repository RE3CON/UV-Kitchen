## [LarSen's set of 2.01.31 firmware mods](https://github.com/Lar-Sen/Quansheng_UV-K5_Kitchen) for Quansheng UV-K5, UV-K5(8), UV-K6, UV-5R PLUS VHF/UHF Handheld HAM Walkie Talkies.
## Customized enhanced by @RE3CON with [Amnemonic's UVMOD Kitchen 31](https://github.com/amnemonic/Quansheng_UV-K5_Firmware/tree/main/uvmod_kitchen_31) additions and more...

### Prerequisites 
 - Windows XP or higher
 - Python 3.6.8 (at least) installed
 - Kenwood/BaoFeng type serial comm cable (USB or RS-232)

### How to use this?
 - customize included mods, for example `mod_custom_freq_ranges.py` has possibility to edit frequency ranges
 - edit `build31.bat`, if you want omit execution of any mod, prefix its line with `::` or `rem`
 - start a shell in `firmware_mods` directory
 - run command `build31.bat`
 - look for any errors. Don't go further if any: double-check editable values in each of active mods
 - now you can flash new firmware file named `k5_v2.01.31_MODDED.bin`, with genuine `Updater.exe` from Quansheng (latest version provided in /Updater directory)

## ROM patches list
<hr>

### `mod_2to1_compressor.py`
LarSeN contribution: Activates only compressor part of the integrated compander, to get better modulation dynamics.
Auto-disables when VOX set, to preserve accuracy in digital modes.
<hr>

### `mod_battery_icon.py`
Sets a better look for battery icon.

Tip: Best to check my `mod_custom_symbols.py` which entirely replaces all icons by better alternatives. Or you can run this after my mod if you hate hearts :)
<hr>

### `mod_bugspatch.py`
LarSeN contribution: Various ROM patches for Quansheng genuine firmware bugs. Evolutive.
<hr>

### `mod_change_contrast.py`
Allows to change LCD appearance, e.g black pixels get more black.

Customization:  A good value is 35. Beware not to put too high value, as this is suspected to shorten LCD lifespan.

### `mod_change_burst_tones`
LarSeN contribution: Now allows to change PTT+F2 and 'long-press F1' burst tones. Defaults are 1750Hz and 1050Hz.

Replaces mod_change_Tone_1750Hz.py.
<hr>

### `mod_change_freq_scan_timeout.py`
LarSeN contribution: Remove infinite time (useless). Instead, restore activity graph which was stuck in previous version.

After applying this mod, the FREQ CLONE and CTC/DCS SCAN function ([F]+4, [F]+Scan) will run till given timeout or if user press [Exit] button.
<hr>

### `mod_change_RF_switch_threshold.py`
Allows to change the threshold frequencies for VHF/UHF switch of the RF path and output amplifier bias.
Factory setting is 280 MHz for both of them.
Better power and/or sensitivity may be observed in some cases.
<hr>

### `mod_change_tx_limits.py`
Self explanatory. Please be aware that TXing below ~80MHz is known to produce a considerable amount of spurious emissions with this unit.
Smarter use is the wiser mod_enable_tx_50to850_except_limits.py .
<hr>

### `mod_enable_tx_50to850_except_limits.py`
Creates a band block for TX frequencies: an interval where you're not allowed to xmit, even if frequency domain is unlocked.
Please be aware that TXing below ~80MHz is known to produce a considerable amount of spurious emissions with this unit.

Customization: Blocks AIR band by default. You can change it at the beginning of the script.

ℹ️This patch alone doesn't extend available frequency ranges. For this use `mod_custom_freq_ranges.py` mod.
<hr>

### `mod_custom_bootscreen_narrow.py`
LarSeN contribution: Completely reworked the display routine. Now better nested and switchable from main menu (edit line FULL to Logo).

Adds a customisable boot screen, sparing ROM bytes by allowing an offset from top of the screen.

Customization: before drawing logo, screen buffer is filled with value defined in `clean_pattern` variable. Have a look at utils/fonts_and_graphics/Clearing_patterns.bmp
To make your own logo, get a 128x64 (max) BMP or PNG file, then convert it using utils/fonts_and_graphics/img2cpp.htm
Import file, change for "Vertical drawing" at the end of the page, then click generate. The code you get have to be pasted into the python script. Look at "MARIO", it's self explanatory.
<hr>

### `mod_custom_ctcss_codes.py`
LarSeN contribution: Genuine CTCSS embedded code list is badly numbered. I restored CTCSS base code list+extended codes to the end.
Please keep in mind that Quansheng codeplug software won't be aware of the new ordered list: Just check your channels after programming.
<hr>

### `mod_custom_digits.py`
LarSeN contribution: Grouped some of the best fonts for Big and Small digits display (BBC mode 7, Geneva, Terminus, Videotex, old computer, etc...)

Change fonts used to display big and small digits.
<hr>

### `mod_custom_font.py`
LarSeN contribution: Integrated some good fonts (Apple Chicago, CP/M..)
Customization:
You can generate your own fonts using utils/fonts_and_graphics/img2cpp.htm . You just have to insert generated string to the beginning of the python script, at font = b'\STRINGSTRINGSTRING'
<hr>

### `mod_custom_freq_ranges.py`
The purpose of this mod is to unlock receiving range of the transceiver. Default is 25-630MHz.

Here you can change low and high limit for each frequency band. 
The underscore `_` symbol is omitted by python interpreter and is added only for better readability.
So for example, if you want to fill the gap between 76 and 108Mhz then in second array change first limit from `76_000_000` to `107_999_990` or 
if you want to extend above 600MHz then change last limit from `600_000_000` to `1300_000_000`. Please keep in mind that different ranges 
are demodulated slightly different inside BK4819 chip, and some ranges have enabled AM demodulation while other don't. 
<hr>

### `mod_custom_mdc_data.py`
LarSeN contribution: Aims to produce a better MDC signalling when MDC1200 roger beep is chosen. String is an EOT for PTT-ID 0001.
<hr>

### `mod_custom_noaa_freqs.py`
The default is now replaced with:
``#first 10 PMR446 channels
new_noaa_table =   [446_006_250, 446_018_750, 446_031_250, 446_043_750, 446_056_250, 446_068_750, 446_081_250, 446_093_750, 446_106_250, 446_118_750]``

LarSeN contribution: First 1-7 GMRS channels and 22-20 GMRS call/repeater channels. This is because of forced 12.5kHz deviation.
Also check mod_disable_1050hz_noaa, to use these without 1050Hz toneburst.
Customization: Just set up to 10 new freq values for the frequencies in NOAA scan list, nothing less, nothing more. 
<hr>

### `mod_disable_1050hz_noaa.py`
LarSeN contribution: Permits normal listening and background scan detection of said "NOAA" channels, without needing for 1050Hz toneburst.
<hr>

### `mod_custom_symbols.py`
LarSeN contribution: Integrated BMP converter, and better symbols (I hope!)

Customization: Just edit provided Symbols_mod.bmp. Keep in mind that you must keep orientation and file format as 2 color BMP.

Replaces all symbols on screen with a rotated +90 degree, 1bit BMP
<hr>

### `mod_disable_tx_completely.py`
No customization. 

On ALL frequencies radio shows "DISABLED" info and don't transmit at any band.

ℹ️ Please do not use this mod together with `mod_enable_tx_50to850.py`
<hr>

### `mod_enable_am_everywhere.py`
No customization. 

On ALL frequencies, AM mode will be switchable.
<hr>

### `mod_enable_swd_port.py`
If you are experimenting deep modifications, need active debugging or playing with EEPROM, this could be useful, even for brick recovery.
Not harmful to enable.
<hr>

### `mod_fm_radio_64-108mhz.py`
LarSeN contribution: Now a working 64 to 108MHz, and function keys remapping (F+VFO: memory recall, F+FM:scan, F+FC:auto-MR)
Extends WFM receive range from 64MHz to 108MHz.
<hr>

### `mod_increase_backlight_timeout`
LarSeN contribution: Fixed old derpy way to increase backlight expiry time. Now factor is a multiplier*500ms. New: Backlight forever if set to 5.
<hr>

### `mod_menu_strings.py`
LarSeN contribution: Edited most of the menu text, messages, and option text to get a better conformity to standards. A must have.
<hr>

### `mod_mic_gain.py`
My contribution: Mod is next to useless now. Please check my "utils/mic_calibrator.py". Good values have to be set in EEPROM.

ℹ️ This patch doesn't extend available mic gain steps (they will still be 0-4.) It just increases the _starting point_ on the mic gain scale sent to the BK4819 mic sensitivity register.
<hr>

### `mod_negative_screen.py`
No customization.

Edits initialization routine of ST7565 (LCD controller) to change default LCD mode normal to negative.
<hr>

### `mod_custom_steps.py`
Customization:
```python
# change below sets to new ones, values are in Hz
new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330]
```
Changes array of frequency steps in menu at position 2
<hr>

### `mod_enable_tx_50to850.py`
No customization. You can just disable or enable it in `build.bat`. The purpose of this mod is to **globally disable/bypass** TX lock. 

ℹ️ This patch alone doesn't extend available frequency ranges. For this use `mod_custom_freq_ranges.py` mod.
<hr>

### `mod_negative_screen.py`
No customization. You can just disable or enable it in `build.bat`.

Edits initialization routine of ST7565 (LCD controller) to change default LCD mode normal to negative.
<hr>

### `mod_ota_qrg.py`
Customization:
```python
AIR_COPY_FREQ_HZ = 433_600_000
```

Default value for copying setting over the air aka "AIR COPY" is 410.025 MHz. You can change that default value using this mod.
<hr>

### `mod_roger_beep.py`
LarSeN contribution: Now with single, dual, or triple beep!  Completely rewrote roger routine.
You can change duration and/or frequency for each tone used. Put 0 in correct duration if single ou dual beep is preferred.

Change "Roger" beep tones.
<hr>

### `mod_rssi_bars.py`
LarSeN contribution: Change RSSI meter behaviour, using 7 possible step bars. Evaluating RSSI is done via maths linear approach.
Completely rewrote routine, and created new function to blink flashlight (call, alarm)

Customization:
VHF: @14B2 origin offset, @14B4 slope, @14B6 s=0 limit. UHF: @14CE origin offset, @14D0 slope, @14D2 s=0 limit.
NEED to change Symbols font: 7 bars+eliminate antenna icon. If you disable this mod, please replace Symbols_mod.bmp in v31 directory by Symbols_mod_(without_rssi_patch).bmp

Upgrades genuine RSSI meter. Also makes use of freed ROM space to put new routines which make flashlight blink when called via DTMF SelCall, and when Alarm is triggered.
<hr>

### `mod_widen_scr_range`
LarSeN contribution:
Changes the scrambler inversion frequency range. Step mod from 100Hz to more conventional 115.5Hz, in order to reach theorical scrambling maximum at 3730Hz (~step/2)
<hr>

### `mod_universal_version.py`
Allow to flash the custom output firmware file on UV-K5(8)/UV-K6 and UV-5R PLUS.
Instead of a fixed firmware version number will be `*` Asterisk sign used as placeholder (HEX 2A in fw.ver.bin unpacked). This allows overwrite any existing firmware and make crossflashing possible even on [OSFW based](https://github.com/OneOfEleven/uv-k5-firmware-custom) F/W. It prevent Flasher Errors such as invalid Version etc... The * (wildcard) stands here in code for universal version. It will make it work on all Quansheng UV-K5 and compatible radios based on the same HW Chip.
 
All credits to [LarSeN](https://github.com/Lar-Sen/Quansheng_UV-K5_Kitchen) for his brilliant work.

