# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        Validation
# Purpose:     Knihovna pro implementaci kontrol VFK podle certifikované metodiky
#
# Author:      Radek Augustýn
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     VÚGTK, v.v.i
#-------------------------------------------------------------------------------

class VFKValidation:
    """
    Abstraktní třída definující kontrolu
    """

    def testHeader(self, header):
        pass

    def testData(self, data):
        pass

    def getMeasureText(self):
        """ Vrací text "Míra shody" do tabulky reportů, viz metodika, kap 7.1  """
        return "undefined"

    def getUserMessage(self):
        """ Vrací text "Hlášení pro uživatele" do tabulky reportů, viz metodika, kap 7.1  """
        return "undefined"

    def getName(self):
        """ Vrací text "Název" do tabulky reportů, viz metodika, kap 7.1  """
        return "undefined"

    def getDescription(self):
        """ Vrací text "Popis kontroly" do tabulky reportů, viz metodika, kap 7.1  """
        return "undefined"


class ErrorType:
    """ Číselník "Typu chyby", viz metodika, kap 7.1 """
    Fatal    = 0
    Critical = 1
    ERROR_TYPE_CAPTIONS = ["fatální", "kritická"]

class UseType:
    """ Záznam pro uložení stejných hodnot pro MGEO, ISKN, GP a NN """
    def __init__(self, MGEO, ISKN, GP, NN):
        self.MGEO = MGEO
        self.ISKN = ISKN
        self.GP = GP
        self.NN = NN
        pass

    def __repr__(self):
        return "MGEO - " + ErrorType.ERROR_TYPE_CAPTIONS[self.MGEO] + \
               " ISKN - " + ErrorType.ERROR_TYPE_CAPTIONS[self.ISKN] + \
               " GP - " + ErrorType.ERROR_TYPE_CAPTIONS[self.GP] + \
               " NN - " + ErrorType.ERROR_TYPE_CAPTIONS[self.NN]

class ValidationRequired(UseType):
    def __repr__(self):
        return "MGEO - " + str(self.MGEO) + " ISKN - " + str(self.ISKN) + " GP - " + str(self.GP) + " NN - " + str(self.NN)

class FieldTypeCheck(VFKValidation):
    """ Třída implemntující kontrolu typu sloupce a hodnot v něm uložených
    """

    def __init__(self, validationNumber, fieldCaption, fieldName, fieldDef, useType, validationRequired):
        """ Uložení parametrů """
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
        """ Vrací formátovaný řádek výstupní tabulky """
        return "<tr><td>" + name + "</td><td>" + value + "</td></tr>\n"

    def getMeasureText(self):
        """ Vrací text "Míra shody" do tabulky reportů, viz metodika, kap 7.1  """
        return "Kvalita dat určena v % jako: (0, pro počet chybných prvků >= 1;1) *100."

    def getUserMessage(self):
        """ Vrací text "Hlášení pro uživatele" do tabulky reportů, viz metodika, kap 7.1  """
        return "Prvek v „výpis chybných záznamů ve formátu: Název bloku – název sloupce“ není typu " + self.fieldDef

    def getName(self):
        """ Vrací text "Název" do tabulky reportů, viz metodika, kap 7.1  """
        return 'Kontrola domény "' + self.fieldCaption + '"'

    def getDescription(self):
        """ Vrací text "Popis kontroly" do tabulky reportů, viz metodika, kap 7.1  """
        return 'Prvky domény "' + self.fieldCaption + '" (' + ", ".join(self.fieldName) + ')'

    def toHTML(self):
        """ Konvertuje hodnoty do fornátu HTML """
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