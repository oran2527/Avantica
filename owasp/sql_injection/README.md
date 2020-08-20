# Manual sql_injection

This project is part of sql injection training proving the creation of queries accesing tables not stablished in the program according the configuration

# Usage

- ./sqlinj.py

- output

Tabla para seleccionar datos:

- type any information according the database selected

- input 1

levels

- output 1

((1, 'low'),)

- input 2 

(just enter (empty))

- output 2

No debes dejar en blanco este campo
Tabla para seleccionar datos:


- input 3

mysql.user

- output 3

(('localhost', 'root', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '', b'', b'', b'', 0, 0, 0, 0, 'mysql_native_password', '*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B', 'N', datetime.datetime(2020, 8, 17, 2, 26, 18), None, 'N'), ('localhost', 'mysql.session', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '', b'', b'', b'', 0, 0, 0, 0, 'mysql_native_password', '*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE', 'N', datetime.datetime(2020, 8, 17, 1, 1, 44), None, 'Y'), ('localhost', 'mysql.sys', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '', b'', b'', b'', 0, 0, 0, 0, 'mysql_native_password', '*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE', 'N', datetime.datetime(2020, 8, 17, 1, 1, 44), None, 'Y'), ('localhost', 'debian-sys-maint', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '', b'', b'', b'', 0, 0, 0, 0, 'mysql_native_password', '*2F69D97C36C8E113132C2B0ADA9CC82A39F64AF9', 'N', datetime.datetime(2020, 8, 17, 1, 1, 46), None, 'N'))

