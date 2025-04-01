from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# On définit le module de paramètres Django par défaut pour Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')

# On utilise un espace de noms spécifique pour les tâches Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# On charge toutes les tâches modélisées dans les fichiers tasks.py des applications Django
app.autodiscover_tasks()
