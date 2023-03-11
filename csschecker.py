#!/usr/bin/env python3

# check html file for used class names
htmlClasses = []
cssClasses = []

html = open("account-screen.html", "r")
css = open("screen.css", "r")
newCss = open("screen-new.css", "w")

stringToWrite = ""

for y in html:
    if (y.find("class=")>0):
        tmpy = y[y.find("class=")+7:]
        tmpy = tmpy[:tmpy.find("\"")]
        htmlClasses.append(tmpy)

html.close()

for x in css:
    #print(type(x))
    if (x.startswith(".")):
        #print(x)
        if (x.endswith("{\n")):

            tmpx = x.lstrip(".")
            tmpx = tmpx.rstrip(" {\n")
            
            #cssClasses.append(tmpx)
            if not tmpx in htmlClasses:
                print(tmpx + " NOT IN HTML")
                stringToWrite = "Not used"
    
    stringToWrite = stringToWrite + x
    newCss.writelines([stringToWrite])
    stringToWrite=""
                


css.close()
newCss.close()

print("Classes:")
#print(htmlClasses)
#print(cssClasses)

