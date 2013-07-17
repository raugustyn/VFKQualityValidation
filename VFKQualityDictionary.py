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
from Validation import *

validationDictionary = {
    "1. Struktura dat": [
        FieldTypeCheck(
            "1.2",
            "D-B�H ID",
            ["BEH_ID"],
            "NUMBER(30,0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.3",
            "D-BPEJ K�D",
            ["BPEJ_KOD", "BPEJ_KOD_HRANICE_1", "BPEJ_KOD_HRANICE_2"],
            "VARCHAR(5)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.4",
            "D- CENA NEMOVITOSTI",
            ["CENA_NEMOVITOSTI"],
            "NUMBER(14.2)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        )
    ]
##    ,
##    "2. �plnost dat ve struktu�e": [],
##    "3. Form�ln� spr�vnost": [],
##    "4. Soulad souboru popisn�ch a grafick�ch informac�": [],
##    "5. Parametry podrobn�ch bod�": [],
##    "6. Topologie": [],
##    "7. N�zvoslov�": [],
##    "8. Kontext zm�ny": []

}

