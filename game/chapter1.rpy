init:
     $ vik = Character(u'Викки', color="#0000aa")
     image bg = "Images/room.jpg"
     image boy = "Images/hero.png"
     $ text = Character(" ",kind=nvl)

screen toy:
     imagebutton xalign 0.85 yalign 0.71:
        idle ("Images/toy.png")
        action Jump ("next")
     imagebutton xalign 0.25 yalign 0.61:
        idle ("Images/toy2.png")
        action Jump ("not")
     imagebutton xalign 0.33 yalign 0.51:
       idle ("Images/toy3.png")
       action Jump ("not")

label first_step:

    ## Вставить картинку с главой
    hide screen main_ch
    $ teddy=0
    scene room
    show hero
    window hide
    pause
    text "{i}(Дзынь-дзынь){/i}"
    text "{i}Это громко, как и всегда, звонит будильник.{/i}"
    vik "{i}Доброе утро!{/i}"
    vik "{i}Уже светит яркое солнышко!{/i}"
    vik "{i}Мне пора вставать с кроватки и собирать свои вещи.{/i}"
    vik "{i}Где же мой любимый плюшевый мишка?{/i}"
    vik "{i}Я должен его найти{/i}"
    show screen toy
    show hero

label find:
    window hide
    pause

    if teddy==0:
        jump find

label next:

    $ teddy = 1
    hide screen toy
    vik "{i}Наконец-то я нашел его!{/i}"
    vik "{i}Но мне уже пора идти{/i}"
    vik "{i}Мама наверняка ждет меня на кухне{/i}"
    vik "{i}Мне нужно позавтракать и ждать няню{/i}"



    return

label not:
    vik "{i}Это не он{/i}"
    vik "{i}Мне нужно поискать получше{/i}"
    jump find
