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

    Události pro kontrolu v souboru VFK:
    def checkRow(self, rowNumber, rowContent)
    def validateHeaderRow(self, rowNumber, itemName, itemValue)
    def validateTableHeader(self, rowNumber, tableName, fieldDefs)
    def validateDataRow(self, rowNumber, tableName, values)
    """
    def __init__(self, validationNumber, name, description, userMessage, useType, measureText, validationRequired):
        """ Uložení parametrů """
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
        """ Vrací text "Název" do tabulky reportů, viz metodika, kap 7.1  """
        return self.name

    def getDescription(self):
        """ Vrací text "Popis kontroly" do tabulky reportů, viz metodika, kap 7.1  """
        return self.description

    def getUserMessage(self):
        """ Vrací text "Hlášení pro uživatele" do tabulky reportů, viz metodika, kap 7.1  """
        return self.userMessage

    def getMeasureText(self):
        """ Vrací text "Míra shody" do tabulky reportů, viz metodika, kap 7.1  """
        return self.measureText

    def tableRow(self, name, value):
        """ Vrací formátovaný řádek výstupní tabulky """
        return "<tr><th>" + name + "</th><td>" + str(value) + "</td></tr>\n"

    def toJson(self):
        """ Konvertuje hodnoty do formátu Json """
        temp = self.validationNumber.split(".")
        kod = int(temp[0])*100+int(temp[1])
        s = "\"id\":" + str(kod) + ",\n"
        apostrophed = self.getName()
        unapostrophed = apostrophed.replace('"', '\\"')
        s = s + "\"text\":" + "\"" + unapostrophed + "\"\n"
        return s

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

class ErrorType:
    """ Číselník "Typu chyby", viz metodika, kap 7.1 """
    Fatal    = 0
    Critical = 1
    Undefined = 2
    ERROR_TYPE_CAPTIONS = ["fatální", "kritická", "nedefinováno"]

class UseType:
    """ Záznam pro uložení stejných hodnot pro MGEO, ISKN, GP a NN """
    def __init__(self, MGEO, ISKN, GP, NN, VFK = ErrorType.Undefined):
        self.VFK = VFK
        self.MGEO = MGEO
        self.ISKN = ISKN
        self.GP = GP
        self.NN = NN
        pass

    def __repr__(self):
        return "MGEO - "  + ErrorType.ERROR_TYPE_CAPTIONS[self.MGEO] + \
               " ISKN - " + ErrorType.ERROR_TYPE_CAPTIONS[self.ISKN] + \
               " GP - "   + ErrorType.ERROR_TYPE_CAPTIONS[self.GP] + \
               " NN - "   + ErrorType.ERROR_TYPE_CAPTIONS[self.NN] + \
               " VFK - "   + ErrorType.ERROR_TYPE_CAPTIONS[self.VFK]

class ValidationRequired(UseType):
    def __repr__(self):
        return "MGEO - " + str(self.MGEO) + " ISKN - " + str(self.ISKN) + " GP - " + str(self.GP) + " NN - " + str(self.NN)

class FieldTypeCheck(VFKValidation):
    """ Třída implemntující kontrolu typu sloupce a hodnot v něm uložených
    """

    def __init__(self, validationNumber, fieldCaption, fieldName, fieldDef, useType, validationRequired):
        """ Uložení parametrů """
        VFKValidation.__init__(self, validationNumber, None, None, None, useType, "Kvalita dat určena v % jako: (0, pro počet chybných prvků >= 1;1) *100.", validationRequired)
        self.fieldCaption = fieldCaption
        self.fieldName = fieldName
        self.fieldDef = fieldDef
        self.VFKFieldPattern = None

        if self.fieldDef.find("(") == -1:
            self.fieldType = self.fieldDef
            self.fieldParams = ""
        else:
            self.fieldType = self.fieldDef[:self.fieldDef.find("(")]
            self.fieldParams =  self.fieldDef[self.fieldDef.find("(") + 1:]

        if self.fieldType == "NUMBER":
            self.VFKFieldPattern = "N" + self.fieldParams[:self.fieldParams.find(")")]
            if self.VFKFieldPattern.find(".0") >= 0:
                self.VFKFieldPattern = self.VFKFieldPattern[:len(self.VFKFieldPattern) - 2]


        pass

    def testData(self, data):
        pass

    def getUserMessage(self):
        """ Vrací text "Hlášení pro uživatele" do tabulky reportů, viz metodika, kap 7.1  """
        return "Prvek v „výpis chybných záznamů ve formátu: Název bloku – název sloupce“ není typu " + self.fieldDef

    def getName(self):
        """ Vrací text "Název" do tabulky reportů, viz metodika, kap 7.1  """
        return 'Kontrola domény "' + self.fieldCaption + '"'

    def getDescription(self):
        """ Vrací text "Popis kontroly" do tabulky reportů, viz metodika, kap 7.1  """
        return 'Prvky domény "' + self.fieldCaption + '" (' + ", ".join(self.fieldName) + ')'

    def validateTableHeader(self, rowNumber, tableName, fieldDefs):
        if self.VFKFieldPattern <> None:
            for fieldDef in fieldDefs:
                fieldName = fieldDef[:fieldDef.find(" ")]
                fieldParams = fieldDef[fieldDef.find(" ") + 1:]
                if fieldName in self.fieldName:
                    if self.VFKFieldPattern <> fieldParams:
                        print "field def for", fieldName, self.VFKFieldPattern, "<>", fieldParams
                    else:
                        pass
        pass



class VFKRowCheck_TypeID(VFKValidation):
    def __init__(self, validationNumber):
        """ Uložení parametrů """
        VFKValidation.__init__(self,
            validationNumber,
            "Základní kontrola",
            "Kontrola jestli řádky souboru začínají povolenými sekvencemi",
            "Soubor VFK musí začínat znaky &H, &D, &B, &K",
            UseType(ErrorType.Undefined, ErrorType.Undefined, ErrorType.Undefined, ErrorType.Undefined, ErrorType.Fatal),
            "Kvalita dat určena v % jako: (0, pro počet chybných prvků >= 1;1) *100.", None)
        pass

    def checkRowString(self, rowNumber, rowContent):
        """ Zkontroluje, jestli jsou hodnoty &H, &D, &B, &K """
        allowedValues = "&H", "&D", "&B", "&K"
        if rowContent in [allowedValues]:
            return ""
        else:
            return "Řádek nezačíná " + allowedValues + " " + rowNumber + ":" + rowContent
        pass

class JustOneRowCheck(VFKValidation):
    """ Třída implemntující kontrolu typu sloupce a hodnot v něm uložených
    """
    def __init__(self, validationNumber, name, description, userMessage, useType, validationRequired, id):
        """ Uložení parametrů """
        VFKValidation.__init__(
            self, validationNumber, name, description, userMessage, useType,
            "Kvalita dat určena v % jako: (1 – (podíl počtu chybějících nebo chybných údajů k požadovanému počtu))*100. Požadovaný počet je v tomto případě 1.",
            validationRequired
        )
        self.id = id
        pass


class FilledFieldsCheck(VFKValidation):
    def __init__(self, validationNumber, name, description, userMessage, useType, validationRequired):
        """ Uložení parametrů """
        VFKValidation.__init__(
            self, validationNumber, name, description, userMessage, useType,
            "U listů vlastnictví musí být povinně vyplněn sloupec ID a šestimístný kód katastrálního území ",
            validationRequired
        )
        pass

    def validateDataRow(self, rowNumber, tableName, values):
        pass