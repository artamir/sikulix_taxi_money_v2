# -*- coding: utf-8 -*-
from sikuli import *

taxi_base = None
answer = ""

def clickOnPicture(pPicture):
    fn = "clickOnPicture"  
    taxi_base.logger.o(fn)     
    region = Region(827,118,277,195) 
    if region.exists(pPicture,0):
        try:
            region.click(pPicture)
        except:
            taxi_base.logger.warning(fn + ": cant click("+pPicture+")")
            taxi_base.logger.c(fn)
            return False
        taxi_base.logger.c(fn)
        return True
    taxi_base.logger.c(fn) 
    return False

def clickOnCaptchaAnswer(strAnswer):
    fn = "clickOnCaptchaAnswer("+strAnswer+")"
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
    if not result and (strAnswer.find("+") > -1 or strAnswer.find("Сложите") > -1 or strAnswer.find("Сумма") > -1 or strAnswer.find("плюс") > -1):
        strAnswer.replace("б","6")
        sum = getSumFromString(strAnswer)            
        answer = str(sum)
        if sum > 0:
            result = getListAndClickOnPictures(sum)
            
    #----------------------------------------------------------
    if not result and (strAnswer.find("Произведение") > -1 or strAnswer.find("Помножьте") > -1):
        strAnswer.replace("б","6")
        prod = getProductFromString(strAnswer)            
        answer = str(prod)
        if prod > 0:
            result = getListAndClickOnPictures(prod)
                           
    #----------------------------------------------------------
    if not result and (strAnswer.find("Отнимите") > -1 or strAnswer.find("Сосчитайте") > -1):
        strAnswer.replace("б","6")
        diff = getDiffFromString(strAnswer)            
        answer = str(diff)
        if diff > 0:
            result = getListAndClickOnPictures(diff)
    
    #----------------------------------------------------------
    if not result and (strAnswer.find(":") > -1 or strAnswer.find("Поделите") > -1):
        strAnswer.replace("б","6")
        div = getDivisionFromString(strAnswer)            
        answer = str(div)
        if div > 0:
            result = getListAndClickOnPictures(div)

    #----------------------------------------------------------        
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
def getProductFromString(s):
    fn = "getSumFromString"
    taxi_base.logger.o(fn)

    numbers = numbersFromString(s)
    prod = 1
    for number in numbers:
        prod *= number

    if prod == 1: prod = 0
    taxi_base.logger.c(fn)
    return prod


#==========================================================================
def getDiffFromString(s):
    fn = "getDiffFromString"
    taxi_base.logger.o(fn)

    numbers = numbersFromString(s)
    diff = numbers[0]
    i=0
    for number in numbers:
        if i == 0: 
            i += 1 
            continue
        diff -= number
        i += 1

    taxi_base.logger.c(fn)
    return diff

#==========================================================================
def getDivisionFromString(s):
    fn = "getDivisionFromString"
    taxi_base.logger.o(fn)

    numbers = numbersFromString(s)
    div = numbers[0]
    i=0
    for number in numbers:
        if i == 0: 
            i += 1 
            continue
        div /= number
        i += 1

    taxi_base.logger.c(fn)
    return div


def getListAndClickOnPictures(num):
    fn = "getListPictures"
    taxi_base.logger.o(fn)
    
    result = False 
    list = getListPictures(num)
    for pic in list:
        if not result: result = clickOnPicture(pic)

    num_list = map(int, str(num))    
    if not result and len(num_list) > 1:
        list = getListPictures(num_list[1])
        for pic in list:
            if not result: result = clickOnPicture(pic)
    
    taxi_base.logger.c(fn)        
    return result

#==========================================================================
def getListPictures(number):
    fn = "getListPictures"
    taxi_base.logger.o(fn)
    list = []
    if number == 1: list  = ["1680775861192.png","1680775975197.png","1682194448992.png","1682194537870.png","1682194621286.png"]
    if number == 2: list  = ["1682196824648.png","1682196925635.png","1682197014937.png","1682193912030.png","1682196809797.png","1682196905043.png","1682196982801.png"]
    if number == 3: list  = ["1682194709257.png","1682194799558.png","1682194893744.png"] 
    if number == 4: list  = ["1680775912844.png",  "1680776031534.png",  "1680776404508.png", "1680934193623.png"] 
    if number == 5: list  = ["1682196366397.png",  "1682196418447.png",  "1682196472946.png", "1682196560431.png",   "1682196669771.png"] 
    if number == 6: list  = ["1680688020353.png",  "1680688441596.png",  "1680688519926.png", "1680688802133.png",  "1680688872401.png", "1680726512084.png" ]    
    if number == 7: list  = ["1680515487197.png",  "1680775584350.png",  "1680775715433.png", "1680776341350.png",  "1680923201723.png"]    
    if number == 8: list  = ["1680728208654.png",  "1680728275937.png",  "1680728400066.png", "1680728538173.png",  "1680728459308.png"  ]    
    if number == 9: list  = ["1680678900795.png",  "1680679013801.png",  "1680679122409.png", "1680679373831.png",  "1680679459717.png", "1680679574363.png"]    
    if number == 10: list = ["1680640982606.png","1680641303054.png","1680642758264.png","1680643063282.png","1680643766353.png","1680700269338.png","1680641157411.png","1680515748953.png","1680642946399.png","1680643292830.png","1680643621285.png","1680682417696.png"]
    if number == 11: list = ["1680670972425.png","1680671106882.png", "1680671205487.png","1680556341159.png"] 
    if number == 12: list = ["1680700513649.png","1680700591875.png", "1680701203457.png","1680701400603.png","1680701552294.png","1680701702544.png", "1680701790674.png", "1680922996271.png"]
    if number == 13: list = ["1680923322881.png"]
    if number == 14: list = ["1680934616554.png"]
    if number == 15: list = []
    if number == 16: list = []
    if number == 17: list = ["1680923418329.png"]
    if number == 18: list = ["1680934428772.png"]
    if number == 19: list = []
    if number == 20: lis  = ["1680923128075.png","1680934511589.png"]
    if number == 0: list  = ["1680934538055.png", "1680934566923.png"]


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

