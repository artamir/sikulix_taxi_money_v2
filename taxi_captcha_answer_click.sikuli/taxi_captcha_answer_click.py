# -*- coding: utf-8 -*-
from sikuli import *

taxi_base = None

def clickOnPicture(pPicture):
    fn = "clickOnPicture"  
    taxi_base.logger.o(fn)     
    if exists(pPicture,0):
        click(pPicture)
        taxi_base.logger.c(fn)
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

    if not result and strAnswer == "3 + 4":
        result = clickOnPicture("1680515487197.png")

    if not result and strAnswer == "30: 5":
        result = clickOnPicture("1680515648836.png")

    if not result and strAnswer == "7 + 3":
        result = clickOnPicture("1680515748953.png")

    if not result and strAnswer == "Выберите зеленый квадрат":
        result = clickOnPicture("1680515841336.png")

    if not result and strAnswer == "Выберите зеленый круг":
        result = clickOnPicture("1680553970392.png")

    if not result and strAnswer == "Выберите красный 10-угольник":
        result = clickOnPicture("1680554074756.png")

    if not result and strAnswer == "Выберите красный квадрат":
        result = clickOnPicture("1680554215437.png")

    if not result and strAnswer == "Выберите розовый треугольник":
        result = clickOnPicture("1680554362616.png")

    if not result and strAnswer == "30:2":
        result = clickOnPicture("1680556176080.png")

    if not result and strAnswer == "4 + 8":
        result = clickOnPicture("1680556257403.png")

    if not result and strAnswer == "6 + 6 + 5":
        result = clickOnPicture("1680556341159.png")

    if not result and strAnswer == "7 + 7":
        result = clickOnPicture("1680556415158.png")

    if not result and strAnswer == "7 плюс 7 + 2":
        result = clickOnPicture("1680556486708.png")

    if not result and strAnswer == "Выберите зеленый ромб":
        result = clickOnPicture("1680556635489.png")
        
    #-------------------------------------------------------------------
    if not result and strAnswer.find("ромб") > -1:
        result = clickOnPicture("1680556635489.png")
    
    if not result and strAnswer.find("треугольник") > -1:
        result = clickOnPicture("1680554362616.png")

    if not result and strAnswer.find("квадрат") > -1:
        result = clickOnPicture("1680554215437.png")

    if not result and strAnswer.find("10-угольник") > -1:
        result = clickOnPicture("1680554074756.png")

    if not result and strAnswer.find("круг") > -1:
        result = clickOnPicture("1680553970392.png")

    #----------------------------------------------------------
    if not result and (strAnswer.find("Сложите") > -1 or strAnswer.find("Сумма") > -1 or strAnswer.find("плюс") > -1):
        strAnswer.replace("б","6")
        sum = getSumFromString(strAnswer)            
        if sum > 0:
            list = getListPictures(sum)
            for pic in list:
                if not result: result = clickOnPicture(pic)
    
    if not result:
        _captcha2 = Pattern("_captcha21-2.png").targetOffset(1,-52)
        if exists(_captcha2):
            click()

    taxi_base.logger.c(fn)
    return result

#==========================================================================
def getSumFromString(s):
    fn = "getSumFromString"
    taxi_base.logger.o(fn)

    numbers = numbersFromString(s)
    sum = 0
    for number in numbers:
        sum += number

    taxi_base.logger.c(fn)
    return sum

#==========================================================================
def getListPictures(number):
    fn = "getListPictures"
    taxi_base.logger.o(fn)
    list = [] 
    if number == 10: list = ["1680640982606.png","1680641303054.png","1680642758264.png","1680643063282.png","1680643766353.png","1680641157411.png","1680515748953.png","1680642946399.png","1680643292830.png","1680643621285.png"]
    if number == 11: list = ["1680670972425.png","1680671106882.png","1680671205487.png","1680556341159.png"] 
    if number == 0: list = []
     
    taxi_base.logger.c(fn)
    return list
#==========================================================================
def numbersFromString(s):
    fn = "numbersFromString"
    taxi_base.logger.o(fn)
    
    num_list = []
 
    num = ''
    for char in s:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    
    taxi_base.logger.c(fn) 
    return num_list

