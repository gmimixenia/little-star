init:
     $ vik = Character(u'Викки', color="#0000aa")
     $ ron = Character(u'Рон',color="#00aacc")
     image chapter="Images/chapter1.jpg"
     image ron="Images/ron.png"
     image kitchen="Images/kitchen.jpg"
     image bg = "Images/room.jpg"
     image hero ="Images/hero.png"
     $ text = Character(" ",kind=nvl)


label second_step:


    stop music fadeout 2.0

    hide screen main_ch

    scene black with fade
    window hide
    text "Глава будет скоро добавлена. Насладитесь пока первой :)"

    return 0
