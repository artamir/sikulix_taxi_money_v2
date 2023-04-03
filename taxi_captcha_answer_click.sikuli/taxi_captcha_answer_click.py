# -*- coding: utf-8 -*-
from sikuli import *

taxi_base = None

def clickOnPicture(pPicture):
    fn = "clickOnPicture"  
    taxi_base.logger.o(fn)     
    if exists(pPicture,0):
        click(pPicture)
        logger.c(fn)
        return True
    taxi_base.logger.c(fn) 
    return False

def clickOnCaptchaAnswer(strAnswer):
    fn = "clickOnCaptchaAnswer"
    taxi_base.logger.o(fn)
    
    result = False

    type("1",KeyModifier.CTRL)
    sleep(1)
     
    if not result and strAnswer == "60:5":
        result = clickOnPicture("12.png")

    if not result and strAnswer == "Выберите зеленый 10-угольник":
        result = clickOnPicture(Pattern("green star.png").similar(0.96))

    if not result and strAnswer == "Выберите зеленый квадрат":
        result = clickOnPicture("1680246478571.png")

    if not result and strAnswer == "Выберите зеленый треугольник":
        result = clickOnPicture(Pattern("green triang.png").similar(0.81))

    if not result and strAnswer == "Выберите красный круг":
        result = clickOnPicture(Pattern("1680345876365.png").similar(0.67))

    if not result and strAnswer == "Выберите красный прямоугольник":
        result = clickOnPicture("1680346165262.png")
    
    if not result and strAnswer == "Выберите розовый квадрат":
        result = clickOnPicture("1680346773183.png")

    if not result and strAnswer == "Выберите розовый прямоугольник":
        result = clickOnPicture("1680421069708.png")

    if not result and strAnswer == "Выберите розовый прямоугольник":
        result = clickOnPicture("1680421277636.png")

    if not result and strAnswer == "Выберите синий круг":
        result = clickOnPicture("1680421402018.png")

    if not result and strAnswer == "Выберите синий прямоугольник":
        result = clickOnPicture("1680421518245.png")
        
    if not result and strAnswer == "Выберите синий треугольник":
        result = clickOnPicture("1680421755333.png")
        
    if not result and strAnswer == "Отнимите от 11 10":
        result = clickOnPicture("1680421833660.png")

    if not result and strAnswer == "Поделите 30 на 10":
        result = clickOnPicture("1680421932622.png")

    if not result and strAnswer == "Поделите 90 на 2":
        result = clickOnPicture("1680421990173.png")

    if not result and strAnswer == "Помножьте 3 на 4":
        result = clickOnPicture(Pattern("1680422056121.png").similar(0.52))
        
    if not result and strAnswer == "Произведение 3 и 4":
        result = clickOnPicture("1680422172313.png")

    if not result and strAnswer == "Произведение 4 и 2":
        result = clickOnPicture("1680422257135.png")

    if not result and strAnswer == "Сложите 3, 5 + 2":
        result = clickOnPicture("1680422468250.png")

    if not result and strAnswer == "Сложите2 и 4":
        result = clickOnPicture("1680422535985.png")

    if not result:
        _captcha2 = Pattern("_captcha21-2.png").targetOffset(1,-52)
        if exists(_captcha2):
            click()

    taxi_base.logger.c(fn)
    return result