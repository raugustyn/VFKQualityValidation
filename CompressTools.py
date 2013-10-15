# -*- coding: cp1250 -*-
#-------------------------------------------------------------------------------
# Name:        CompressTools
# Purpose:
#
# Author:      raugustyn
#
# Created:     13/10/2013
# Copyright:   (c) raugustyn 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import shutil, os

# @TODO Nastavovat vhodne proměnnou tempDir
# @TODO Vymazat při ukončení programu proměnnou tempDir

UNCOMPRESSED_EXTENSIONS = ['vfk']

def openFile(fileName):
    """
    Otevře soubor fileName vhodným kompresním programem a vrátí otevřený stream.

    @result {Stream | None}
    """
    fileExtension = fileName[fileName.rfind(".") + 1:].lower()
    if fileExtension in UNCOMPRESSED_EXTENSIONS:
        return open(fileName)
    else:
        formats = shutil.get_archive_formats()
        for dict in formats:
            if fileExtension == dict[0]:
                tempDir = "tempDir"
                if os.path.exists(tempDir):
                    shutil.rmtree(tempDir)

                shutil.unpack_archive(fileName, tempDir)
                onlyfiles = [ f for f in os.listdir(tempDir) if os.path.isfile(os.path.join(tempDir,f)) ]
                if onlyfiles == []:
                    return None
                else:
                    return open(tempDir + '\\' + onlyfiles[0])
            pass
    return None

if __name__ == '__main__':
    import Testing.tests_CompressTools
    Testing.tests_CompressTools.main()
