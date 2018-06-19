# 导入XAdmin模块
import xadmin
# 导入views
from xadmin import views
# 导入模型
from IdcManager.models import IDC

# 创建一个基本设置类
class BasicSettings():
    # 开启主题组定制自选模式
    enable_themes = True
    # 设置选择模式（下拉）
    use_bootswatch = True

# 在系统中进行注册并启用
xadmin.site.register(views.BaseAdminView, BasicSettings)

# 创建一个全局设置类
class GlobalSettings():
    # 设置应用的名称
    site_title = 'IDC服务器运维管理平台'
    # 设置应用的脚注
    site_footer = '中软国际'
    # 扩展：设置左边菜单栏的样式(折叠)
    #menu_style = 'accordion'

# 在系统中进行注册并启用
xadmin.site.register(views.CommAdminView, GlobalSettings)

# 创建IDC管理模型绑定IDC模型
@xadmin.sites.register(IDC)
class IDCAdmin():
    # 设置前端页面的显示选项（自动构建一个表格）
    list_display = ('name', 'desc', 'phone', 'address', 'create_time', 'user',)
    # 设置一个搜索栏
    search_fields = ('name',)
    # 设置指定字段排序显示
    ordering = ('id',)
    # 实现分页
    list_per_page = 3 # 每页显示3条记录

    # 定义保存操作用户的实现方法
    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    pass