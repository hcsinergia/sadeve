#!/bin/bash

NAME="sadeve"                                   	# Nombre de la aplicación
DJANGODIR=/home/web/sadeve               			# Directorio de proyectos de Django
SOCKFILE=/home/web/sadeve/run/gunicorn.sock  		# Nos comunicaremos usando este socket unix
USER=root                                         	# el usuario para ejecutar como
GROUP=root                                        	# el grupo para correr como
NUM_WORKERS=3                                       # Cuántos procesos de trabajo debería generar Gunicorn
DJANGO_SETTINGS_MODULE=sadeve.settings      		# qué archivo de configuración debe usar Django
DJANGO_WSGI_MODULE=sadeve.wsgi              		# nombre del modulo WSGI
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /home/web/sadeve/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Cree el directorio de ejecución si no existe

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Comienza tu Django Unicorn
# Los programas destinados a ejecutarse bajo supervisión no deben demonizarse a sí mismos (no utilizar --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-