import os.path
import sys, var, shutil
import zipfile

from ventana import *
from datetime import date, datetime
from zipfile import ZipFile
class Eventos():

    def Salir():
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print('Error: %s' % str(error))

'''
    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%YY.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None,'Guardar Copia', var.copia,'.zip', options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))

        except Exception as error:
            print('Error Crear Backup', error)

    def restaurarBackup(self):
        try:
            dirpro = os.getcwd()
            print(dirpro)
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad','*.zip;;All
                                                        opstions = option)
            if var.dlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall()
                bbdd.close()
                shutil.move('bbdd.sqlite',str(dirpro))
            

        except Exception as error:
            print('Error en restaurar backup', error)
'''