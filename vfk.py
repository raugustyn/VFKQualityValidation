# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        vfk
# Purpose:
#
# Author:      Augustyn
#
# Created:     02.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
from EuradinImport import configRUIAN

ORIGIN_FIELD_NAME = 'origin'
EDGE_FIELD_NAME   = 'edge'

class TableData:
    def __init__(self, tableName, fieldNames, tableDefs):
        self.fieldNames = fieldNames
        self.fieldIndexes = []
        self.data = []
        for i in range(len(fieldNames)):
            self.fieldIndexes.append(-1)

        fieldDefs = tableDefs[tableName.lower()]
        i = 0
        for fieldDef in fieldDefs:
            j = 0
            for keyName in fieldNames:
                if fieldDef.fieldName == keyName:
                    self.fieldIndexes[j] = i
                j = j + 1
            i = i + 1
            pass
        pass

    def processRecord(self, record):
        dataToAdd = []
        for idx in self.fieldIndexes:
            dataToAdd.append(record[self.fieldIndexes[idx] + 1])
        self.data.append(dataToAdd)
        pass

class FieldDef:
    """ Záznam informací o field def v databázi """
    def __init__(self, fieldName, fieldType):
        fieldType = fieldType.replace("\n", "")

        self.fieldName = fieldName.lower()
        self.fieldType = fieldType[0:1]
        self.length = None
        self.precision = None

        if len(fieldType) > 1:
            precs = fieldType[1:].split(".")
            self.length = precs[0]
            if len(precs) == 2:
                self.precision = precs[1]
        pass

    def __repr__(self):
        r = self.fieldName + "," + self.fieldType
        if self.length <> None:
            r = r + ":" + str(self.length)
        if self.precision <> None:
            r = r + "." + str(self.precision)
        return "(" + r + ")"

class RowType:
    Header = 1
    Block = 2
    Data = 3
    NextLine = 4
    Error = 5
    Eof = 6
    # = Enum('Header', 'Block', 'Data', 'NextLine', 'Error')

def dummyOnStartFileEvent(session):
    session.recordNumber = 0
    pass

def xyToGML(x, y):
    return '<gml:MultiPoint srsName="urn:ogc:def:crs:EPSG::2065" srsDimension="2"><gml:pointMembers><gml:Point><gml:pos>' + \
             "-" + x + " " + "-" + y + '</gml:pos></gml:Point></gml:pointMembers></gml:MultiPoint>' # 750137.00 1029016.00

def posListToGML(posList):
    coordList = "-" + " -".join(posList)
    result = '''
        <gml:MultiCurve srsDimension="2" gml:id="DUL.429767" srsName="urn:ogc:def:crs:EPSG::2065">
            <gml:curveMember>
                <gml:LineString gml:id="DUL.429767.1">
                    <gml:posList>''' + coordList + '''</gml:posList>
                </gml:LineString>
            </gml:curveMember>
        </gml:MultiCurve>'''
    result2 = '''<gml:MultiSurface gml:id="HOB.539228" srsName="urn:ogc:def:crs:EPSG::2065" srsDimension="2">
            <gml:surfaceMember><gml:Polygon gml:id="HOB.539228.1"><gml:exterior><gml:LinearRing>
            <gml:posList>''' + coordList + '''</gml:posList>
            </gml:LinearRing></gml:exterior></gml:Polygon></gml:surfaceMember></gml:MultiSurface>'''
    result = result.replace("\n", "")
    result = result.replace("\t", "")
    return result

def dummyOnNextLineEvent(session):
    session.recordNumber = session.recordNumber + 1
    if 5000*math.floor(session.recordNumber/5000) == session.recordNumber:
        print session.recordNumber, u"řádků"
    pass

def dummyEofEvent(session):
    print session.recordNumber, u" řádků v souboru"
    pass

onStartFile = dummyOnStartFileEvent
onNextLine = dummyOnNextLineEvent
onEof = dummyEofEvent

class VFKReader:
    # SBP Table Defs
    SBP_TABLENAME  = 'sbp'
    HP_TABLENAME   = 'hp'
    SBP_ID_NAME    = 'ID'
    SBP_HID_NAME   = 'HP_ID'
    BP_ID_NAME     = 'BP_ID'

    # SOBR Table defs
    SOBR_TABLENAME = 'sobr'
    SOBR_ID_NAME   = 'ID'
    SOBR_X_NAME    = 'SOURADNICE_X'
    SOBR_Y_NAME    = 'SOURADNICE_Y'
    LINE_CONNECTOR = "¤".decode('iso-8859-2')


    """ Abstraktní třída reprezentující parser VFK souboru. """
    def __init__(self, aFileHandler, aFieldSeparator = ";"):
        self.fieldSeparator = aFieldSeparator
        self.fileHandler = aFileHandler
        self._tableDefs = None
        self.readFileHeader()
        self.__geometryTablesRead = False
        self.recordNumber = 0

        self._lastFieldCountTableName = None
        self._lastFieldCount = None
        pass

    def getTableDefs(self):
        if self._tableDefs == None:
            self._searchForTablesDefs()
        return self._tableDefs

    tableDefs = property(getTableDefs)

    def readFileHeader(self):
        self.fileHandler.seek(0)
        onStartFile(self)
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

        if lineType == RowType.Header:
            result = line.split(self.fieldSeparator)
            result[0] = result[0][2:]
            return [lineType, result]
        if lineType in [RowType.Data, RowType.Block]:
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

            if lineType == RowType.Eof:
                break
            elif lineType == RowType.Block:
                record = line.split(self.fieldSeparator)
                recordSectionName = record[0].lower()

                sectionName = recordSectionName[2:]
                sections.append(sectionName)
                self.tableDefs[sectionName] = []
                for fieldDef in record:
                    s = fieldDef.split(" ")
                    if len(s) == 2:
                        self.tableDefs[sectionName].append(FieldDef(s[0], s[1]))
                print "--- ", sectionName
            pass

        #print sections
        print "Field Types:", fieldTypes
        pass

    def readFileHeader(self):
        """ Načte ze souboru hlavičku. """
        pass

    def getRowType(self, dataStr):
        if dataStr == None or dataStr == "" or dataStr[0:2] == "&K":
            onEof(self)
            return RowType.Eof
        elif len(dataStr)<2 or dataStr[0:1] <> "&":
            return RowType.Error
        elif dataStr[1:2] == "H":
            return RowType.Header
        elif dataStr[1:2] == "B":
            return RowType.Block
        elif dataStr[1:2] == "D":
            return RowType.Data
        else:
            return RowType.NextLine


    def getTableNames(self):
        """ Vrací seznam tabulek obsažených v souboru VFK. """
        return self.tableDefs.keys()

    def getFieldCount(self, tableName):
        if self.tableDefs == {}:
            return -1
        else:
            if self._lastFieldCountTableName <> tableName:
                tableDef = self.tableDefs[tableName]
                self._lastFieldCountTableName = tableName
                self._lastFieldCount = len(tableDef)

            return self._lastFieldCount

    def getFieldTypes(self):
        """ Vrací seznam použitých typů v souboru VFK. """
        result = []
        for tableName in self.tableDefs:
            fieldDefs = self.tableDefs[tableName]
            for fieldDef in fieldDefs:
                if not fieldDef.fieldType in result:
                    result.append(fieldDef.fieldType)
        return result

    def getSpatialTables(self):
        result = []
        for tableName in self.tableDefs:
            fieldDefs = self.tableDefs[tableName]
            for fieldDef in fieldDefs:
                if fieldDef.fieldName.upper().find("SOURADNICE") == 0:
                    result.append(tableName)
                    break
        return result

    def readLine(self):
        """ Vrací další rádek ze vstupního souboru. """
        onNextLine(self)
        result = self.fileHandler.readline()
        result = result.decode('iso-8859-2')
        result = result.replace('"', "")
        return result

    def rewindToStart(self):
        self.fileHandler.seek(0)
        pass

    def importVFKDatabase(self, dbHandler):
        self.readFileHeader()
        recordCount = 0
        while True:
            recordData = self.read()
            lineType = recordData[0]

            if lineType == RowType.Eof:
                break
            elif lineType == RowType.Data:
                record = recordData[1]
                tableName = record[0].lower()
                recordCount = recordCount + 1
                if tableName in self.tableDefs:
                    fields = self.tableDefs[tableName]
                    if len(fields) + 1 == len(record):
                        data = {}
                        recordIndex = 1;
                        x = None
                        y = None
                        for fieldDef in fields:
                            if fieldDef.fieldType == "D" and record[recordIndex] == "":
                                pass
                            elif fieldDef.fieldType == "N" and record[recordIndex] == "":
                                pass
                            else:
                                data[fieldDef.fieldName] = record[recordIndex]

                            if fieldDef.fieldName == "souradnice_x":
                                x = record[recordIndex]
                            if fieldDef.fieldName == "souradnice_y":
                                y = record[recordIndex]

                            recordIndex = recordIndex + 1
                            pass # for iteration

                        if x <> None and y <> None:
                            data[ORIGIN_FIELD_NAME] = xyToGML(x, y)

                        if tableName == VFKReader.HP_TABLENAME:
                            data[EDGE_FIELD_NAME] = posListToGML(self.coordFromHPID(record[1]))
                            pass

                        dbHandler.writeRowToTable(tableName, data)
                    else:
                        print "Error:", len(fields) + 1, "<>", len(record)
            pass

        print recordCount, "records - End of file"

    def createVFKDatabase(self, dbHandler):
        print "Creating VFK Database"

        for tableName in self.tableDefs:
            ruian_def = {
                "skipNamespacePrefix" : "true", # remove namespace prefix obi, oki etc
                "fields": {    }
            }

            fields = ruian_def["fields"]
            fieldDefs = self.tableDefs[tableName]
            hasGeometry = False
            for fieldDef in fieldDefs:
                if fieldDef.fieldName.lower().find("souradnice") == 0:
                    hasGeometry = True
                if fieldDef.fieldType == "N":
                    if fieldDef.precision == None:
                        fields[fieldDef.fieldName] = { "type" : "Long"}
                    else:
                        fields[fieldDef.fieldName] = { "type" : "Double"}
                elif fieldDef.fieldType == "T":
                     fields[fieldDef.fieldName] = { "type" : "String"}
                elif fieldDef.fieldType == "D":
                     fields[fieldDef.fieldName] = { "type" : "DateTime"}
                else:
                    print "Error, unknown field type " + fieldDef.fieldType
                pass

            if hasGeometry:
                fields[ORIGIN_FIELD_NAME] = {"type":"MultiPointPropertyType" }
                print tableName, "is spatial table"

            if tableName == VFKReader.HP_TABLENAME:
                fields[EDGE_FIELD_NAME] = {"type":"MultiCurvePropertyType" }
                print tableName, "is spatial table"

            configRUIAN.tableDef[tableName] = ruian_def
            dbHandler.createTable(tableName, True)
        pass

    def coordFromHPID(self, hpId):
        self.readGeometryTables()
        bp_ids = []
        for sbpRec in self.sbpTable:
            if sbpRec[1] == hpId:
                bp_ids.append(sbpRec[2])

        if bp_ids == []:
            return []
        else:
            result = []
            for sobrRec in self.sobrTable:
                if sobrRec[0] in bp_ids:
                    result.append(sobrRec[1])
                    result.append(sobrRec[2])
            return result
        pass



    def readGeometryTables(self):
        if not self.__geometryTablesRead:
            self.sbpTable = []
            self.sobrTable = []

            tableInfos = {
             "par": TableData("par", ["id"], self.tableDefs)
            }

            fieldDefs = self.tableDefs[VFKReader.SBP_TABLENAME]
            i = 0
            for fieldDef in fieldDefs:
                if fieldDef.fieldName == VFKReader.SBP_ID_NAME.lower():
                    id_idx = i + 1
                if fieldDef.fieldName == VFKReader.SBP_HID_NAME.lower():
                    hp_id_idx = i + 1
                if fieldDef.fieldName == VFKReader.BP_ID_NAME.lower():
                    bp_id_idx = i + 1
                i = i + 1
                pass

            fieldDefs = self.tableDefs[VFKReader.SOBR_TABLENAME]
            i = 0
            for fieldDef in fieldDefs:
                if fieldDef.fieldName == VFKReader.SOBR_ID_NAME.lower():
                    sobr_id_idx = i + 1
                if fieldDef.fieldName == VFKReader.SOBR_X_NAME.lower():
                    sobr_x_idx = i + 1
                if fieldDef.fieldName == VFKReader.SOBR_Y_NAME.lower():
                    sobr_y_idx = i + 1
                i = i + 1
                pass


            self.rewindToStart()
            while True:
                recordData = self.read()
                lineType = recordData[0]

                if lineType == RowType.Eof:
                    break
                elif lineType == RowType.Data:
                    record = recordData[1]
                    tableName = record[0].lower()
                    if tableName == VFKReader.SBP_TABLENAME:
                        self.sbpTable.append([record[id_idx], record[hp_id_idx], record[bp_id_idx]])
                    elif tableName == VFKReader.SOBR_TABLENAME:
                        self.sobrTable.append([record[sobr_id_idx], record[sobr_x_idx], record[sobr_y_idx]])

                    for infoTableName in tableInfos:
                        if tableName == infoTableName:
                            tableInfos[infoTableName].processRecord(record)

            self.__geometryTablesRead = True


            print "sbpTable:", len(self.sbpTable)
            print "sobrTable:", len(self.sobrTable)
            print self.coordFromHPID("3876520211")
        pass
