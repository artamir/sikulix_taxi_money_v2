import logging

logging.disable(level=logging.CRITICAL)
FORMAT='%(asctime)-15s %(message)s'


logger=logging.getLogger('')

loggetTabs = []

#=======================================================================================
def setBaseConfig(logname='log-taxi.log', logformat=''):
    if logformat == '':
        logformat = FORMAT
    logging.basicConfig(
        filename=logname,
        format=logformat,
        level=logging.INFO)

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
def c(text, pReturn = ''): 
    if len(loggetTabs) > 0:
        loggetTabs.pop()

    textReturn = ""
    if pReturn != '':
        textReturn = ":: return = " + str(pReturn)
    logger.warning(getLoggerTabsStr()+'} '+text+textReturn)
    return pReturn

def warning(pText):
    logger.warning(pText)
    
def info(pText):
    logger.info(pText)    