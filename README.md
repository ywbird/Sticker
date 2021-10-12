# Sticker.py

Animated Custom Sticker using PyQt5 with Python.
Create Sticker with .exe file or python with just arguments. 

float sticker by @kairess  
compile, sys.argv arguments code by @ywbird  
origin repo : [link](https://github.com/kairess/animated-wallpaper-sticker)  
  
기본 스티커 코드 by 빵형(@kairess)  
컴파일, 설정값 by 고앵이(@ywbird)  
기존 코드 리포 : [링크](https://github.com/kairess/animated-wallpaper-sticker)

# Usage

```batch
        ┌─img path─┐     ┌Always on top(1 for true 0 for false)
sticker gif/gura.gif 0.2 1 200,200 -100,100 100,0 120
                     └┬┘   └──┬──┘ ├──────┘ ├───┘ └─┤
                  Size┘   [Position└from pos└to pos └speed]←optional
```

Just sticker:

```batch
sticker gif/gura.gif 0.2 1 200,200
```

Sticker with movements:

```batch
sticker gif/gura.gif 0.2 1 200,200 -100,100, 100,0 120
```

Image types:
- `.png` 
- `.gif`
- `.jpg`
- `.ico`
and more...