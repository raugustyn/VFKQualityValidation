# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      raugustyn
#
# Created:     18/07/2013
# Copyright:   (c) raugustyn 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from vfk import RowType

class VFKValidator:
    """ Tato třída spouští relevantní kontroly při parsování souboru VFK. """

    def __init__(self, VFKType, validationDictionary):
        """
        Vytváří spouštěč kontrol nad rádky souboru VFK

        Parameters:
            VFKType {Validation.???}
            validationDictionary {Dictionary of Array of Validation.VFKValidation}
        """
        self.VFKType = VFKType
        self.validationDictionary = validationDictionary

        self.checkRowStringList = []
        self.validateTableHeaderList = []
        self.validateDataRowList = []

        for groupName in validationDictionary:
            group = validationDictionary[groupName]
            for checkItem in group:
                if "checkRowString" in dir(checkItem):
                    self.checkRowStringList.append(checkItem)

                if "validateTableHeader" in dir(checkItem):
                    self.validateTableHeaderList.append(checkItem)

                if "validateDataRow" in dir(checkItem):
                    self.validateDataRowList.append(checkItem)

                pass
        pass

    def validateFile(self, reader):
        reader.rewindToStart()
        rowNumber = 0
        while True:
            recordData = reader.read()
            rowNumber = rowNumber + 1
            lineType = recordData[0]

            if lineType == RowType.Eof:
                break
            elif lineType == RowType.Header:
                data = recordData[1]
                self.validateHeaderRow(data[0], data[1])
                pass
            elif lineType == RowType.Block:
                data = recordData[1]
                self.validateTableHeader(rowNumber, data[0].lower(), data[1:])
                print data[0].lower()
                pass
            elif lineType == RowType.Data:
                data = recordData[1]
                self.validateDataRow(rowNumber, data[0].lower(), data[1:])
                pass
        pass

    def checkRowString(self, rowNumber, rowContent):
        for validateItem in self.checkRowStringList:
            validateItem.checkRowString(rowNumber, rowContent)
        pass

    def validateHeaderRow(self, identifier, value):
        """
        Volá nad řádkem hlavičky všechny relevantní kontrolní funkce.
        například: &HVYTVORENO;"04.12.2012 09:47:58"

        Parameters:
            identifier {String} Identifikátor záznamu hlavičky, např. VYTVORENO
            value {String} Hodnota záznamu hlavičky, např. 04.12.2012 09:47:58
        """
        pass

    def validateTableHeader(self, rowNumber, tableName, fieldDefs):
        """ Volá nad hlavičkou tabulky všechny relevantní kontrolní funkce.
        například: &BSOBR;ID N30;STAV_DAT N2;KATUZE_KOD N6;CISLO_ZPMZ N5;CISLO_TL N4;CISLO_BODU N12;UPLNE_CISLO N12;SOURADNICE_Y N10.2;SOURADNICE_X N10.2;KODCHB_KOD N2

        Parameters:
            tableName {String} Identifikátor záznamu hlavičky, např. SOBR
            fieldDefs {Array of vfk.FieldDef} Definice položek tabulky, např. [ID Number(30), STAV_DAT Number(2), ...]
        """
        for validateItem in self.validateTableHeaderList:
            validateItem.validateTableHeader(rowNumber, tableName, fieldDefs)
        pass

    def validateDataRow(self, rowNumber, tableName, fieldValues):
        """ Volá nad řádkem tabulky všechny relevantní kontrolní funkce.
        například: &DSOBR;2765745709;0;733491;1;;32;1000010032;560257.84;1134738.66;

        Parameters:
            tableName {String} Identifikátor záznamu hlavičky, např. SOBR
            fieldValues {Array of String} Hodnoty záznamu tabulky, např. ["2765745709","0","733491","1","","32","1000010032","560257.84","1134738.66"]
        """
        for validateItem in self.validateDataRowList:
            validateItem.validateDataRow(rowNumber, tableName, fieldValues)
        pass

from Testing.referencedatabase import *

import vfk
import VFKQualityDictionary

def main():
    reader = vfk.VFKReader(SAMPLE_DATA[0]) # 5
    validator = VFKValidator(None, VFKQualityDictionary.validationDictionary)
    validator.validateFile(reader)


if __name__ == '__main__':
    main()