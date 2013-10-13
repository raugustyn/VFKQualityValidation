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
    "0. VFK File Format": [
        VFKRowCheck_TypeID("0.1")
    ],
    "1. Struktura dat": [
        FieldTypeCheck(
            "1.2",
            "D-BĚH ID",
            ["BEH_ID"],
            "NUMBER(30.0)",
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
            "D-CENA NEMOVITOSTI",
            ["CENA_NEMOVITOSTI"],
            "NUMBER(14.2)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.5",
            "D-ČÁST OBCE KÓD",
            ["CAOBCE_KOD"],
            "NUMBER(6.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.6",
            "D-ČÍSLO DÍLU PARCELY",
            ["DIL_PARCELY"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.7",
            "D-ČÍSLO POPISNÉ NEBO EVIDENČNÍ",
            ["CISLO_DOMOVNI"],
            "NUMBER(4.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.8",
            "D-ČÍSLO VLASTNICTVÍ",
            ["CISLO_TEL"],
            "NUMBER(6.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.9",
            "D-ČÍSLO ZPMZ",
            ["CISLO_ZPMZ", "ZPMZ_CISLO_ZPMZ"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.10",
            "D-DNEŠNÍ DATUM",
            ["CREATE_DATE", "DATUM_VZNIKU", "DATUM_ZANIKU", "UPDATE_DATE"],
            "DATE",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.11",
            "D-DPM TYPE",
            ["DPM_TYPE"],
            "VARCHAR(10)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.12",
            "D-DRUH ČÍSLOVÁNÍ PARCEL",
            ["DRUH_CISLOVANI_PAR"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.13",
            "D-DRUH POZEMKU KÓD",
            ["DRUHPOZ_KOD"],
            "NUMBER(2.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.14",
            "D-GEOMETRIE BOD",
            ["DEFINICNI_BOD_PAR"],
            "VARCHAR(100)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.15",
            "D-ID",
            ["BP_ID", "BUD_ID", "DPM_ID", "HBPEJ_ID", "HJPV_ID", "HP_ID", "ID", "JED_ID", "MAPLIS_KOD", "ML_ID", "NZ_ID", "OB_ID", "OP_ID", "PAR_ID", "PAR_ID_1", "PAR_ID_2", "PBPP_ID", "PKN_ID", "PPZ_ID", "PROJEKT_ID", "PZBPP_ID", "RIZENI_ID_VZNIKU", "RIZENI_ID", "RIZENI_ID_ZANIKU", "TEL_ID", "VERZE", "ZBPP_ID", "ZVB_ID"],
            "NUMBER(30.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.16",
            "D-KATASTRÁLNÍ ÚZEMÍ KÓD",
            ["KATUZE_KOD_PUV", "KATUZE_KOD", "ZPMZ_KATUZE_KOD"],
            "NUMBER(6.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.17",
            "D-KMENOVÉ ČÍSLO PARCELY",
            ["KMENOVE_CISLO_PAR"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.18",
            "D-KVALITA URČENÍ VÝMĚRY",
            ["ZPURVY_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.19",
            "D-NÁZEV DLOUHÝ",
            ["CISLO_ZPMZ", "ZPMZ_CISLO_ZPMZ"],
            "VARCHAR(60)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.20",
            "D-NZ TYPE",
            ["NZ_TYPE"],
            "VARCHAR(10)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.21",
            "D-OBBP TYPE",
            ["OBBP_TYPE"],
            "VARCHAR(10)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.22",
            "D-OPAR_TYPE",
            ["OPAR_TYPE"],
            "VARCHAR(10)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.23",
            "D-PAR_TYPE",
            ["PAR_TYPE"],
            "VARCHAR(10)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.24",
            "D-OBRBUD_TYPE",
            ["OBRBUD_TYPE"],
            "VARCHAR(10)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.25",
            "D-PARAMETRY LINIE",
            ["PARAMETRY_SPOJENI"],
            "VARCHAR(100)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.26",
            "D-ČÍSLO ZPMZ",
            ["CISLO_ZPMZ", "ZPMZ_CISLO_ZPMZ"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.27",
            "D-PRACOVIŠTĚ RESORTU KÓD",
            ["PRARES_KOD_OWN"],
            "NUMBER(3.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.28",
            "D-PŘÍZNAK KONTEXTU",
            ["PRIZNAK_KONTEXTU"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.29",
            "D-STAV DAT",
            ["STAV_DAT"],
            "NUMBER(2.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.30",
            "D-STAV GP",
            ["STAV_NZ"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.31",
            "D-STAV ZPMZ",
            ["STAV_ZPMZ"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.32",
            "D-TYP BUDOVY KÓD",
            ["TYPBUD_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.33",
            "D-TYP PARCELY",
            ["TYP PARCELY"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.34",
            "D-TYP PRVKU PROSTOROVÝCH DAT KÓD",
            ["TYPPPD_KOD"],
            "NUMBER(10.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.35",
            "D-TYP SOUŘADNÉHO SYSTÉMU",
            ["TYPSOS_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.36",
            "D-TYP ÚČELU",
            ["U_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.37",
            "D-USERNAME",
            ["CREATED_BY", "UPDATED_BY"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.38",
            "D-VÝMĚRA",
            ["VYMERA", "VYMERA_PARCELY"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.39",
            "D-ZDROJ PARCELY ZE KÓD",
            ["ZDPAZE_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.40",
            "D-ZPŮSOB OCHRANY NEMOVITOSTI KÓD",
            ["ZPOCHR_KOD"],
            "NUMBER(4.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.41",
            "D-ZPŮSOB VYUŽITÍ NEMOVITOSTI KÓD",
            ["ZPVYBU_KOD", "ZPVYPA_KOD"],
            "NUMBER(4.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        )
    ]
    ,
    "2. Úplnost dat ve struktuře": [
        JustOneRowCheck(
            "2.1",
            "Označení verze VF",
            'VF musí obsahovat právě jeden řádek tvaru:&HVERZE;"číslo verze VF"Číslo verze je dané konstantou (např. „4.2“)',
            '„Chybějící nebo chybné označení verze VF (&HVERZE). Doplňte údaj nebo opravte verzi VF.“',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "VERZE"
        ),
        JustOneRowCheck(
            "2.2",
            "Datum a čas vytvoření souboru",
            'VF musí obsahovat právě jeden řádek tvaru:&HVYTVORENO;"Datum"',
            '„Chybějící nebo chybné označení data vytvoření souboru (&HVYTVORENO). Doplňte nebo upravte označení data.“',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "VYTVORENO"
        ),
        JustOneRowCheck(
            "2.3",
            "Původ dat",
            'VF musí obsahovat právě jeden řádek tvaru:&HPUVOD;"libovolný text"',
            '„Chybějící nebo chybné označení původu dat (&HPUVOD). Doplňte nebo upravte označení původu dat.“',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "PUVOD"
        ),
        JustOneRowCheck(
            "2.4",
            "Označení kódové stránky",
            'VF musí obsahovat právě jeden řádek tvaru:&HCODEPAGE;"WE8ISO8859P2" nebo &HCODEPAGE;"EE8MSWIN1250"',
            '„Chybějící nebo chybné označení kódové stránky (&HCODEPAGE). Doplňte údaj nebo opravte kódovou stránku souboru“',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "CODEPAGE"
        ),
        JustOneRowCheck(
            "2.5",
            "Seznam skupin datových bloků souboru",
            'VF musí obsahovat právě jeden řádek tvaru:&HSKUPINA;"Zkratka skupiny";["Zkratka skupiny".....] Kontrola provedena proti číselníku datových bloků',
            '„Chybějící nebo chybné označení skupin datových bloků (&HSKUPINA). Doplňte nebo upravte seznam skupin datových bloků souboru.“',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "SKUPINA"
        ),
        JustOneRowCheck(
            "2.6",
            "Jméno osoby, která soubor vytvořila",
            'VF musí obsahovat právě jeden řádek tvaru:&HJMENO;"Jméno Příjmení"',
            '„Chybějící nebo chybné označení jména (&HJMENO). Doplňte nebo upravte označení jména.“',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "JMENO"
        ),
        FilledFieldsCheck(
            "2.7",
            "Kontrola povinně vyplněných sloupců u parcel",
            "U parcely musí být povinně vyplněn sloupec stav dat (STAV_DAT), typ parcely (PAR_TYPE), šestimístný kód katastrálního území (KATUZE_KOD), druh číslování parcely (DRUH_CISLOVANI_PAR), kmenové parcelní číslo (KMENOVE_CISLO_PAR), výměra parcely (VYMERA_PARCELY), identifikace budovy (IDENT_BUD).",
            "Parcely nemají vyplněné všechny povinné sloupce stav dat (STAV_DAT), typ parcely (PAR_TYPE), šestimístný kód katastrálního území ( KATUZE_KOD), druh číslování parcel (DRUH_CISLOVANI_PAR), kmenové parcelní číslo (KMENOVE_CISLO_PAR), výměra parcely (VYMERA_PARCELY), identifikace budovy (IDENT_BUD): „výpis chybných záznamů“. Doplňte chybějící údaje.",
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True)
        )
    ],
    "3. Formální správnost": [],
    "4. Soulad souboru popisných a grafických informací": [],
    "5. Parametry podrobných bodů": [],
    "6. Topologie": [],
    "7. Názvosloví": [],
    "8. Kontext změny": []

}