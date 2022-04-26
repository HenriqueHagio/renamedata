#! python3
# renameDates.py - Renomeia os nomes de arquivo com formato de data MM-DD-AAAA em estilo
# americano para o formato DD-MM-AAAA em estilo europeu

import shutil,os,re

# Cria uma regex que corresponda aos arquivos com formato de data estilo americano
datePattern=re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

# TODO: Percorre os arquivos do diretório de trabalho com loop.
for amerFilename in os.listdir('C:\\'):
    mo=datePattern.search(amerFilename)
# TODO: Ignora os arquivos que não tenham uma data. 
    if mo==None:
        continue
# TODO: Obtém as diferentes partes do nome do arquivo. 
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)
# TODO: Compõe o nome do arquivo em estilo europeu. 
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
# TODO: Obtém os paths absolutos completos dos arquivos. 
    absWorkingDir=os.path.abspath('C:\\')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)
# TODO: Renomeia os arquivos.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename,euroFilename)
