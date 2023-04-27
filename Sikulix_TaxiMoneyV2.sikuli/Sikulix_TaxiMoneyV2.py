import datetime
import time
import csv

import taxi_logging as logger
import taxi_base
import taxi_ability_click
import taxi_captcha_answer_click

urlGarage = "https://www.taxi-money.net/garage/"
captchaPath = "c:\\Sikulix_scripts\\git_sikulix_taximoney\\sikulix_taximoney\\captcha\\"
urlYaPictureSearch = r'https://yandex.ru/images/search?rpt=imageview'

auto = None
dictTaxi = {"OCR":
                {"id":"OCR",
                "tab":"1"},
            "319558":
                {"id":"319558",
                "tab":"2",
                "pic":"319558.png",
                "orderPic":"rabota",
                "findWords":"работа",
                "abilities":["expensive order", "fast order"],
                "use diamonds reload": True},
            "264417":
                {"id":"264417",
                "tab":"3",
                "pic":"264417.png",
                "orderPic":"diamonds",
                "findWords":"бонус",
                #"orderPic":"haltura",
                #"findWords":"халтура",
                "use diamonds reload": True}}

#firefox = App("c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
firefox = App(r"i:\\FirefoxPortable\\App\\Firefox64\\firefox.exe")
firefox.open()

fault_capcha_counter = 0


region = Region(450,113,691,547)
regionMargin = Region(1106,270,237,311)
regionSideMenu = Region(243,113,236,517)

#=======================================================================================
def debugStop():
    1/0



#=======================================================================================
def saveCaptcha():
    fn = "saveCaptcha"
    logger.o(fn)    
    #return 
    rightClick(Pattern("1679759379856.png").targetOffset(-4,-111))
    wait("1679759439561.png")
    click()    

    if exists(Pattern("captchaFileName.png").targetOffset(40,-11),60):
        click()
    if exists(Pattern("btns openlink cancel.png").targetOffset(51,-3)):
        click()
        logger.c(fn) 
        return None
            
    type(r"a",KeyModifier.CTRL)
    today = datetime.datetime.today()
    t = today.strftime("%Y-%m-%d-%H-%M-%S")    
    fileName = captchaPath+t+".jpg"
    paste(fileName)
    type(Key.ENTER)
    try:
        waitVanish("1679905123827.png",60)
    except:
        if exists("1680786260373.png"):
            click()
            logger.c(fn) 
            return None


    if exists("1679905123827.png",0):
        if exists("1681126953941.png",0):
            try:
                click()
            except:
                print "cant click 'sohranit'"
        
    logger.c(fn) 
    return(fileName)    

#=======================================================================================
def goToURL(url):
    fn = "goToURL"
    logger.o(fn)
    type(u"l",KeyModifier.CTRL)
    type(u"a",KeyModifier.CTRL)
    paste(url)
    sleep(1)
    type(Key.ENTER)
    type(Key.ESC)
    logger.c(fn)

#=======================================================================================
def getTabNumber(taxiID=""):
    fn = "getTabNumber(taxiID="+taxiID+")"
    logger.o(fn)

    if taxiID == "":
        taxiID = auto["id"]
 
    logger.c(fn)
    return dictTaxi[taxiID]["tab"]


#=======================================================================================
def createTabs():
    fn = "createTabs"
    logger.o(fn)
    for key,val in dictTaxi.items():
        type(u"t",KeyModifier.CTRL)
        sleep(2)
    logger.c(fn)


#=======================================================================================
def openOCRTab():
    fn = "openOCRTab"
    logger.o(fn)
    wait("1679776061740.png", 120)
    tabNumber = getTabNumber("OCR")
    type(tabNumber,KeyModifier.CTRL)
    sleep(2)
    goToURL(urlYaPictureSearch)
    wait(Pattern("find_picture.png").similar(0.97).targetOffset(54,2),120)
        
    logger.c(fn)

#=======================================================================================
def ocrCaptcha(filename):
    fn = "ocrCaptcha" 
    logger.c(fn)
    
    type(getTabNumber("OCR"),KeyModifier.CTRL)
    wait(Pattern("find_picture.png").similar(0.97).targetOffset(54,2),120)
    sleep(1)
    click() 
    try: 
        wait("select_file.png")
        click()
    except:
        type(getTabNumber(auto["id"]), KeyModifier.CTRL)
        return False

     
    if exists("file_name.png",10):
        click()
        paste(filename)
        type(Key.ENTER)
    
    try:
        waitVanish("unload file.png")
    except:
        click("1680675612848.png")

    
    if exists("unload file.png"):
        click("1680675612848.png")        
        
    #recognizePic = Pattern("btn recognize text.png").similar(0.84)

    recognizePic =  "recognizePic.png"
    if exists(recognizePic,10): 
        taxi_base.highlightPicture(recognizePic)
        try:
            click(recognizePic)
        except:
            print "cant click on recognizePic"
         
    if exists(Pattern("copy_in_buffer.png").similar(0.97)):
        click()
    else:
        type(getTabNumber(auto["id"]), KeyModifier.CTRL)
        return False
    
    sleep(2) 
    captchaText = firefox.getClipboard()
    captchaText = captchaText.encode('utf-8').strip().splitlines()[0] 
    result = taxi_captcha_answer_click.clickOnCaptchaAnswer(captchaText)

    if not result:
        answer = taxi_captcha_answer_click.answer
        csvfile = open("captcha.csv", 'a') #открыть на дозапись
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([answer, captchaText, filename])
        csvfile.close()
    
    type(getTabNumber(auto["id"]), KeyModifier.CTRL)
    return result

#=======================================================================================
def waitPageLoad():
    fn = "waitPageLoad"
    logger.o(fn)
    _region = Region(6,23,395,82)
    #_region.wait("1678363257952.png",60)
    _region.wait("1682631301869.png",60)
    logger.c(fn)


#=======================================================================================
def isOrderAccepted():
    fn = "isOrderAccepted"
    logger.o(fn)

    status = getAutoStatus()
    if status.find("empty") > -1:
        logger.c(fn)
        return False

    #----------------------------------------------------
    m = exists("1682623392722.png", 0)

    if m:
        r = Region(m.getX()+20, m.getY(),70,20)
        r.highlight(1)
        t = r.text()
        print(t)
        csvfile = open("orders.csv", 'a') #открыть на дозапись
        csvwriter = csv.writer(csvfile, dialect='excel-tab')
        csvwriter.writerow([auto["id"], t, datetime.datetime.now().strftime('%d.%m.%Y %H:%M')])
        csvfile.close()
    #----------------------------------------------------


    logger.c(fn)
    return True
    
    
    #_pic = "_ZacazPrineat.png"
    #if taxi_base.scrollToOrderDown(_pic, region):
    #    return True

    #return False

#=======================================================================================
def reloadOrders():
    fn="reloadOrders"
    logger.o(fn)
    taxi_base.goToPageDown()
    logger.warning(fn+": auto['use diamonds reload'] = "+str(auto["use diamonds reload"]))
    if not auto["use diamonds reload"]:
        status = getAutoStatus()
        while not (status == "empty reload"):
            logger.warning(fn+":status = " + status)
            if time.time() - auto.get("emptyStart", time.time()) > 1.2*60:
                logger.warning(fn+":timer emptyStart = " + str(time.time() - auto.get("emptyStart", time.time())))
                loadAutoPage()
                logger.c(fn)
                return
            wait(1)
            status = getAutoStatus()
            taxi_base.goToPageDown()
        
    if not taxi_base.ifExistsClick("load orders.png"):
        if not taxi_base.ifExistsClick("update.png"):
            loadAutoPage()
            logger.c(fn)
            return

    wait(10)

    maxWait = 5 
    while isPageBusy() and maxWait >= 0:
        wait(1)
        maxWait -= 1

    if maxWait <= 0:
        loadAutoPage()
    logger.c(fn)
    
#=======================================================================================
def isPageBusy():
    fn = "isPageBusy"
    logger.o(fn)
    _pic = Pattern("loadOrdersIsBusy.png").similar(0.84) 
    if exists(_pic,1):
        logger.warning("    isPageBusy: True")
        if not taxi_base.highlightPicture(_pic):
            logger.c(fn)
            return False
        
        logger.c(fn)
        return True

    logger.c(fn)
    return False

#=======================================================================================
def checkCaptchaOrder():
    fn = "checkCaptchaOrder"
    logger.o(fn)
    _pic = getOrderCheckPic(1)
    if exists(_pic,0):
        logger.c(fn)
        return True

    _pic = getOrderCheckPic(2)
    if exists(_pic,0):
        logger.c(fn)
        return True
    logger.c(fn)
    return False

#=======================================================================================
def clickOnCaptcha():
    fn = "clickOnCaptcha"
    logger.o(fn)
    isCaptchaFound = False
    _captcha2 = Pattern("_captcha21.png").targetOffset(1,-52)
    captchaFileName = "" 
    if exists(_captcha2):
        if not checkCaptchaOrder():
            logger.c(fn) 
            return False
        captchaFileName = saveCaptcha()
        if captchaFileName == None:
           logger.c(fn) 
           return False 
        result = ocrCaptcha(captchaFileName)
        
        try:
            click(_captcha2)
        except:
            print "cant click on second captcha"
        isCaptchaFound = True
        logger.c(fn)
        return isOrderAccepted()
        
    _captcha2 = Pattern("_captcha22.png").targetOffset(7,-52) 
    if exists(_captcha2):
        if not checkCaptchaOrder():
            logger.c(fn) 
            return False
        #captchaFileName = saveCaptcha()
        try:
            click(_captcha2)
        except:
            logger.c(fn)
            return False
        isCaptchaFound = True
        logger.c(fn)
        return isOrderAccepted()
    
    logger.c(fn)
    return False

#=======================================================================================
def getOrderPic():
    fn = "getOrderPic"
    logger.o(fn)
    print "auto : "
    print auto
    if auto["orderPic"] == "diamonds":
        logger.c(fn)
        return Pattern("1678956270388.png").similar(0.96).targetOffset(-19,36)
    if auto["orderPic"] == "haltura":
        logger.c(fn)
        return Pattern("1678956311533.png").similar(0.95).targetOffset(-39,40)
    if auto["orderPic"] == "rabota":
        logger.c(fn)
        return Pattern("1678956673196.png").similar(0.95).targetOffset(-49,23)
    logger.c(fn)

#=======================================================================================
def getOrderFindWords(i=1):
    fn = "getOrderFindWord(i="+str(i)+")"
    logger.o(fn)
    
    _findWord = auto["findWords"]
    if i==1:
        _findWord = _findWord+" -макс"

    logger.c(fn)
    return _findWord    

#=======================================================================================
def getOrderFindWordsPic(i=1):
    fn = "getOrderFindWordPic"
    logger.o(fn)
    if auto["findWords"] == "работа":
        logger.c(fn)
        if i==1:
            return Pattern("rabota-max.png").similar(0.93).targetOffset(-150,50)
        if i==2:     
            return Pattern("find_word_rabota.png").similar(0.93).targetOffset(-140,50)
    if auto["findWords"] == "бонус":
        logger.c(fn)
        if i==1:
            return Pattern("bonus-max.png").similar(0.94).targetOffset(-150,50)
        if i==2:
            return Pattern("1679495102267.png").similar(0.92).targetOffset(-140,50)

    if auto["findWords"] == "халтура":
        logger.c(fn)
        if i==1:
            return Pattern("haltura-max.png").similar(0.94).targetOffset(-150,50)
        if i==2:    
            return Pattern("1679495289633.png").similar(0.93).targetOffset(-140,50)
    logger.c(fn)

#=======================================================================================
def getOrderCheckPic(i=1):
    fn = "getOrderCheckPic"
    logger.o(fn)
    if auto["orderPic"] == "diamonds":
        logger.c(fn)
        if i==1: return "1681414176624.png"
        if i==2: return "1681414253967.png"
        if i==3: return "1681414222097.png" 
    if auto["orderPic"] == "haltura":
        logger.c(fn)
        if i==1: return "1681414411208.png"
        if i==2: return "1681414462048.png"
        if i==3: return "1681414525789.png"
    if auto["orderPic"] == "rabota":
        logger.c(fn)
        if i==1: return "1681414622176.png"
        if i==2: return "1681414678789.png"
        if i==3: return "1681414637745.png"    
    logger.c(fn)

#=======================================================================================
def findWords():
    fn = "findWords"
    logger.o(fn)
    #type(Key.ENTER)
    sleep(1)
    for count in range(5):
        #Do.popup("count = "+str(count),1)
        if exists("btn-close-red.png",0):
            click()
        if exists("1682437218504.png",0):
            click()    
        index = 1
        #if count>1: index = 2
        _picFindWords = getOrderFindWordsPic(index)
        _findWords = getOrderFindWords(index)
        type(r"f",KeyModifier.CTRL)
        paste(unicd(_findWords))

        if exists(_picFindWords,1): 
            type(Key.ESC) 
            click(_picFindWords)
            logger.c(fn)
            return True
    
    logger.c(fn) 
    return False
    
#=======================================================================================
def getOrder():
    fn = "getOrder"
    logger.o(fn)
    isOrderTaken = False 
    _pic = getOrderPic()
    while not isOrderTaken:
        #scrollToOrder = taxi_base.scrollToOrderDown(_pic, region)
        status = getAutoStatus()
        if status == "empty reload":
            reloadOrders()
        else:    
            scrollToOrder = findWords()
        
            if scrollToOrder:
                #taxi_base.highlightPicture(_pic)
                #if taxi_base.ifExistsClick(_pic, region):
                #    isOrderTaken = clickOnCaptcha()
                isOrderTaken = clickOnCaptcha()
            else:
                reloadOrders()
                wait(5)
    logger.warning("    isOrderTaken = "+str(isOrderTaken))
    if isOrderTaken:
        auto["timeStart"] = time.time()
        logger.c(fn)
        return True
    else:    
        reloadOrders()
        wait(3)
    logger.c(fn)


#=======================================================================================
def setTimers():
    fn = "setTimers"
    logger.o(fn)
    status = auto["status"]
    orderAcceptedStart = auto.get("orderAcceptedStart", None)
    if status == "order accepted":
        if orderAcceptedStart == None:
            auto["orderAcceptedStart"] = time.time()
    else:
        auto.pop("orderAcceptedStart",None)
            
    emptyStart = auto.get("emptyStart", None)
    if status == "empty":
        if emptyStart == None:
            auto["emptyStart"] = time.time()
    else:
        auto.pop("emptyStart",None)
    logger.c(fn)

#=======================================================================================
def getAutoStatus():
    fn = "getAutoStatus"
    logger.o(fn)
    logger.warning( "    getAutoStatus: auto: " + str(auto)) 
    pStopPicture = "_DownPage.png"

    
    taxi_base.closeReclama()
    if exists("vzyati zakaz gray.png",0):
        auto['status'] = "empty reload"
        setTimers()
        logger.c(fn)
        return "empty reload"    
    if exists("vzyati zakaz blue.png",0):
        auto['status'] = "empty"
        setTimers()
        logger.c(fn)
        return "empty"


    if exists("_ZacazPrineat.png",0):
        auto['status'] = "order accepted"
        setTimers()
        logger.c(fn)
        return "order accepted"
    if exists("submit order.png",0):
        auto['status'] = "submit order"
        setTimers()
        logger.c(fn)
        return "submit order"
    if exists("1678655733157.png",0):
        auto['status'] = "close"
        setTimers()
        logger.c(fn)
        return "close"

    if exists("otdykhayet.png",0):
        auto['status'] = "resting"
        setTimers()
        logger.c(fn)
        return "resting"

    type(Key.PAGE_DOWN)

    if exists(pStopPicture,0):
        auto['status'] = "unknown"
        setTimers()
        loadAutoPage()
        logger.c(fn)
        return "unknown"

    logger.c(fn)
    return getAutoStatus()

#=======================================================================================
def checkAutoURL():
    fn = "checkAutoURL"
    logger.o(fn)
    result = True
    url = urlGarage+auto["id"]        
    mouseMove("1682630621223.png")   
    type(u"l",KeyModifier.CTRL)
    sleep(1)
    type(u"a",KeyModifier.CTRL)
    type(u"c",KeyModifier.CTRL)
    type(Key.ESC)
    clipboardURL = firefox.getClipboard()
    if url != clipboardURL:
        logger.warning("url="+url)
        logger.warning("clipboardURL="+clipboardURL)
        result = False

    logger.c(fn)
    return result


#=======================================================================================
def loadAutoPage():
    fn = "loadAutoPage"
    logger.o(fn)
    type(getTabNumber(auto["id"]),KeyModifier.CTRL)
    sleep(1)
    _pic = auto["pic"]
    key = auto["id"]
    print auto 
    while not exists(_pic,0): 
        goToURL(urlGarage+key)
        waitPageLoad()
        taxi_base.closeReclama()
    taxi_base.highlightPicture(_pic)    
    logger.c(fn)

#=======================================================================================
def main():
    fn = "main"
    #logger.o(fn)
    for key, val in dictTaxi.items(): 
        if val["id"] == "OCR":
            continue;
        
        global auto
        auto = val
        taxi_base.auto = auto
                
        if auto.get("status", "empty") == "order accepted":
            if time.time() - auto.get("orderAcceptedStart", time.time()-60*60*24) < 1*60:
                continue

            if time.time() - auto.get("lastEnterTime", time.time()-60*60*24) < 1*60:
                continue

        logger.warning("=========================================================")
        #print "orderAcceptedStart = "+time.strftime('%d.%m.%Y %H:%M', time.localtime(auto.get("orderAcceptedStart", time.time()-60*60*24))) 
        
        type(getTabNumber(auto["id"]),KeyModifier.CTRL)
        sleep(1)

        auto["lastEnterTime"] = time.time()
        if auto.get("status", "firs open") == "first open":
            loadAutoPage()

        if not checkAutoURL():
            loadAutoPage()
                          
        status = getAutoStatus()
        
        if status.find("empty") > -1:
            getOrder()
            taxi_ability_click.getAbilities(auto)

        #if status == "order accepted":
        #    taxi_ability_click.getAbilities(auto)
                
        if status == "submit order":
            click("submit order.png")

        if status == "close":
            click("1678655733157.png")

    #logger.c(fn)


logger.warning("test")
taxi_base.logger = logger
taxi_base.region = region
taxi_base.regionMargin = regionMargin
taxi_base.regionSideMenu = regionSideMenu
taxi_base.firefox = firefox
taxi_base.auto = auto

taxi_ability_click.taxi_base = taxi_base
taxi_captcha_answer_click.taxi_base = taxi_base

createTabs()

print captchaPath
openOCRTab()
while True:
    #logger.warning("=========================================================")
    main()    