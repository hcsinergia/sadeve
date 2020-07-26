from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (index, blog, post, search, article, contact, presentation, Estatuto)
from about.views import (about)

# from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

# from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from apps.socio.views import (
    Perfil_Actualizar,
)


# from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='post-list'),
    path('article/', login_required(article), name='article-list'),
    path('presentation/', presentation, name='presentation-list'),
    path('search/', search, name='search'),
    # path('contact/', contact,  name='contact'),
    path('about/', about, name='about'),
    path('post/<id>/', post, name='post-detail'),
    path('tinymce/', include ('tinymce.urls')),

    # path('login/', Login.as_view(), name='login'),
    # path('logout/', logout, name='logout'),

    path('socio/', include(('apps.socio.urls', 'socio'))),
    path('gcalendar/', include(('apps.gcalendar.urls', 'gcalendar'))),

    path('estatuto/', Estatuto.as_view(), name='estatuto'),
    #path('posts/', include(('apps.posts.urls', 'posts'))),

    path('accounts/', include(('apps.accounts.urls', 'accounts'))),
    # path('accounts/', include('apps.accounts.urls')),
    #path('accounts/', include(('django.contrib.auth.urls', 'accounts'))),
    #path('accounts/', include('accounts.urls')),
    # path('account/', include('django.contrib.auth.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contact/', include(('apps.contact.urls', 'contact'))),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 















