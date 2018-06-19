from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 创建一个全新的模型IDC
class IDC(models.Model):
    # 设置属性
    name = models.CharField(max_length=64, verbose_name='服务器名称') # 服务器名称
    desc = models.CharField(max_length=128, verbose_name='服务器描述') # 服务器描述
    phone = models.CharField(max_length=64, verbose_name='联系电话') # 联系电话
    address = models.CharField(max_length=128, verbose_name='所在地') # 所在地
    create_time = models.DateTimeField(auto_now=True, verbose_name='录入时间') # 信息录入时间
    # 外键关联User用户模型
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, verbose_name='操作员')

    # 设置模型元数据信息
    class Meta:
        # 设置选项名称
        verbose_name = 'IDC服务器'
        # 设置菜单的名称
        verbose_name_plural = verbose_name
