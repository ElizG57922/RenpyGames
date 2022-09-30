screen bars(time, totalTime):
    bar:
        xalign 0 ypos 10
        xsize 500
        value AnimatedValue(time, totalTime) style "bar"