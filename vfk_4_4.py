# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        vfk_4_4
# Purpose:
#
# Author:      Augustyn
#
# Created:     02.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import vfk

class VFKReader(vfk.VFKReader):
    #def __init__(self, aFileHandler, aFieldSeparator = ";"):
    #    VFKReader.__init__(aFileHandler, aFieldSeparator)
    #    pass
    LINE_CONNECTOR = "¤".decode('iso-8859-2')

    def readFileHeader(self):
        self.fileHandler.seek(0)
        vfk.onStartFile(self)
        while True:
            lineStr = self.readLine()
            if lineStr[:2] <> "&H":
                break

        # @TODO Zbytecne se nacte dalsi radek
        pass

    def read(self):
        """ Čte řádek ze vstupního souboru a rozdělí ho na záznamy. Kontroluje,
            jestli se jedná o data nebo hlavičku dat. Jestliže je počet záznamů
            dat neúplný, načte další rádek.
        """
        line = self.readLine()
        if line.find(VFKReader.LINE_CONNECTOR) <> -1:
            pass
        while line[len(line)-1:] == VFKReader.LINE_CONNECTOR:
            line = line[:len(line) - 1] + self.readLine()

        lineType = self.getRowType(line)
        line = line.replace("\n", "")

        if lineType == vfk.RowType.Header:
            result = line.split(self.fieldSeparator)
            result[0] = result[0][2:]
            return [lineType, result]
        if lineType in [vfk.RowType.Data, vfk.RowType.Block]:
            result = line.split(self.fieldSeparator)
            result[0] = result[0][2:]
            return [lineType, result]
        else:
            return [lineType]

    def _searchForTablesDefs(self):
        self.readFileHeader()
        print "Reading records"
        self.tableDefs = {}
        sections = []
        fieldTypes = []
        sectionName = None
        while True:
            line = self.readLine()
            lineType = self.getRowType(line)

            if lineType == vfk.RowType.Eof:
                break
            elif lineType == vfk.RowType.Block:
                record = line.split(self.fieldSeparator)
                recordSectionName = record[0].lower()

                sectionName = recordSectionName[2:]
                sections.append(sectionName)
                self.tableDefs[sectionName] = []
                for fieldDef in record:
                    s = fieldDef.split(" ")
                    if len(s) == 2:
                        self.tableDefs[sectionName].append(vfk.FieldDef(s[0], s[1]))
                print "--- ", sectionName
            pass

        #print sections
        print "Field Types:", fieldTypes
        pass

