init:
    $ win= False


init python:
    # окно игры в центре экрана
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # автоматическое объявление изображений
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['images/cliker']
    # вспышка
    flash  = Fade(.25, 0, .5, color="#fff")
    flash2 = Fade(.25, 0, .5, color="#222")

# настройки игры:
    # максимальное значение шкалы
    max_points = 100
    # название картинки (без нумерации кадров)
    img_name = ""
    # первый и последний кадры анимации
    minN = 1
    maxN = 14
    # значение, на которое прибавляется шкала при клике
    # (т.е. сложность игры. 2.0 - очень сложно, 3.0 - легко)
    points_plus = 2.5

# переменные по умолчанию
    # при желании можно поменять и это значение,
    # чтобы точнее подобрать баланс игры
    points_minus = 1.0
    # допустимое время между кликами или
    # скорость анимации (время между сменой кадров)
    ani_time = .1
    # текущий кадр
    number = 0
    # инкремент кадра (+1/-1)
    plus = 1
    # шкала, которую нужно заполнить
    points = 0
    # недавно был клик
    clicked = True
    # смена кадров анимации, если клик был недавно
    # и перерисовка экрана, чтобы увидеть изменения
    def NextFrameF():
        global points, number, plus, clicked
        # если клик был недавно, то продолжаем анимацию,
        # иначе следующего кадра не будет. пауза
        if clicked:
            # следующий/предыдущий кадр
            number += plus
            # если за пределы числа кадров, то анимация в обратную сторону
            if number > maxN:
                number = maxN - 1
                plus = -plus
            if number < minN:
                number = minN + 1
                plus = -plus
        # уменьшение шкалы, если давно не было клика
        points -= points_minus
        if points < 0:
            points = 0
        clicked = False
        # перерисовка экрана
        renpy.restart_interaction()
    # функция → action
    NextFrame = renpy.curry(NextFrameF)

# экран игры
screen clicker:
    # это чтобы игра не продолжилась по клику мышкой
    modal True
    # сбрасываем настройки игры при появлении экрана
    on "show" action [SetVariable("number", 0), SetVariable("plus", 1), SetVariable("clicked", True)]
    # меняем кадр, если клик был недавно,
    # и проверяем на проигрыш
    timer ani_time repeat True action [NextFrame(), If(points <= 0, true=Return(False), false=NullAction())]
    # картинка с анимацией
    add img_name + str(number)
    # отображаем невидимую кнопку для кликов
    # по нажатию прибавляем шкалу и устанавливаем флаг клика
    button:
        text _(" ")
        xfill True
        yfill True
        background "#00000001"
        # если шкала полная, то конец игры, победа
        action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, true=Return(True), false=NullAction())]
    # альтернативное нажатие с клавиатуры
    key "K_SPACE" action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, true=Return(True), false=NullAction())]
    # индикатор
    vbar value StaticValue(points, max_points):
        align (0, 0) # положение на экране
        maximum (150, 150) # размеры
        left_bar "heartempty" # пустое сердце
        right_bar "heart" # полное сердце
        thumb None # тут можно поставить разделитель
        thumb_shadow None # и тень

label cat_click:
    hide screen cat_food
    # всякие ненужные штуки для оформления
    scene expression (img_name + "0")
    pause .8
    #show expression Text("Сейчас будет мини-игра!") at truecenter as txt       
    show expression Text("{color=#fff} {size=+20}Сейчас будет мини-игра! {/size}{/color}") at truecenter as txt
    #" " "Сейчас будет мини-игра!"
        
    with dissolve
    pause
    hide txt
    # начать с 10 очков, чтобы не проиграть сразу же
    $ points = 30

   
    call screen clicker 
    

    # дальше снова пошли всякие ненужные вещи:
    # показываем результаты игры
    if _return:
        # перематываем анимацию до последнего кадра
        while number < maxN:
            $ number += 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + str(maxN))
        with flash
        $win=True
        
    else:
        # перематываем анимацию до первого кадра
        while number > 1:
            $ number -= 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + "0")
        with flash2
        
    
    $ renpy.pause(1.0, hard=True)
    hide txt
    with dissolve
    jump after_click
