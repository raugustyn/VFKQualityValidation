# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        Validation
# Purpose:     Knihovna pro implementaci kontrol VFK podle certifikovan� metodiky
#
# Author:      Radek August�n
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     V�GTK, v.v.i
#-------------------------------------------------------------------------------

class VFKValidation:
    """
    Abstraktn� t��da definuj�c� kontrolu
    """
    def __init__(self, validationNumber, name, description, userMessage, useType, measureText, validationRequired):
        """ Ulo�en� parametr� """
        self.validationNumber = validationNumber
        self.useType = useType
        self.validationRequired = validationRequired

        self.name = name
        self.description = description
        self.userMessage = userMessage
        self.measureText = measureText
        pass

    def testHeader(self, header):
        pass

    def testData(self, data):
        pass

    def getName(self):
        """ Vrac� text "N�zev" do tabulky report�, viz metodika, kap 7.1  """
        return self.name

    def getDescription(self):
        """ Vrac� text "Popis kontroly" do tabulky report�, viz metodika, kap 7.1  """
        return self.description

    def getUserMessage(self):
        """ Vrac� text "Hl�en� pro u�ivatele" do tabulky report�, viz metodika, kap 7.1  """
        return self.userMessage

    def getMeasureText(self):
        """ Vrac� text "M�ra shody" do tabulky report�, viz metodika, kap 7.1  """
        return self.measureText

    def tableRow(self, name, value):
        """ Vrac� form�tovan� ��dek v�stupn� tabulky """
        return "<tr><td>" + name + "</td><td>" + value + "</td></tr>\n"

    def toHTML(self):
        """ Konvertuje hodnoty do forn�tu HTML """
        s = "<table>\n"
        s = s + self.tableRow("Ozna�en� kontroly", self.validationNumber)
        s = s + self.tableRow("N�zev", self.getName())
        s = s + self.tableRow("Popis kontroly", self.getDescription())
        s = s + self.tableRow("Hl�en� pro u�ivatele", self.getUserMessage())
        s = s + self.tableRow("Typ chyby", str(self.useType))
        s = s + self.tableRow("M�ra shody", self.getMeasureText())
        s = s + self.tableRow("Povinnost kontroly", str(self.validationRequired))
        s = s + "</table>\n"
        return s

class ErrorType:
    """ ��seln�k "Typu chyby", viz metodika, kap 7.1 """
    Fatal    = 0
    Critical = 1
    ERROR_TYPE_CAPTIONS = ["fat�ln�", "kritick�"]

class UseType:
    """ Z�znam pro ulo�en� stejn�ch hodnot pro MGEO, ISKN, GP a NN """
    def __init__(self, MGEO, ISKN, GP, NN):
        self.MGEO = MGEO
        self.ISKN = ISKN
        self.GP = GP
        self.NN = NN
        pass

    def __repr__(self):
        return "MGEO - "  + ErrorType.ERROR_TYPE_CAPTIONS[self.MGEO] + \
               " ISKN - " + ErrorType.ERROR_TYPE_CAPTIONS[self.ISKN] + \
               " GP - "   + ErrorType.ERROR_TYPE_CAPTIONS[self.GP] + \
               " NN - "   + ErrorType.ERROR_TYPE_CAPTIONS[self.NN]

class ValidationRequired(UseType):
    def __repr__(self):
        return "MGEO - " + str(self.MGEO) + " ISKN - " + str(self.ISKN) + " GP - " + str(self.GP) + " NN - " + str(self.NN)

class FieldTypeCheck(VFKValidation):
    """ T��da implemntuj�c� kontrolu typu sloupce a hodnot v n�m ulo�en�ch
    """

    def __init__(self, validationNumber, fieldCaption, fieldName, fieldDef, useType, validationRequired):
        """ Ulo�en� parametr� """
        VFKValidation.__init__(self, validationNumber, None, None, None, useType, "Kvalita dat ur�ena v % jako: (0, pro po�et chybn�ch prvk� >= 1;1) *100.", validationRequired)
        self.fieldCaption = fieldCaption
        self.fieldName = fieldName
        self.fieldName = fieldName
        self.fieldDef = fieldDef
        pass

    def testData(self, data):
        pass

    def getUserMessage(self):
        """ Vrac� text "Hl�en� pro u�ivatele" do tabulky report�, viz metodika, kap 7.1  """
        return "Prvek v �v�pis chybn�ch z�znam� ve form�tu: N�zev bloku � n�zev sloupce� nen� typu " + self.fieldDef

    def getName(self):
        """ Vrac� text "N�zev" do tabulky report�, viz metodika, kap 7.1  """
        return 'Kontrola dom�ny "' + self.fieldCaption + '"'

    def getDescription(self):
        """ Vrac� text "Popis kontroly" do tabulky report�, viz metodika, kap 7.1  """
        return 'Prvky dom�ny "' + self.fieldCaption + '" (' + ", ".join(self.fieldName) + ')'


class JustOneRowCheck(VFKValidation):
    """ T��da implemntuj�c� kontrolu typu sloupce a hodnot v n�m ulo�en�ch
    """
    def __init__(self, validationNumber, name, description, userMessage, useType, validationRequired, id):
        """ Ulo�en� parametr� """
        VFKValidation.__init__(
            self, validationNumber, name, description, userMessage, useType,
            "Kvalita dat ur�ena v % jako: (1 � (pod�l po�tu chyb�j�c�ch nebo chybn�ch �daj� k po�adovan�mu po�tu))*100. Po�adovan� po�et je v tomto p��pad� 1.",
            validationRequired
        )
        self.id = id
        pass

