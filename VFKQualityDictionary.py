# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        VFKQualityDictionary
# Purpose:     Slovníky pro definici jednotlivých kontrol
#
# Author:      Radek Augustýn
#
# Created:     16.07.2013
# Copyright:   (c) Augustyn 2013
# Licence:     VÚGTK, v.v.i
#-------------------------------------------------------------------------------
from Validation import *

validationDictionary = {
    "1. Struktura dat": [
        FieldTypeCheck(
            "1.2",
            "D-BĚH ID",
            ["BEH_ID"],
            "NUMBER(30,0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.3",
            "D-BPEJ KÓD",
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
##    "2. Úplnost dat ve struktuře": [],
##    "3. Formální správnost": [],
##    "4. Soulad souboru popisných a grafických informací": [],
##    "5. Parametry podrobných bodů": [],
##    "6. Topologie": [],
##    "7. Názvosloví": [],
##    "8. Kontext změny": []

}

