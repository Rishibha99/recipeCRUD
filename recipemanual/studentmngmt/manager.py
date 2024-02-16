from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,phone_number, password=None,**extrafields):
        user=self.model(phone_number=phone_number, **extrafields)
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_super_user(self,phone_number, password=None, **extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_admin',True)
        return self.create_user(phone_number, password=None,**extrafields)