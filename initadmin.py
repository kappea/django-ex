#!/usr/bin/env python
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    from django.contrib.auth.models import User
    if User.objects.count() == 0:
        User.objects.create_superuser('admin', 'albert.kappe@rijksoverheid.nl', 'Dinsdag24!')
