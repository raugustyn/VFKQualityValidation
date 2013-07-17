# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Augustyn
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class VFKValidation:
    def __init__(self):
        pass

    def testHeader(self, header):
        pass

    def testData(self, data):
        pass

    def getMeasureText(self):
        return "undefined"

    def getUserMessage(self):
        return "undefined"

    def getName(self):
        return "undefined"

    def getDescription(self):
        return "undefined"


class ErrorType:
    Fatal = 0
    Critical = 1

ERROR_TYPE_CAPTIONS = ["fatální", "kritická"]

class UseType:
    def __init__(self, MGEO, ISKN, GP, NN):
        self.MGEO = MGEO
        self.ISKN = ISKN
        self.GP = GP
        self.NN = NN
        pass

    def __repr__(self):
        return "MGEO - " + ERROR_TYPE_CAPTIONS[self.MGEO] + " ISKN - " + ERROR_TYPE_CAPTIONS[self.ISKN] + " GP - " + ERROR_TYPE_CAPTIONS[self.GP] + " NN - " + ERROR_TYPE_CAPTIONS[self.NN]

class ValidationRequired(UseType):
    def __repr__(self):
        return "MGEO - " + str(self.MGEO) + " ISKN - " + str(self.ISKN) + " GP - " + str(self.GP) + " NN - " + str(self.NN)

class FieldTypeCheck(VFKValidation):
    def __init__(self, validationNumber, fieldCaption, fieldName, fieldDef, useType, validationRequired):
        self.validationNumber = validationNumber
        self.fieldCaption = fieldCaption
        self.fieldName = fieldName
        self.fieldName = fieldName
        self.fieldDef = fieldDef
        self.useType = useType
        self.validationRequired = validationRequired
        pass

    def testData(self, data):
        pass

    def tableRow(self, name, value):
        return "<tr><td>" + name + "</td><td>" + value + "</td></tr>\n"

    def getMeasureText(self):
        return "Kvalita dat určena v % jako: (0, pro počet chybných prvků >= 1;1) *100."

    def getUserMessage(self):
        return "Prvek v „výpis chybných záznamů ve formátu: Název bloku – název sloupce“ není typu " + self.fieldDef

    def getName(self):
        return 'Kontrola domény "' + self.fieldCaption + '"'

    def getDescription(self):
        return 'Prvky domény "' + self.fieldCaption + '" (' + ", ".join(self.fieldName) + ')'

    def toHTML(self):
        s = "<table>\n"
        s = s + self.tableRow("Označení kontroly", self.validationNumber)
        s = s + self.tableRow("Název", self.getName())
        s = s + self.tableRow("Popis kontroly", self.getDescription())
        s = s + self.tableRow("Hlášení pro uživatele", self.getUserMessage())
        s = s + self.tableRow("Typ chyby", str(self.useType))
        s = s + self.tableRow("Míra shody", self.getMeasureText())
        s = s + self.tableRow("Povinnost kontroly", str(self.validationRequired))
        s = s + "</table>\n"
        return s