"""django_xadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
xadmin.autodiscover() # 工程启动自动检测XAdmin套件

# 导入XAdmin的插件
from xadmin.plugins import xversion
# 调用XAdmin函数加载后台所有的模型
xversion.register_models() 

from django.urls import path

urlpatterns = [
    path('admin/', xadmin.site.urls),
]