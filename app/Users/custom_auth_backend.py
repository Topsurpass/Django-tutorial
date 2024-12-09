# custom_auth_backend.py
from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                print("Password check passed")
                if self.user_can_authenticate(user):
                    print("User can authenticate")
                    return user
                else:
                    print("User cannot authenticate (inactive or other reason)")
            else:
                print("Password check failed")
        except User.DoesNotExist:
            print("User does not exist")
            return None
