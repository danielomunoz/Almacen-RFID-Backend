# Generalidades del proyecto Almacén RFID

## Para el desarrollo se ha utilizado la siguiente máquina virtual:
* Un ubuntu 20.04 LTS con el usuario 'danilo' corriendo sobre virtual-box. Imagen aquí: https://releases.ubuntu.com/focal/ubuntu-20.04.6-desktop-amd64.iso
* (Recurso para la instalación: youtube.com/watch?v=GEx046EHphl)
* Abrimos un terminal y hacemos: ```cd /home/danilo```
* ```sudo apt install git```
* ```sudo apt install python3-pip```
* ```export PATH=$PATH:/home/danilo/.local/bin```
* ```sudo apt-get install libpq-dev python-dev```
* Listo, con ésto ya tenemos la máquina provisionada para correr nuestro backend

## Cómo reconstruir el entorno virtual y correr el backend de la aplicación:
* Nos situamos en una carpeta deseada
* Abrimos un terminal
* Ejecutamos: ```git clone https://github.com/danielomunoz/Almacen-RFID-Backend.git```
* Ejecutamos: ```cd Almacen-RFID-Backend```
* Ejecutamos: ```source start.sh```
* Al terminar, ya tendremos nuestro entorno virtual con todas las dependencias instaladas y el backend corriendo.

### INFO (no hay que replicar estos comandos, sólo son informativos para realizar la memoria):
* Para crear un nuevo proyecto de django: ```django-admin startproject core .```
* Comprobamos que lo hemos hecho bien con: ```python3 manage.py runserver 127.0.0.1:8000```
* Para crear una aplicación (api en nuestro caso): ```python3 manage.py startapp api```
* Si hemos modificado los modelos: ```python3 manage.py makemigrations && python manage.py migrate```
