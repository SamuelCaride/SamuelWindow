'''

Funciones gestion clientes

'''

import var



class Clientes():
    def validarDNI():
        try:
            global dnivalido
            dnivalido = False
            dni = var.ui.txtDNI.text()
            var.ui.txtDNI.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE' #letras DNI
            dig_ext = 'XYZ'                   #digito documento extranjero
            reemp_dig_ext = {'X': '0', 'Y':'1', 'Z':'2' }
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValDNI.setStyleSheet('QLabel {color:green;}')
                    var.ui.lblValDNI.setText('V')
                    var.ui.txtDNI.setStyleSheet('background-color: white')
                    dnivalido = True
                else:
                    var.ui.lblValDNI.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValDNI.setText('X')
                    var.ui.txtDNI.setStyleSheet('background-color: pink')
            else:
                var.ui.lblValDNI.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValDNI.setText('X')
                var.ui.txtDNI.setColor('background-color: pink')
        except Exception as error:
            print('Error modulo validacion dni', error)