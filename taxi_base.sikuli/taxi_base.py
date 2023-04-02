# -*- coding: utf-8 -*-
from sikuli import *

logger = None
region = None
regionMargin = None
regionSideMenu = None
firefox = None

#=======================================================================================
def setLogger(pLogger):
    logger = pLogger

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
def scrollToPicture(pPicture, pRegion, pStopPicture, pKey):
    fn = "scrollToPicture"
    logger.o(fn)
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
            logger.c(fn)
            return True

    highlightPicture(pStopPicture)    
    logger.c(fn)
    return False        

#=======================================================================================
def scrollToPictureUp(pPicture, pRegion):
    fn = "scrollToPictureUp"
    logger.o(fn)
    _stopPic = "_UpPage.png"
    logger.c(fn)
    return scrollToPicture(pPicture, pRegion, _stopPic, Key.UP) 

#=======================================================================================
def scrollToPictureDown(pPicture, pRegion):
    fn = "scrollToPictureDown"
    logger.o(fn)
    _stopPic = "_DownPage.png"
    logger.c(fn)
    return scrollToPicture(pPicture, pRegion, _stopPic, Key.DOWN) 

#=======================================================================================
def  scrollToOrderDown(pPicture, pRegion):
    fn = "scrollToOrderDown"
    logger.o(fn)
    pStopPicture = "_DownPage.png"  
    while not exists(pStopPicture,0): 
        closeReclama()
        if not pRegion.exists(pPicture,0):
            if pRegion.exists("1678522428242.png",0):
                reloadOrders()
                
            type(Key.PAGE_DOWN)
        else:
            logger.c(fn)
            return True
    #highlightPicture(pStopPicture) 
    logger.c(fn)
    return False

#=======================================================================================
def goToPageEnd():
    fn = "goToPageEnd"
    logger.o(fn)
    #at = Mouse.at()
    ifExistsClick("1668111730485.png",regionMargin)
    #Mouse.move(at)
    type(Key.END, KeyModifier.CTRL)
    logger.c(fn)

#=======================================================================================
def goToPageHome():
    fn = "goToPageHome"
    logger.o(fn)
    #at = Mouse.at()
    ifExistsClick("1668111730485-1.png",regionMargin)
    #Mouse.move(at)
    type(Key.HOME, KeyModifier.CTRL)
    logger.c(fn)
    
#=======================================================================================
def goToPageUp():
    goToPageHome()
    
#=======================================================================================
def goToPageDown():
    goToPageEnd()

#=======================================================================================
def ifExistsClick(pPicture, pRegion=None):
    fn = "ifExistsClick"
    logger.o(fn)
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
            logger.c(fn)
            return True
    except: 
        if exists(pPicture,0):
            #click(pPicture)
            click()
            #Mouse.move(at)
            logger.c(fn)
            return True
    
    logger.c(fn)
    return False


#=======================================================================================
def closeReclama():
    fn = "closeReclama"
    logger.o(fn)
    if exists("1678405736924.png",0):
        click()
    if exists("1678405891197.png",0):
        click()
    if exists(Pattern("1679127224332.png").similar(0.87),0):
        click()
    logger.c(fn)
