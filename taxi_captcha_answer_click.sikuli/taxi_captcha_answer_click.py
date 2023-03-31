 Pattern("_captcha21.png").targetOffset(1,-52)

def clickOnPicture(pPicture):
    if exists(pPicture,0):
        click(pPicture)
        return True
    return False

def clickOnCaptchaAnswer(strAnswer):
    if strAnswer == "60:5":
        result = clickOnPicture("12.png")

    if strAnswer == "Выберите зеленый 10-угольник":
        result = clickOnPicture(Pattern("green star.png").similar(0.96))

    if strAnswer == "Выберите зеленый квадрат":
        result = clickOnPicture("1680246478571.png")

    if strAnswer == "Выберите зеленый треугольник":
        result = clickOnPicture(Pattern("green triang.png").similar(0.80))