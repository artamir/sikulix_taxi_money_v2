import logging

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(
        filename='log-taxi.log',#logname,
        format=FORMAT)

logger=logging.getLogger('')

loggetTabs = []

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

def warning(pText):
    logger.warning(pText)