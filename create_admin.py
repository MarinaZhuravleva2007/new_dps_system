import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traffic_project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'marina'
password = 'david181007++'
email = 'marina.zhuravleva.07@inbox.ru'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Суперпользователь создан!')
else:
    print('Суперпользователь уже существует.')
