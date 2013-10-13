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
    """ Tato t��da spou�t� relevantn� kontroly p�i parsov�n� souboru VFK. """

    def __init__(self, VFKType, validationDictionary):
        """
        Vytv��� spou�t�� kontrol nad r�dky souboru VFK

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
        Vol� nad ��dkem hlavi�ky v�echny relevantn� kontroln� funkce.
        nap��klad: &HVYTVORENO;"04.12.2012 09:47:58"

        Parameters:
            identifier {String} Identifik�tor z�znamu hlavi�ky, nap�. VYTVORENO
            value {String} Hodnota z�znamu hlavi�ky, nap�. 04.12.2012 09:47:58
        """
        pass

    def validateTableHeader(self, rowNumber, tableName, fieldDefs):
        """ Vol� nad hlavi�kou tabulky v�echny relevantn� kontroln� funkce.
        nap��klad: &BSOBR;ID N30;STAV_DAT N2;KATUZE_KOD N6;CISLO_ZPMZ N5;CISLO_TL N4;CISLO_BODU N12;UPLNE_CISLO N12;SOURADNICE_Y N10.2;SOURADNICE_X N10.2;KODCHB_KOD N2

        Parameters:
            tableName {String} Identifik�tor z�znamu hlavi�ky, nap�. SOBR
            fieldDefs {Array of vfk.FieldDef} Definice polo�ek tabulky, nap�. [ID Number(30), STAV_DAT Number(2), ...]
        """
        for validateItem in self.validateTableHeaderList:
            validateItem.validateTableHeader(rowNumber, tableName, fieldDefs)
        pass

    def validateDataRow(self, rowNumber, tableName, fieldValues):
        """ Vol� nad ��dkem tabulky v�echny relevantn� kontroln� funkce.
        nap��klad: &DSOBR;2765745709;0;733491;1;;32;1000010032;560257.84;1134738.66;

        Parameters:
            tableName {String} Identifik�tor z�znamu hlavi�ky, nap�. SOBR
            fieldValues {Array of String} Hodnoty z�znamu tabulky, nap�. ["2765745709","0","733491","1","","32","1000010032","560257.84","1134738.66"]
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