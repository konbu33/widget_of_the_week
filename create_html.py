from glob import glob
from pprint import pprint
import re

dirName = 'Flutter Widget of the Week'
# dirName = 'New to Figma Get started with Figma for beginners tutorials'

def getWidgetList():
    widgetList = glob(dirName + "/*")

    return widgetList

widgetList = getWidgetList()
# pprint(widgetList)

def htmlFileList():
    htmlFileName = dirName + ".html"

    with open(htmlFileName, 'w') as f:
        f.write('<html>\n')
        f.write('   <head>\n')
        f.write('   </head>\n')
        f.write('   <body>\n')

        for widget in widgetList:
            htmlFileList = (glob(widget + "/*"))
            sortedHtmlFileList = sorted(htmlFileList)

            widgetName = (re.split('/',sortedHtmlFileList[0]))[1]
            f.write('       <div>\n')
            # f.write('           <h1 style="color:red; font-size:20px;">' + widgetName + '</h1>\n')
            f.write('           <a href="" style="display:block;">' + widgetName + '</a>\n')

            shlink = (0.5 * 0.5 * 0.5)
            width  = int(1320 * shlink)
            height =  int(820 * shlink)
            print('width : ', width, 'height : ', height)

            for imgSrc in sortedHtmlFileList:
                f.write('               <img src="' + imgSrc + '" height=' + str(height) + ',  width=' + str(width) + ' />\n')

            f.write('       </div>\n')

        f.write('   </body>\n')
        f.write('</html>\n')


htmlFileList()

