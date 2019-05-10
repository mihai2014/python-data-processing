import os
import re
from names import names

string = ""

def traverse_dir(dir):

    global string
    string += '<ul>\n'

    for item in os.listdir(dir):
    #for item in filterList(os.listdir(dir)):

        #exclude settings folder '.' at the beggining
        avoid = re.findall("^\.(.*)$",item)
        if( avoid == []):

            fullpath = os.path.join(dir, item)

            if os.path.isdir(fullpath):
                string += ('<li>%s</li>\n' % item)
            else:

                #only *.html and *.ipynb
                html = re.findall("^(.*).html$",item)
                ipynb = re.findall("^(.*).ipynb$",item)

                #only html and ipynb files
                if(html != [] or ipynb != []):
                    #startStr = PWD + "/blog/templates/blog/data"
                    startStr = "https://nbviewer.jupyter.org/github/mihai2014/python-data-processing/blob/master"
                    #remove startStr
                    fullpath = fullpath[1:len(fullpath)]

                    #rename
                    try:
                        item = names[item]
                    except:
                        pass

                    relativePath = startStr + fullpath
                    string += ('<li><a href="%s">%s</a></li>\n' % (relativePath,item))


            if os.path.isdir(fullpath):
                if os.listdir(fullpath) != []:
                    traverse_dir(fullpath)

    string += '</ul>\n'

traverse_dir('.')
print(string)

#ttps://nbviewer.jupyter.org/github/mihai2014/python-data-processing/blob/master
