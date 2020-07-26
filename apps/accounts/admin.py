from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import Account
from apps.socio.models import Socio



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin




#la clase agrga los campos que necesito
class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        #'fields': ('email', 'username', 'dni', 'nombre_1', 'apellido_1', 'password1', 'password2',)
        'fields': ('email', 'username', 'dni', 'nombre_1', 'apellido_1', 'password1', 'password2',)
     
    }),
)


class AccountAdmin(UserAdmin):
	list_display = ('email','nombre_1','apellido_1', 'dni', 'last_login', 'date_joined','is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
# admin.site.register(Socio, CustomUserAdmin)



