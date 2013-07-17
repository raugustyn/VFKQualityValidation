# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        VFKValidation
# Purpose:     Hlavn� bussiness logic validace
#
# Author:      Radek August�n
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     V�GTK, v.v.i
#-------------------------------------------------------------------------------
import Validation, VFKQualityDictionary

def main():
    s = """<html>
    <head>
        <link rel="stylesheet" href="geoext.css" type="text/css" />
        <link rel="stylesheet" href="pygments.css" type="text/css" />
    </head>
    <body>\n"""
    for categoryName in VFKQualityDictionary.validationDictionary:
        s = s + "<h1>" + categoryName + "</h1>\n"
        for validation in VFKQualityDictionary.validationDictionary[categoryName]:
            s = s + validation.toHTML() + "<br/>\n"
        s = s + "</body></html>\n"
    f = open("list.html", "w")
    f.write(s)
    f.close()
    print "Soubor list.html je vytvo�en."
    pass

if __name__ == '__main__':
    main()
