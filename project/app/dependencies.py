from .models import Usuario

def is_this_very_first_user():
    num_users = Usuario.select().count()
    return num_users == 0
