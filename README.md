# On Screen Measurement helper

This little script was created with the aim of helping to take measurements with scale directly from any app in the screen of the computer. It should be compatible with all operative system. 

It creates a measurement zone on top of visible screen and allows to click in a desired are spots to take linear measurments.

The first two points determine the scale in pixel equivalent to 1 cm, and then consecutive points determine independent measurements. Optionally, by pressing a key (a to z) allow to take measurments of 26 independent measurments. See usage for more details.

The app is minimizable, so user could change photo, app, tab, etc., and take even more measurements. At the end pressing the key `Tab` it will report the range and outliners if there are any.

## Installation
No installation required.

Use any of the binaries in the releases. Those are executables and should work on Windows (`OnScreeM.exe`) or Linux (`OnScreeM`).

Or just copy the script `OnScreeM.py` in any folder and run it using Python v.3.x.x, for example:

```Bash
python -m OnScreeM.py
```

### Dependencies
The library `tkinter` is needed. The simplest way to get that library is by using `pip`

```Bash
pip install tk
```

## Hotkeys  
`Tab` -> Copy to the clipboard min, max and if possible min outlier and max outlier  
`Backspace` -> Remove from memory last measurement  
`Space` -> Minimize measurement zone  
`Esc` -> Clean measuremnt area and restart scale. Useful to measure multiple photos with different scales. This do not clean measurements in the memory  
`Alt + F4` -> Close the app  
`a` to `z` -> Any character key (a to z) to take multiple measurements of multiple traits or things.


## Usage
