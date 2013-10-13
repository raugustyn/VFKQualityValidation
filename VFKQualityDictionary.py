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
            "D-B�H ID",
            ["BEH_ID"],
            "NUMBER(30.0)",
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
            "D-CENA NEMOVITOSTI",
            ["CENA_NEMOVITOSTI"],
            "NUMBER(14.2)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.5",
            "D-��ST OBCE K�D",
            ["CAOBCE_KOD"],
            "NUMBER(6.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.6",
            "D-��SLO D�LU PARCELY",
            ["DIL_PARCELY"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.7",
            "D-��SLO POPISN� NEBO EVIDEN�N�",
            ["CISLO_DOMOVNI"],
            "NUMBER(4.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.8",
            "D-��SLO VLASTNICTV�",
            ["CISLO_TEL"],
            "NUMBER(6.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.9",
            "D-��SLO ZPMZ",
            ["CISLO_ZPMZ", "ZPMZ_CISLO_ZPMZ"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.10",
            "D-DNE�N� DATUM",
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
            "D-DRUH ��SLOV�N� PARCEL",
            ["DRUH_CISLOVANI_PAR"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.13",
            "D-DRUH POZEMKU K�D",
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
            "D-KATASTR�LN� �ZEM� K�D",
            ["KATUZE_KOD_PUV", "KATUZE_KOD", "ZPMZ_KATUZE_KOD"],
            "NUMBER(6.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.17",
            "D-KMENOV� ��SLO PARCELY",
            ["KMENOVE_CISLO_PAR"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.18",
            "D-KVALITA UR�EN� V�M�RY",
            ["ZPURVY_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.19",
            "D-N�ZEV DLOUH�",
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
            "D-��SLO ZPMZ",
            ["CISLO_ZPMZ", "ZPMZ_CISLO_ZPMZ"],
            "NUMBER(5.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.27",
            "D-PRACOVI�T� RESORTU K�D",
            ["PRARES_KOD_OWN"],
            "NUMBER(3.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.28",
            "D-P��ZNAK KONTEXTU",
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
            "D-TYP BUDOVY K�D",
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
            "D-TYP PRVKU PROSTOROV�CH DAT K�D",
            ["TYPPPD_KOD"],
            "NUMBER(10.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.35",
            "D-TYP SOU�ADN�HO SYST�MU",
            ["TYPSOS_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.36",
            "D-TYP ��ELU",
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
            "D-V�M�RA",
            ["VYMERA", "VYMERA_PARCELY"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.39",
            "D-ZDROJ PARCELY ZE K�D",
            ["ZDPAZE_KOD"],
            "NUMBER(1.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.40",
            "D-ZP�SOB OCHRANY NEMOVITOSTI K�D",
            ["ZPOCHR_KOD"],
            "NUMBER(4.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        ),

        FieldTypeCheck(
            "1.41",
            "D-ZP�SOB VYU�IT� NEMOVITOSTI K�D",
            ["ZPVYBU_KOD", "ZPVYPA_KOD"],
            "NUMBER(4.0)",
            UseType(ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal, ErrorType.Fatal),
            ValidationRequired(True, True, True, True)
        )
    ]
    ,
    "2. �plnost dat ve struktu�e": [
        JustOneRowCheck(
            "2.1",
            "Ozna�en� verze VF",
            'VF mus� obsahovat pr�v� jeden ��dek tvaru:&HVERZE;"��slo verze VF"��slo verze je dan� konstantou (nap�. �4.2�)',
            '�Chyb�j�c� nebo chybn� ozna�en� verze VF (&HVERZE). Dopl�te �daj nebo opravte verzi VF.�',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "VERZE"
        ),
        JustOneRowCheck(
            "2.2",
            "Datum a �as vytvo�en� souboru",
            'VF mus� obsahovat pr�v� jeden ��dek tvaru:&HVYTVORENO;"Datum"',
            '�Chyb�j�c� nebo chybn� ozna�en� data vytvo�en� souboru (&HVYTVORENO). Dopl�te nebo upravte ozna�en� data.�',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "VYTVORENO"
        ),
        JustOneRowCheck(
            "2.3",
            "P�vod dat",
            'VF mus� obsahovat pr�v� jeden ��dek tvaru:&HPUVOD;"libovoln� text"',
            '�Chyb�j�c� nebo chybn� ozna�en� p�vodu dat (&HPUVOD). Dopl�te nebo upravte ozna�en� p�vodu dat.�',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "PUVOD"
        ),
        JustOneRowCheck(
            "2.4",
            "Ozna�en� k�dov� str�nky",
            'VF mus� obsahovat pr�v� jeden ��dek tvaru:&HCODEPAGE;"WE8ISO8859P2" nebo &HCODEPAGE;"EE8MSWIN1250"',
            '�Chyb�j�c� nebo chybn� ozna�en� k�dov� str�nky (&HCODEPAGE). Dopl�te �daj nebo opravte k�dovou str�nku souboru�',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "CODEPAGE"
        ),
        JustOneRowCheck(
            "2.5",
            "Seznam skupin datov�ch blok� souboru",
            'VF mus� obsahovat pr�v� jeden ��dek tvaru:&HSKUPINA;"Zkratka skupiny";["Zkratka skupiny".....] Kontrola provedena proti ��seln�ku datov�ch blok�',
            '�Chyb�j�c� nebo chybn� ozna�en� skupin datov�ch blok� (&HSKUPINA). Dopl�te nebo upravte seznam skupin datov�ch blok� souboru.�',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "SKUPINA"
        ),
        JustOneRowCheck(
            "2.6",
            "Jm�no osoby, kter� soubor vytvo�ila",
            'VF mus� obsahovat pr�v� jeden ��dek tvaru:&HJMENO;"Jm�no P��jmen�"',
            '�Chyb�j�c� nebo chybn� ozna�en� jm�na (&HJMENO). Dopl�te nebo upravte ozna�en� jm�na.�',
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True),
            "JMENO"
        ),
        FilledFieldsCheck(
            "2.7",
            "Kontrola povinn� vypln�n�ch sloupc� u parcel",
            "U parcely mus� b�t povinn� vypln�n sloupec stav dat (STAV_DAT), typ parcely (PAR_TYPE), �estim�stn� k�d katastr�ln�ho �zem� (KATUZE_KOD), druh ��slov�n� parcely (DRUH_CISLOVANI_PAR), kmenov� parceln� ��slo (KMENOVE_CISLO_PAR), v�m�ra parcely (VYMERA_PARCELY), identifikace budovy (IDENT_BUD).",
            "Parcely nemaj� vypln�n� v�echny povinn� sloupce stav dat (STAV_DAT), typ parcely (PAR_TYPE), �estim�stn� k�d katastr�ln�ho �zem� ( KATUZE_KOD), druh ��slov�n� parcel (DRUH_CISLOVANI_PAR), kmenov� parceln� ��slo (KMENOVE_CISLO_PAR), v�m�ra parcely (VYMERA_PARCELY), identifikace budovy (IDENT_BUD): �v�pis chybn�ch z�znam��. Dopl�te chyb�j�c� �daje.",
            UseType(ErrorType.Critical, ErrorType.Critical, ErrorType.Critical, ErrorType.Critical),
            ValidationRequired(True, True, True, True)
        )
    ],
    "3. Form�ln� spr�vnost": [],
    "4. Soulad souboru popisn�ch a grafick�ch informac�": [],
    "5. Parametry podrobn�ch bod�": [],
    "6. Topologie": [],
    "7. N�zvoslov�": [],
    "8. Kontext zm�ny": []

}