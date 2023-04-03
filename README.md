# On Screen Measurement helper

This little script was created with the aim of helping to take measurements with scale directly from any app in the screen of the computer. It should be compatible with all operative system. 

It creates a measurement zone on top of visible screen and allows to click in a desired are spots to take linear measurments.

The first two points determine the scale in pixel equivalent to 1 cm, and then consecutive points determine independent measurements. 

The app is minimizable, so user could change photo, app, tab, etc., and take even more measurements. At the end pressing the key `Tab` it will report the range and outliners if there are any.

## Installation
No installation required, just copy the script `OnScreeM.py` in a given folder and run it using Python, for example:

```Bash
python -m OnScreeM.py
```

## Hotkeys  
`Tab` -> Copy to the clipboard min, max and if possible min outlier and max outlier  
`Backspace` -> Remove from memory last measurement  
`Space` -> Minimize measurement zone  
`Esc` -> Clean measuremnt area and restart scale. Useful to measure multiple photos with different scales. This do not clean measurements in the memory  


## Usage
