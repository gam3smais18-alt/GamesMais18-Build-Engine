label gallery:

    call screen gallery
    
screen gallery():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery"):
            
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1"
                textbutton "2" action Hide("gallery"), Show("gallery2")
                textbutton "3" action Hide("gallery"), Show("gallery3")
                textbutton "4" action Hide("gallery"), Show("gallery4")
                # textbutton "5" action Hide("gallery"), Show("gallery5")
                # textbutton "6" action Hide("gallery"), Show("gallery6")
                # textbutton "7" action Hide("gallery"), Show("gallery7")
                # textbutton "8" action Hide("gallery"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -100
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery"), Show("gallery")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery"), Show("gallery")
                        
        
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing

                    
            if persistent.day149amySex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day149amySex", locked=False)
                        idle Transform("images/v96/day149 morn77.webp", zoom=0.2)
                        hover Transform("images/v96/day149 morn77.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day149pollySpank == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day149pollySpank", locked=False)
                        idle Transform("images/v96/day149 morn288.webp", zoom=0.2)
                        hover Transform("images/v96/day149 morn288.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day149amyPollyThreesome == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day149amyPollyThreesome", locked=False)
                        idle Transform("images/v96/day149 morn369.webp", zoom=0.2)
                        hover Transform("images/v96/day149 morn369.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day149peeParty == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day149peeParty", locked=False)
                        idle Transform("images/v96/day149 morn503.webp", zoom=0.2)
                        hover Transform("images/v96/day149 morn503.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day149abbySex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day149abbySex", locked=False)
                        idle Transform("images/v96/day149 morn592.webp", zoom=0.2)
                        hover Transform("images/v96/day149 morn592.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day150abbyBJ == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day150abbyBJ", locked=False)
                        idle Transform("images/v97/day150 morn7.webp", zoom=0.2)
                        hover Transform("images/v97/day150 morn7.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day150abbyAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day150abbyAnal", locked=False)
                        idle Transform("images/v97/day150 morn68.webp", zoom=0.2)
                        hover Transform("images/v97/day150 morn68.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day150amySandraTagteam == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day150amySandraTagteam", locked=False)
                        idle Transform("images/v97/day150 morn215.webp", zoom=0.2)
                        hover Transform("images/v97/day150 morn215.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day150meganMabelThreesome == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day150meganMabelThreesome", locked=False)
                        idle Transform("images/v97/day150 morn379.webp", zoom=0.2)
                        hover Transform("images/v97/day150 morn379.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            
screen gallery2():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 2"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery2"), Show("gallery")
                textbutton "2"
                textbutton "3" action Hide("gallery2"), Show("gallery3")
                textbutton "4" action Hide("gallery2"), Show("gallery4")
                # textbutton "5" action Hide("gallery2"), Show("gallery5")
                # textbutton "6" action Hide("gallery2"), Show("gallery6")
                # textbutton "7" action Hide("gallery2"), Show("gallery7")
                # textbutton "8" action Hide("gallery2"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery2"), Show("gallery2")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery2"), Show("gallery2")
                        
        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
                    
                    
            if persistent.day150catShawnaThreesome == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day150catShawnaThreesome", locked=False)
                        idle Transform("images/v97/day150 morn488.webp", zoom=0.2)
                        hover Transform("images/v97/day150 morn488.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day150catDoublePee == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day150catDoublePee", locked=False)
                        idle Transform("images/v97/day150 morn586.webp", zoom=0.2)
                        hover Transform("images/v97/day150 morn586.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day151shawnaAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day151shawnaAnal", locked=False)
                        idle Transform("images/v98/day151 morn14.webp", zoom=0.2)
                        hover Transform("images/v98/day151 morn14.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day151allisonSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day151allisonSex", locked=False)
                        idle Transform("images/v98/day151 morn178.webp", zoom=0.2)
                        hover Transform("images/v98/day151 morn178.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day151gilfOrgy == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day151gilfOrgy", locked=False)
                        idle Transform("images/v98/day151 morn272.webp", zoom=0.2)
                        hover Transform("images/v98/day151 morn272.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day151anabelleSophiaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day151anabelleSophiaSex", locked=False)
                        idle Transform("images/v98/day151 morn494.webp", zoom=0.2)
                        hover Transform("images/v98/day151 morn494.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day152anabelleMilked == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day152anabelleMilked", locked=False)
                        idle Transform("images/v99/day152 morn17.webp", zoom=0.2)
                        hover Transform("images/v99/day152 morn17.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day152peneOrgy == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day152peneOrgy", locked=False)
                        idle Transform("images/v99/day152 morn107.webp", zoom=0.2)
                        hover Transform("images/v99/day152 morn107.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day152isabellaCatThreesome == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day152isabellaCatThreesome", locked=False)
                        idle Transform("images/v99/day152 morn195.webp", zoom=0.2)
                        hover Transform("images/v99/day152 morn195.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)


screen gallery3():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 3"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery3"), Show("gallery")
                textbutton "2" action Hide("gallery3"), Show("gallery2")
                textbutton "3" 
                textbutton "4" action Hide("gallery3"), Show("gallery4")
                # textbutton "5" action Hide("gallery3"), Show("gallery5")
                # textbutton "6" action Hide("gallery3"), Show("gallery6")
                # textbutton "7" action Hide("gallery3"), Show("gallery7")
                # textbutton "8" action Hide("gallery3"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery3"), Show("gallery3")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery3"), Show("gallery3")
                        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
                    
            if persistent.day152asamiTitjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day152asamiTitjob", locked=False)
                        idle Transform("images/v99/day152 morn300.webp", zoom=0.2)
                        hover Transform("images/v99/day152 morn300.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day152debbieZeldaAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day152debbieZeldaAnal", locked=False)
                        idle Transform("images/v99/day152 morn362.webp", zoom=0.2)
                        hover Transform("images/v99/day152 morn362.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day152genevieveJosianneThreesome == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day152genevieveJosianneThreesome", locked=False)
                        idle Transform("images/v99/day152 morn511.webp", zoom=0.2)
                        hover Transform("images/v99/day152 morn511.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day153deanSleep == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day153deanSleep", locked=False)
                        idle Transform("images/v100/day153 morn1.webp", zoom=0.2)
                        hover Transform("images/v100/day153 morn1.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day153genevieveCunni == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day153genevieveCunni", locked=False)
                        idle Transform("images/v100/day153 morn42.webp", zoom=0.2)
                        hover Transform("images/v100/day153 morn42.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day153jamilaBreastfeed == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day153jamilaBreastfeed", locked=False)
                        idle Transform("images/v100/day153 morn103.webp", zoom=0.2)
                        hover Transform("images/v100/day153 morn103.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day153allisonPriyaBJ == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day153allisonPriyaBJ", locked=False)
                        idle Transform("images/v100/day153 morn157.webp", zoom=0.2)
                        hover Transform("images/v100/day153 morn157.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day153yvonneTamed == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day153yvonneTamed", locked=False)
                        idle Transform("images/v100/day153 morn275.webp", zoom=0.2)
                        hover Transform("images/v100/day153 morn275.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day153missesLeeNTR == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day153missesLeeNTR", locked=False)
                        idle Transform("images/v100/day153 morn441.webp", zoom=0.2)
                        hover Transform("images/v100/day153 morn441.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            

screen gallery4():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 4"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery4"), Show("gallery")
                textbutton "2" action Hide("gallery4"), Show("gallery2")
                textbutton "3" action Hide("gallery4"), Show("gallery3")
                textbutton "4"
                # textbutton "5" action Hide("gallery4"), Show("gallery5")
                # textbutton "6" action Hide("gallery4"), Show("gallery6")
                # textbutton "7" action Hide("gallery4"), Show("gallery7")
                # textbutton "8" action Hide("gallery4"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery4"), Show("gallery4")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery4"), Show("gallery4")
                        
        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
            
            if persistent.day154aikoSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day154aikoSex", locked=False)
                        idle Transform("images/v101/day154 morn17.webp", zoom=0.2)
                        hover Transform("images/v101/day154 morn17.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day154catPlugged == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day154catPlugged", locked=False)
                        idle Transform("images/v101/day154 morn97.webp", zoom=0.2)
                        hover Transform("images/v101/day154 morn97.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day154catMilaAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day154catMilaAnal", locked=False)
                        idle Transform("images/v101/day154 morn177.webp", zoom=0.2)
                        hover Transform("images/v101/day154 morn177.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day154mayorStripsearch == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day154mayorStripsearch", locked=False)
                        idle Transform("images/v101/day154 morn347.webp", zoom=0.2)
                        hover Transform("images/v101/day154 morn347.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day154kaylaMassage == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day154kaylaMassage", locked=False)
                        idle Transform("images/v101/day154 morn531.webp", zoom=0.2)
                        hover Transform("images/v101/day154 morn531.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
                        
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
                
            
# screen gallery5():
    # tag menu
    # add "ui/bg.jpg"
    
    # use game_menu("Gallery 5"):
            
        
        # hbox:
                # style_prefix "page"

                # xalign 0.5
                # yalign 1.0
                # yoffset -30

                # spacing gui.page_spacing
                

                
                # textbutton "1" action Hide("gallery5"), Show("gallery")
                # textbutton "2" action Hide("gallery5"), Show("gallery2")
                # textbutton "3" action Hide("gallery5"), Show("gallery3")
                # textbutton "4" action Hide("gallery5"), Show("gallery4")
                # textbutton "5"
                # textbutton "6" action Hide("gallery5"), Show("gallery6")
                # textbutton "7" action Hide("gallery5"), Show("gallery7")
                # textbutton "8" action Hide("gallery5"), Show("gallery8")

        
        # vbox:
            # frame:
                # yoffset -125
                # xoffset -50
            
                # if persistent.g_Unlock == 1:
                    # textbutton _("Lock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery5"), Show("gallery5")
                        
                # else:
                    # textbutton _("Unlock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery5"), Show("gallery5")
                        
        
            
        # grid 3 3:
            # style_prefix "slot"

            # xalign 0.5
            # yalign 0.5
            # xpos 650
            # ypos 360
            
            # spacing gui.slot_spacing
            
            # if persistent.day145amyNTRliz == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day145amyNTRliz", locked=False)
                        # idle Transform("images/v92/day145 morn33.webp", zoom=0.2)
                        # hover Transform("images/v92/day145 morn33.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day145amyRimjob == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day145amyRimjob", locked=False)
                        # idle Transform("images/v92/day145 morn253.webp", zoom=0.2)
                        # hover Transform("images/v92/day145 morn253.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day145deanSpank == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day145deanSpank", locked=False)
                        # idle Transform("images/v92/day145 morn625.webp", zoom=0.2)
                        # hover Transform("images/v92/day145 morn625.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day145lizBJ == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day145lizBJ", locked=False)
                        # idle Transform("images/v92/day145 morn662.webp", zoom=0.2)
                        # hover Transform("images/v92/day145 morn662.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
                        
            # if persistent.day146deanSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day146deanSex", locked=False)
                        # idle Transform("images/v93/day146 morn2.webp", zoom=0.2)
                        # hover Transform("images/v93/day146 morn2.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day146allisonSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day146allisonSex", locked=False)
                        # idle Transform("images/v93/day146 morn226.webp", zoom=0.2)
                        # hover Transform("images/v93/day146 morn226.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
                        
            # if persistent.day146jamilaSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day146jamilaSex", locked=False)
                        # idle Transform("images/v93/day146 morn266.webp", zoom=0.2)
                        # hover Transform("images/v93/day146 morn266.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day146shizukaSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day146shizukaSex", locked=False)
                        # idle Transform("images/v93/day146 morn345.webp", zoom=0.2)
                        # hover Transform("images/v93/day146 morn345.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
                        
            # if persistent.day146asamiCatThreesome == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day146asamiCatThreesome", locked=False)
                        # idle Transform("images/v93/day146 morn409.webp", zoom=0.2)
                        # hover Transform("images/v93/day146 morn409.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            

# screen gallery6():
    # tag menu
    # add "ui/bg.jpg"
    
    # use game_menu("Gallery 6"):
            
        
        # hbox:
                # style_prefix "page"

                # xalign 0.5
                # yalign 1.0
                # yoffset -30

                # spacing gui.page_spacing
                

                
                # textbutton "1" action Hide("gallery6"), Show("gallery")
                # textbutton "2" action Hide("gallery6"), Show("gallery2")
                # textbutton "3" action Hide("gallery6"), Show("gallery3")
                # textbutton "4" action Hide("gallery6"), Show("gallery4")
                # textbutton "5" action Hide("gallery6"), Show("gallery5")
                # textbutton "6"
                # textbutton "7" action Hide("gallery6"), Show("gallery7")
                # textbutton "8" action Hide("gallery6"), Show("gallery8")

        
        # vbox:
            # frame:
                # yoffset -125
                # xoffset -50
            
                # if persistent.g_Unlock == 1:
                    # textbutton _("Lock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery6"), Show("gallery6")
                        
                # else:
                    # textbutton _("Unlock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery6"), Show("gallery6")
                        
        
        # grid 3 3:
            # style_prefix "slot"

            # xalign 0.5
            # yalign 0.5
            # xpos 650
            # ypos 360
            
            # spacing gui.slot_spacing
            
            # if persistent.day147amyShowerSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day147amyShowerSex", locked=False)
                        # idle Transform("images/v94/day147 morn55.webp", zoom=0.2)
                        # hover Transform("images/v94/day147 morn55.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day147mariaSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day147mariaSex", locked=False)
                        # idle Transform("images/v94/day147 morn192.webp", zoom=0.2)
                        # hover Transform("images/v94/day147 morn192.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148helgaHandjob == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148helgaHandjob", locked=False)
                        # idle Transform("images/v94/day147 morn451.webp", zoom=0.2)
                        # hover Transform("images/v94/day147 morn451.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day147helgaAssFingered == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day147helgaAssFingered", locked=False)
                        # idle Transform("images/v94/day147 morn538.webp", zoom=0.2)
                        # hover Transform("images/v94/day147 morn538.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148helgaAnal == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148helgaAnal", locked=False)
                        # idle Transform("images/v95/day148 morn1.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn1.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148jamilaHelgaBreastfeed == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148jamilaHelgaBreastfeed", locked=False)
                        # idle Transform("images/v95/day148 morn95.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn95.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148anabelleSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148anabelleSex", locked=False)
                        # idle Transform("images/v95/day148 morn169.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn169.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148opheliaBJ == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148opheliaBJ", locked=False)
                        # idle Transform("images/v95/day148 morn254.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn254.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148imogeneCunni == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148imogeneCunni", locked=False)
                        # idle Transform("images/v95/day148 morn339.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn339.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            
# screen gallery7():
    # tag menu
    # add "ui/bg.jpg"
    
    # use game_menu("Gallery 7"):
            
        
        # hbox:
                # style_prefix "page"

                # xalign 0.5
                # yalign 1.0
                # yoffset -30

                # spacing gui.page_spacing
                

                
                # textbutton "1" action Hide("gallery7"), Show("gallery")
                # textbutton "2" action Hide("gallery7"), Show("gallery2")
                # textbutton "3" action Hide("gallery7"), Show("gallery3")
                # textbutton "4" action Hide("gallery7"), Show("gallery4")
                # textbutton "5" action Hide("gallery7"), Show("gallery5")
                # textbutton "6" action Hide("gallery7"), Show("gallery6")
                # textbutton "7"
                # textbutton "8" action Hide("gallery7"), Show("gallery8")

        
        # vbox:
            # frame:
                # yoffset -125
                # xoffset -50
            
                # if persistent.g_Unlock == 1:
                    # textbutton _("Lock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery7"), Show("gallery7")
                        
                # else:
                    # textbutton _("Unlock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery7"), Show("gallery7")
                        
        
        # grid 3 3:
            # style_prefix "slot"

            # xalign 0.5
            # yalign 0.5
            # xpos 650
            # ypos 360
            
            # spacing gui.slot_spacing
            
            # if persistent.day148debbiePeeDrink == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148debbiePeeDrink", locked=False)
                        # idle Transform("images/v95/day148 morn425.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn425.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day148imogeneSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day148imogeneSex", locked=False)
                        # idle Transform("images/v95/day148 morn486.webp", zoom=0.2)
                        # hover Transform("images/v95/day148 morn486.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
            
            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
            
            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
            
            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
            
            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
            
            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)

            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)

# screen gallery8():
    # tag menu
    # add "ui/bg.jpg"
    
    # use game_menu("Gallery 8"):
            
        
        # hbox:
                # style_prefix "page"

                # xalign 0.5
                # yalign 1.0
                # yoffset -30

                # spacing gui.page_spacing
                

                
                # textbutton "1" action Hide("gallery8"), Show("gallery")
                # textbutton "2" action Hide("gallery8"), Show("gallery2")
                # textbutton "3" action Hide("gallery8"), Show("gallery3")
                # textbutton "4" action Hide("gallery8"), Show("gallery4")
                # textbutton "5" action Hide("gallery8"), Show("gallery5")
                # textbutton "6" action Hide("gallery8"), Show("gallery6")
                # textbutton "7" action Hide("gallery8"), Show("gallery7")
                # textbutton "8"

        
        # vbox:
            # frame:
                # yoffset -125
                # xoffset -50
            
                # if persistent.g_Unlock == 1:
                    # textbutton _("Lock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery8"), Show("gallery8")
                        
                # else:
                    # textbutton _("Unlock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery8"), Show("gallery8")
                        
        
            
        # grid 3 3:
            # style_prefix "slot"

            # xalign 0.5
            # yalign 0.5
            # xpos 650
            # ypos 360
            
            # spacing gui.slot_spacing
            
            # if persistent.day84pollyFinger == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day84pollyFinger", locked=False)
                        # idle Transform("images/v35/day84 morn141.webp", zoom=0.2)
                        # hover Transform("images/v35/day84 morn141.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day84lizMasturbate == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day84lizMasturbate", locked=False)
                        # idle Transform("images/v35/day84 night102.webp", zoom=0.2)
                        # hover Transform("images/v35/day84 night102.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day85jamilaBreastfeed == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day85jamilaBreastfeed", locked=False)
                        # idle Transform("images/v35/day85 morn33.webp", zoom=0.2)
                        # hover Transform("images/v35/day85 morn33.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day85anabelleFinger == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day85anabelleFinger", locked=False)
                        # idle Transform("images/v35/day85 ana46.webp", zoom=0.2)
                        # hover Transform("images/v35/day85 ana46.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day86shizukashower == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day86shizukashower", locked=False)
                        # idle Transform("images/v36/day86 morn50.webp", zoom=0.2)
                        # hover Transform("images/v36/day86 morn50.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day87priyaBJ == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day87priyaBJ", locked=False)
                        # idle Transform("images/v37/day87 doc73.webp", zoom=0.2)
                        # hover Transform("images/v37/day87 doc73.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day87jamilaBath == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day87jamilaBath", locked=False)
                        # idle Transform("images/v37/day87 jam2.webp", zoom=0.2)
                        # hover Transform("images/v37/day87 jam2.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day87sophiaSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day87sophiaSex", locked=False)
                        # idle Transform("images/v37/day87 soph79.webp", zoom=0.2)
                        # hover Transform("images/v37/day87 soph79.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)

            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
                    

python early:
    def unlockGallery():
        if persistent.g_Unlock == 1:
            persistent.g_Unlock = 0
        elif persistent.g_Unlock == 0:
            persistent.g_Unlock = 1
            
python early:
    def changePage(pageNum):
        Hide(renpy.current_screen)