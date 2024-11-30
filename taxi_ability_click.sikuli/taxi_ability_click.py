# -*- coding: utf-8 -*-
from sikuli import *

taxi_base = None

def getAbilityPic(ability):
    if ability == "expensive order":
        return Pattern("expensive order pic.png").similar(0.95)

    if ability == "fast order":
        return Pattern("fast order pic-2.png").similar(0.94)

    if ability == "stimul1":
        return Pattern("1731903892684.png").similar(0.91)
    if ability == "medium nitro":
        return Pattern("1732786567149.png").similar(0.91)

#=======================================================================================
def getAbilities(auto):
    abilities = auto.get("abilities", None)
    if not abilities == None:
        for ability in abilities:
            abilityPic = getAbilityPic(ability)            
            taxi_base.goToPageUp()
            taxi_base.scrollToPictureDown(abilityPic, taxi_base.region)
            taxi_base.ifExistsClick(abilityPic)
