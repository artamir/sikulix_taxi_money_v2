import datetime
print datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
#----------------------------------------------------
m = exists("_ZacazPrineat.png", 0)

if m:
    r = Region(m.getX()-125, m.getY()-10,140,20)
    r.highlight(1)
    print(r.text())
 
#----------------------------------------------------

#----------------------------------------------------
m = exists("1682581574284.png", 0)

if m:
    r = Region(m.getX()-125, m.getY()-10,140,20)
    r.highlight(1)
    print(r.text())
 
#----------------------------------------------------

#----------------------------------------------------
listm = findAll("1682623392722.png")
for m in listm:
    r = Region(m.getX()+20, m.getY(),70,20)
    r.highlight(1)
    print(r.text())
 
#----------------------------------------------------
