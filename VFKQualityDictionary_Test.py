# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        VFKQualityDictionary_Test
# Purpose:     Testování úplnosti databáze testů
#
# Author:      Radek Augustýn
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     VÚGTK, v.v.i
#-------------------------------------------------------------------------------
import Validation, VFKQualityDictionary

def main():
    s = """<html>
    <head>

    <link rel="stylesheet" href="http://jquery.bassistance.de/treeview/jquery.treeview.css" />
	<script src="http://jquery.bassistance.de/treeview/lib/jquery.js" type="text/javascript"></script>
	<script src="http://jquery.bassistance.de/treeview/lib/jquery.cookie.js" type="text/javascript"></script>
	<script src="http://jquery.bassistance.de/treeview/jquery.treeview.js" type="text/javascript"></script>

    <script type="text/javascript" >
        $(document).ready(function(){
            $("#browser").treeview();
        });
    </script>

    </head>
    <body>\n"""

    s = s + '<ul id="browser" class="filetree">'
    for categoryName in VFKQualityDictionary.validationDictionary:
        s = s + '<li><span class="folder">' + categoryName + '</span><ul>'
        for validation in VFKQualityDictionary.validationDictionary[categoryName]:
            s = s + '<li><span class="file">' + validation.validationNumber + " " + validation.getName() + '</span></li>'
        s = s + "</ul></li>\n"

    for categoryName in VFKQualityDictionary.validationDictionary:
        s = s + "<h1>" + categoryName + "</h1>\n"
        for validation in VFKQualityDictionary.validationDictionary[categoryName]:
            s = s + validation.toHTML() + "<br/>\n"

    s = s + "<br>"

    s = s + "</body></html>\n"
    f = open("..\\HTML\\list.html", "w")
    f.write(s)
    f.close()
    print "Soubor ..\\HTML\\list.html je vytvořen."
    pass

if __name__ == '__main__':
    main()
