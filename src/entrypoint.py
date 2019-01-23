from django.contrib.auth import get_user_model
User = get_user_model()
# if admin exists:
user = User.objects.filter(username="admin")
if user:
    user = user[0]
    user.is_superuser = True
    user.set_password("adminadmin")
    user.save()
else:
    user = User(username='admin')
    user.is_superuser = True
    user.set_password("adminadmin")
    user.save()
