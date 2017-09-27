"""django_gateone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from webterminal.views import Index,Commands,CommandExecute,CommandExecuteList,CommandExecuteDetailApi,CredentialCreate,CredentialList,CredentialDetailApi
from django.contrib.auth.views import LoginView,LogoutView

#Webterminal api
from rest_framework import routers
from webterminal.api import ServerGroupViewSet,ServerInforViewSet,CommandsSequenceViewSet,CredentialViewSet

#Register webterminal api
router = routers.DefaultRouter()
router.register('servergroup', ServerGroupViewSet)
router.register('serverinfo', ServerInforViewSet)
router.register('commandssequence', CommandsSequenceViewSet)
router.register('credential', CredentialViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Index.as_view(),name='index'),
    url(r'^commands/add/$',Commands.as_view(),name='commands'),
    url(r'^commandexecute/$',CommandExecute.as_view(),name='commandexecute'),
    url(r'^commandslist/$',CommandExecuteList.as_view(),name='commandslist'),
    url(r'^commandsapi/$',CommandExecuteDetailApi.as_view(),name='commandsapi'),
    url(r'^accounts/login/$', LoginView.as_view(template_name='admin/login.html'),name='login'),
    url(r'^accounts/logout/$',LogoutView.as_view(template_name='registration/logged_out.html'),name='logout'),     
    url(r'^credentialcreate/$',CredentialCreate.as_view(),name='credentialcreate'),
    url(r'^credentiallist/$',CredentialList.as_view(),name='credentiallist'),
    url(r'^credentialdetailapi/$',CredentialDetailApi.as_view(),name='credentialdetailapi'),
    url(r'^api/',include(router.urls)),
]