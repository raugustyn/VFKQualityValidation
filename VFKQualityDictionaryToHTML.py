# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        VFKQualityDictionaryToHTML
# Purpose:     Testování úplnosti databáze testů
#
# Author:      Radek Augustýn
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     VÚGTK, v.v.i
#-------------------------------------------------------------------------------
import Validation, VFKQualityDictionary

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

htmlStart = """<html>
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

<style>
    body {
        font-family: "Lucida Grande", "Lucida Sans Unicode", "Geneva", "Verdana", sans-serif;
    }

    h1, h2, h3 {
        color: #385f95;
    }

    table {
        background-color:rgb(247, 247, 247);
        padding: 0 0 0 0;
        margin:0 0 0 0;
    }

    td {
        border-style:solid;
        border-color:#86989b;
        border-width:1px;
        font-size:0.9em;
    }

    th {
        border-style:solid;
        border-color:#86989b;
        border-width:1px;
        background-color:rgb(175, 193, 196);
        padding:0 0 0 0;
        margin:0 0 0 0;
        text-align:right;
        color:white
        font-size:0.9em;
    }

    .document {
        border-color:#eeeeee;
        border-style:solid;
        border-width:1px;
        margin-right:80px;
        margin-left:80px;
    }

    div.header {
        position: relative;
        overflow: hidden;
        height: 120px;
        background: #97b7e1 url(./header-bg.png) 0 0 repeat-x;
    }

.logo {
    padding: 0;
}
.logo a {
    float: left;
    width: 300px;
    height: 120px;
    overflow: hidden;
    text-indent: -9999em;
    background: url(img/geoext-logo.png) no-repeat;
    color:white;
}

</style>

</head>
<body>\n
    <div class="header">
        <h1 class="logo"><a href="dd">GeoExt</a></h1>
    </div>
    <div class="document">
"""

htmlEnd = "</div></body></html>\n"

def saveStrToFile(s, fileName):
    f = open(fileName, "w")
    f.write(s)
    f.close()
    print "Soubor ", fileName, "vytvořen."

def getTreeHTML():
    s = ""
    s = s + '<ul id="browser" class="filetree">'
    for categoryName in VFKQualityDictionary.validationDictionary:
        s = s + '<li><span class="folder">' + categoryName + '</span><ul>'
        for validation in VFKQualityDictionary.validationDictionary[categoryName]:
            s = s + '<li><span class="file">' + validation.validationNumber + " " + validation.getName() + '</span></li>'
        s = s + "</ul></li>\n"

    s = s + "</div>"

    return s

def getListHTML():
    s = ""
    for categoryName in sorted(VFKQualityDictionary.validationDictionary.iterkeys()):
    #for categoryName in VFKQualityDictionary.validationDictionary:
        s = s + "<h1>" + categoryName + "</h1>\n"
        for validation in VFKQualityDictionary.validationDictionary[categoryName]:
            s = s + validation.toHTML() + "<br/>\n"

    s = s + "<br>"

    return s



outputDir = "..\\03_Output\\"
saveStrToFile(htmlStart + getListHTML() + htmlEnd, outputDir + "list.html")

outputDir = "..\\03_Output\\"
saveStrToFile(htmlStart + getTreeHTML() + htmlEnd, outputDir + "tree.html")

