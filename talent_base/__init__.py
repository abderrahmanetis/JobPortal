from __future__ import absolute_import, unicode_literals

# On évite de charger des tâches au moment du démarrage de Django
from .celery import app as celery_app

__all__ = ('celery_app',)
