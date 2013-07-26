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

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

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
<body>\n"""

s = s + '<div class="header"><h1 class="logo"><a href="dd">GeoExt</a></h1></div>'
s = s + '<div class="document">'
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

s = s + "</div>"
s = s + "</body></html>\n"
##f = open("..\\HTML\\list.html", "w")
##f.write(s)
##f.close()
##print "Soubor ..\\HTML\\list.html je vytvořen."
print s
