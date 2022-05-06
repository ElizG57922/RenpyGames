screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/stats_idle.png"
        action ShowMenu("StatsUI")

screen StatsUI:
    add "UI/bg gray.png"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding -0
        ypadding 0

        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Sanity" size 30

            vbox:
                spacing 10
                text "[sanity]" size 30

    imagebutton:
        xalign 1.0
        yalign 0.0
        xpadding -30
        ypadding 30
        idle "UI/stats_return.png"
        #auto "UI/return_%s.png"
        action Return()