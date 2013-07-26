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

    def validateFile(self, reader):
        reader.rewindToStart()
        while True:
            recordData = reader.read()
            lineType = recordData[0]

            if lineType == RowType.Eof:
                break
            elif lineType == RowType.Header:
                data = recordData[1]
                self.validateHeaderRow(data[0], data[1])
                pass
            elif lineType == RowType.Block:
                data = recordData[1]
                self.validateTableHeader(data[0].lower(), data[1:])
                print data[0].lower()
                pass
            elif lineType == RowType.Data:
                data = recordData[1]
                self.validateTableRow(data[0].lower(), data[1:])
                pass
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

    def validateTableHeader(self, tableName, fieldDefs):
        """ Vol� nad hlavi�kou tabulky v�echny relevantn� kontroln� funkce.
        nap��klad: &BSOBR;ID N30;STAV_DAT N2;KATUZE_KOD N6;CISLO_ZPMZ N5;CISLO_TL N4;CISLO_BODU N12;UPLNE_CISLO N12;SOURADNICE_Y N10.2;SOURADNICE_X N10.2;KODCHB_KOD N2

        Parameters:
            tableName {String} Identifik�tor z�znamu hlavi�ky, nap�. SOBR
            fieldDefs {Array of vfk.FieldDef} Definice polo�ek tabulky, nap�. [ID Number(30), STAV_DAT Number(2), ...]
        """
        pass

    def validateTableRow(self, tableName, fieldValues):
        """ Vol� nad ��dkem tabulky v�echny relevantn� kontroln� funkce.
        nap��klad: &DSOBR;2765745709;0;733491;1;;32;1000010032;560257.84;1134738.66;

        Parameters:
            tableName {String} Identifik�tor z�znamu hlavi�ky, nap�. SOBR
            fieldValues {Array of String} Hodnoty z�znamu tabulky, nap�. ["2765745709","0","733491","1","","32","1000010032","560257.84","1134738.66"]
        """
        pass

from Testing.referencedatabase import *

import vfk
import VFKQualityDictionary

def main():
    reader = vfk.VFKReader(SAMPLE_DATA[2]) # 5
    validator = VFKValidator(None, VFKQualityDictionary.validationDictionary)
    validator.validateFile(reader)


if __name__ == '__main__':
    main()