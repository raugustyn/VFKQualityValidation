# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        VFKReader
# Purpose:
#
# Author:      Augustyn
#
# Created:     02.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import vfk
from EuradinImport import configRUIAN, textFile_DBHandler, postGIS_DBHandler

##class _VFKReaderHandler:
##    def __init__(self, aFileHandler, aFieldSeparator = ";"):
##        self.fieldSeparator = aFieldSeparator
##        self.fileHandler = aFileHandler


def VFKReader(fileName, aFieldSeparator = ";"):
    f = open(fileName, "r")
    versionLine = f.readline()
    #if versionLine.find("&HVERZE;") == 0:
    #    versionString = versionLine.split('"')[1]  # &HVERZE;"4.4"
        #if versionString == "4.4":
    return vfk.VFKReader(f, aFieldSeparator)

    return None

SAMPLE_DATA = [
 "..\\SampleData\\krasice_4_3.vfk",
 "..\\SampleData\\Jinocany_anonym.vfk",
 "..\\SampleData\\Zemek\\Od_Podhurska_04_04_2013\\brozankyPodh.vfk",
 "..\\SampleData\\Zemek\\Od_Podhurska_04_04_2013\\melnikPodh.vfk",
 "..\\SampleData\\Zemek\\Od_Doubek_12_2012\\File1.vfk",
 "..\\SampleData\\Zemek\\Od_Doubek_12_2012\\File2.vfk",
 "..\\SampleData\\Zemek\\Od_Doubek_12_2012\\File3.vfk",
 "..\\SampleData\\Zemek\\Od_Doubek_12_2012\\File4.vfk"
]

def main():
    reader = VFKReader(SAMPLE_DATA[2]) # 5

    writeToDB = False
    if not writeToDB:
        handler = textFile_DBHandler.Handler("..\\FileDB\\", ";")
    else:
        #handler = postGIS_DBHandler.Handler("dbname=VFKImport host=localhost port=5432 user=postgres password=ahoj","public")
        handler = postGIS_DBHandler.Handler("dbname=VFKImport host=localhost port=5432 user=postgres password=ahoj","public")

    print reader.tableDefs
    print "---- Table Names ----"
    print reader.getTableNames()
    print "Field types:", reader.getFieldTypes()
    print "Spatial tables:", reader.getSpatialTables()

    reader.readGeometryTables()
    reader.createVFKDatabase(handler)
    reader.importVFKDatabase(handler)


if __name__ == '__main__':
    main()
