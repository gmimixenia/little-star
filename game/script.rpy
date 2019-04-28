init:
     image m_bg = "Images/main_bg.png"


screen main_ch:
  vbox xalign 0.45 yalign 0.45:
        textbutton "Первая глава":
             text_color "#ffffff"
             text_hover_color "#97BEF8"
             action Jump("first_step")
        textbutton "Вторая глава":
             text_color "#ffffff"
             text_hover_color "#97BEF8"
             action Jump("second_step")
        textbutton "Назад":
             text_color "#ffffff"
             text_hover_color "#97BEF8"
             action MainMenu()

label start:
  scene m_bg with fade
label m_ch:
  show screen main_ch
  pause
  jump m_ch

  return
