import logging
import datetime
import time

urlGarage = "https://www.taxi-money.net/garage/"
captchaPath = "c:\\Sikulix_scripts\\git_sikulix_taximoney\\sikulix_taximoney\\captcha\\"
urlYaPictureSearch = r'https://yandex.ru/images/search?rpt=imageview'

auto = {}
dictTaxi = {"319558":
                {"id":"319558",
                "pic":"319558.png",
                "orderPic":"rabota",
                "findWords":"работа",
                "use diamonds reload": True},
            "264417":
                {"id":"264417",
                "pic":"264417.png",
                "orderPic":"diamonds",
                "findWords":"бонус",
                "use diamonds reload": True}}

firefox = App("c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
firefox.open()

fault_capcha_counter = 0

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(
        filename='log-taxi.log',#logname,
        format=FORMAT)
logger=logging.getLogger('')

loggetTabs = []


region = Region(450,113,691,547)
regionMargin = Region(1106,270,237,311)
regionSideMenu = Region(243,113,236,517)

#=======================================================================================
def debugStop():
    1/0

#=======================================================================================
def getLoggerTabsStr():
    t=''
    for i in range(len(loggetTabs)):
        t+='\t'
    return t

#=======================================================================================
def o(text):
    logger.warning(getLoggerTabsStr()+text+' {')
    loggetTabs.append(text)

#=======================================================================================
def c(text): 
    if len(loggetTabs) > 0:
        loggetTabs.pop()
    logger.warning(getLoggerTabsStr()+'} '+text)

#=======================================================================================
def highlightPicture(pPicture):
    try: 
        m = find(pPicture)
        # the red frame will grow 5 times
        for i in range(2):
            m.highlight(1)
            m = m.nearby(5)

        return True    
    except:
        return False

#=======================================================================================
def saveCaptcha():
    fn = "saveCaptcha"
    o(fn)    
    #return 
    rightClick(Pattern("1679759379856.png").targetOffset(-4,-111))
    click("1679759439561.png")    

    wait(Pattern("captchaFileName.png").targetOffset(40,-11),60)
    click()
    type(r"a",KeyModifier.CTRL)
    today = datetime.datetime.today()
    t = today.strftime("%Y-%m-%d-%H-%M-%S")    
    fileName = captchaPath+t+".jpg"
    paste(fileName)
    type(Key.ENTER)
    waitVanish("1679905123827.png",60)
    
    c(fn) 
    return(fileName)    

#=======================================================================================
def goToURL(url):
    fn = "goToURL"
    o(fn)
    type(u"l",KeyModifier.CTRL)
    type(u"a",KeyModifier.CTRL)
    paste(url)
    type(Key.ENTER)
    c(fn)

#=======================================================================================
def openOCRTab():
    fn = "openOCRTab"
    o(fn)
    if exists("1679776061740.png"):
        type(r't',KeyModifier.CTRL)
        goToURL(urlYaPictureSearch)
        wait("1679904976092.png",60)
        
    c(fn)


#=======================================================================================
def waitPageLoad():
    fn = "waitPageLoad"
    o(fn)
    _region = Region(5,0,1318,53)
    _region.wait("1678363257952.png",60)
    c(fn)

#=======================================================================================
def scrollToPicture(pPicture, pRegion, pStopPicture, pKey):
    fn = "scrollToPicture"
    o(fn)
    while not exists(pStopPicture,0):
        if not pRegion.exists(pPicture,0):
            #at = Mouse.at()
            ifExistsClick("1668111730485-2.png",regionMargin)
            firefox.focus()
            #Mouse.move(at) 
            type(pKey)
            type(pKey)
            type(pKey)
        else:
            highlightPicture(pPicture)
            c(fn)
            return True

    highlightPicture(pStopPicture)    
    c(fn)
    return False        

#=======================================================================================
def scrollToPictureUp(pPicture, pRegion):
    fn = "scrollToPictureUp"
    o(fn)
    _stopPic = "_UpPage.png"
    c(fn)
    return scrollToPicture(pPicture, pRegion, _stopPic, Key.UP) 

#=======================================================================================
def scrollToPictureDown(pPicture, pRegion):
    fn = "scrollToPictureDown"
    o(fn)
    _stopPic = "_DownPage.png"
    c(fn)
    return scrollToPicture(pPicture, pRegion, _stopPic, Key.DOWN) 

#=======================================================================================
def  scrollToOrderDown(pPicture, pRegion):
    fn = "scrollToOrderDown"
    o(fn)
    pStopPicture = "_DownPage.png"  
    while not exists(pStopPicture,0): 
        closeReclama()
        if not pRegion.exists(pPicture,0):
            if pRegion.exists("1678522428242.png",0):
                reloadOrders()
                
            type(Key.PAGE_DOWN)
        else:
            c(fn)
            return True
    #highlightPicture(pStopPicture) 
    c(fn)
    return False

#=======================================================================================
def goToPageEnd():
    fn = "goToPageEnd"
    o(fn)
    #at = Mouse.at()
    ifExistsClick("1668111730485.png",regionMargin)
    #Mouse.move(at)
    type(Key.END, KeyModifier.CTRL)
    c(fn)

#=======================================================================================
def goToPageHome():
    fn = "goToPageHome"
    o(fn)
    #at = Mouse.at()
    ifExistsClick("1668111730485-1.png",regionMargin)
    #Mouse.move(at)
    type(Key.HOME, KeyModifier.CTRL)
    c(fn)
    
#=======================================================================================
def goToPageUp():
    goToPageHome()
    
#=======================================================================================
def goToPageDown():
    goToPageEnd()

#=======================================================================================
def ifExistsClick(pPicture, pRegion=None):
    fn = "ifExistsClick"
    o(fn)
    #at = Mouse.at() 
    closeReclama()           
    #Mouse.move(at)
      
    #at = Mouse.at()
    if regionMargin.exists("1668111730485.png",0):
        try:
            regionMargin.click("1668111730485.png")
        except:
           print 'ifExistsClick: cant click on 1668111730485.png' 
    #Mouse.move(at)

    #at = Mouse.at()   
    try:
        if pRegion.exists(pPicture,0):
            #pRegion.click(pPicture)
            pRegion.click()
            #Mouse.move(at)
            c(fn)
            return True
    except: 
        if exists(pPicture,0):
            #click(pPicture)
            click()
            #Mouse.move(at)
            c(fn)
            return True
    
    c(fn)
    return False


#=======================================================================================
def closeReclama():
    fn = "closeReclama"
    o(fn)
    if exists("1678405736924.png",0):
        click()
    if exists("1678405891197.png",0):
        click()
    if exists(Pattern("1679127224332.png").similar(0.87),0):
        click()
    c(fn)

#=======================================================================================
def isOrderAccepted():
    fn = "isOrderAccepted"
    o(fn)

    status = getAutoStatus()
    if status.find("empty") > -1:
        c(fn)
        return False

    logging.basicConfig(
        filename='log-'+auto["id"]+'.log',#logname,
        format=FORMAT)

    logging.warning("1")
    
    logging.basicConfig(
        filename='log-taxi.log',#logname,
        format=FORMAT)
     
    c(fn)
    return True
    #if exists("vzyati zakaz blue.png",0):
    #    return False
    #if exists("vzyati zakaz gray.png",0):
    #    return False
    
    
    #_pic = "_ZacazPrineat.png"
    #if scrollToOrderDown(_pic, region):
    #    return True

    #return False

#=======================================================================================
def reloadOrders():
    fn="reloadOrders"
    o(fn)
    goToPageDown()
    logger.warning(fn+": auto['use diamonds reload'] = "+str(auto["use diamonds reload"]))
    if not auto["use diamonds reload"]:
        status = getAutoStatus()
        while not (status == "empty reload"):
            logger.warning(fn+":status = " + status)
            if time.time() - auto.get("emptyStart", time.time()) > 1.2*60:
                logger.warning(fn+":timer emptyStart = " + str(time.time() - auto.get("emptyStart", time.time())))
                loadAutoPage()
                c(fn)
                return
            wait(1)
            status = getAutoStatus()
            goToPageDown()
        
    if not ifExistsClick("load orders.png"):
        if not ifExistsClick("update.png"):
            loadAutoPage()
            c(fn)
            return

    wait(10)

    maxWait = 5 
    while isPageBusy() and maxWait >= 0:
        wait(1)
        maxWait -= 1

    if maxWait <= 0:
        loadAutoPage()
    c(fn)
    
#=======================================================================================
def isPageBusy():
    fn = "isPageBusy"
    o(fn)
    _pic = Pattern("loadOrdersIsBusy.png").similar(0.84) 
    if exists(_pic,1):
        logger.warning("    isPageBusy: True")
        if not highlightPicture(_pic):
            c(fn)
            return False
        
        c(fn)
        return True

    c(fn)
    return False

#=======================================================================================
def checkCaptchaOrder():
    fn = "checkCaptchaOrder"
    o(fn)
    _pic = getOrderCheckPic(1)
    if exists(_pic,0):
        c(fn)
        return True

    _pic = getOrderCheckPic(2)
    if exists(_pic,0):
        c(fn)
        return True
    c(fn)
    return False

#=======================================================================================
def clickOnCaptcha():
    fn = "clickOnCaptcha"
    o(fn)
    isCaptchaFound = False
    _captcha2 = Pattern("_captcha21.png").targetOffset(1,-52)
    captchaFileName = "" 
    if exists(_captcha2):
        if not checkCaptchaOrder():
            return False
        captchaFileName = saveCaptcha()
        try:
            click(_captcha2)
        except:
            c(fn) 
            return False
        isCaptchaFound = True
        c(fn)
        return isOrderAccepted()
        
    _captcha2 = Pattern("_captcha22.png").targetOffset(7,-52) 
    if exists(_captcha2):
        if not checkCaptchaOrder():
            return False
        captchaFileName = saveCaptcha()
        try:
            click(_captcha2)
        except:
            c(fn)
            return False
        isCaptchaFound = True
        c(fn)
        return isOrderAccepted()
    
    c(fn)
    return False

#=======================================================================================
def getOrderPic():
    fn = "getOrderPic"
    o(fn)
    print "auto : "
    print auto
    if auto["orderPic"] == "diamonds":
        c(fn)
        return Pattern("1678956270388.png").similar(0.96).targetOffset(-19,36)
    if auto["orderPic"] == "haltura":
        c(fn)
        return Pattern("1678956311533.png").similar(0.95).targetOffset(-39,40)
    if auto["orderPic"] == "rabota":
        c(fn)
        return Pattern("1678956673196.png").similar(0.95).targetOffset(-49,23)
    c(fn)


#=======================================================================================
def getOrderFindWordsPic():
    fn = "getOrderFindWordPic"
    o(fn)
    if auto["findWords"] == "работа":
        c(fn)
        return Pattern("find_word_rabota.png").similar(0.93).targetOffset(-140,50)
    if auto["findWords"] == "бонус":
        c(fn)
        return Pattern("1679495102267.png").similar(0.92).targetOffset(-140,50)

    if auto["findWords"] == "халтура":
        c(fn)
        return Pattern("1679495289633.png").similar(0.93).targetOffset(-140,50)
    c(fn)

#=======================================================================================
def getOrderCheckPic(i=1):
    fn = "getOrderCheckPic"
    o(fn)
    if auto["orderPic"] == "diamonds":
        c(fn)
        if i==1:
            return "1679146889005.png"
        if i==2:
            return "bonus blue.png"
    if auto["orderPic"] == "haltura":
        c(fn)
        if i==1:
            return "1679146785443.png"
    if auto["orderPic"] == "rabota":
        c(fn)
        if i==1:
            return "1679146710257.png"
        if i==2:
            return "rabota blue.png"
    c(fn)

#=======================================================================================
def findWords():
    fn = "findWords"
    o(fn)
    _picFindWords = getOrderFindWordsPic()
    _findWords = auto["findWords"]
    type(r"f",KeyModifier.CTRL)
    paste(unicd(_findWords))
    type(Key.ENTER)
    for i in range(5):
        if exists(_picFindWords,1):
            click()
            c(fn)
            return True
    
        type(Key.F3) 
    c(fn) 
    return False
    
#=======================================================================================
def getOrder():
    fn = "getOrder"
    o(fn)
    isOrderTaken = False 
    _pic = getOrderPic()
    while not isOrderTaken:
        #scrollToOrder = scrollToOrderDown(_pic, region)
        status = getAutoStatus()
        if status == "empty reload":
            reloadOrders()
        else:    
            scrollToOrder = findWords()
        
            if scrollToOrder:
                #highlightPicture(_pic)
                #if ifExistsClick(_pic, region):
                #    isOrderTaken = clickOnCaptcha()
                isOrderTaken = clickOnCaptcha()
            else:
                reloadOrders()
                wait(5)
    logger.warning("    isOrderTaken = "+str(isOrderTaken))
    if isOrderTaken:
        auto["timeStart"] = time.time()
        c(fn)
        return True
    else:    
        reloadOrders()
        wait(3)
    c(fn)


#=======================================================================================
def setTimers():
    fn = "setTimers"
    o(fn)
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
    c(fn)

#=======================================================================================
def getAutoStatus():
    fn = "getAutoStatus"
    o(fn)
    logger.warning( "    getAutoStatus: auto: " + str(auto)) 
    pStopPicture = "_DownPage.png"

    
    closeReclama()
    if exists("vzyati zakaz gray.png",0):
        auto['status'] = "empty reload"
        setTimers()
        c(fn)
        return "empty reload"    
    if exists("vzyati zakaz blue.png",0):
        auto['status'] = "empty"
        setTimers()
        c(fn)
        return "empty"


    if exists("_ZacazPrineat.png",0):
        auto['status'] = "order accepted"
        setTimers()
        c(fn)
        return "order accepted"
    if exists("submit order.png",0):
        auto['status'] = "submit order"
        setTimers()
        c(fn)
        return "submit order"
    if exists("1678655733157.png",0):
        auto['status'] = "close"
        setTimers()
        c(fn)
        return "close"

    if exists("otdykhayet.png",0):
        auto['status'] = "resting"
        setTimers()
        c(fn)
        return "resting"


    

    type(Key.PAGE_DOWN)

    if exists(pStopPicture,0):
        auto['status'] = "unknown"
        setTimers()
        loadAutoPage()
        c(fn)
        return "unknown"

    c(fn)
    return getAutoStatus()

#=======================================================================================
def loadAutoPage():
    fn = "loadAutoPage"
    o(fn)
    type("1",KeyModifier.CTRL)
    _pic = auto["pic"]
    key = auto["id"]
    print auto 
    while not exists(_pic,0): 
        goToURL(urlGarage+key)
        waitPageLoad()
        closeReclama()
    highlightPicture(_pic)    
    c(fn)

#=======================================================================================
def main():
    fn = "main"
    #o(fn)
    for key, val in dictTaxi.items(): 
        global auto
        auto = val

        if auto.get("status", "empty") == "order accepted":
            if time.time() - auto.get("orderAcceptedStart", time.time()-60*60*24) < 10*60:
                continue

            if time.time() - auto.get("lastEnterTime", time.time()-60*60*24) < 10*60:
                continue

        logger.warning("=========================================================")
        #print "orderAcceptedStart = "+time.strftime('%d.%m.%Y %H:%M', time.localtime(auto.get("orderAcceptedStart", time.time()-60*60*24))) 
        auto["lastEnterTime"] = time.time()
        loadAutoPage()
                   
        status = getAutoStatus()
        
        if status.find("empty") > -1:
            getOrder()
        
        if status == "submit order":
            click("submit order.png")

        if status == "close":
            click("1678655733157.png")

    #c(fn)


print captchaPath
openOCRTab()
while True:
    #logger.warning("=========================================================")
    main()    