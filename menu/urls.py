from django.urls import re_path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register('menu_cat', MenuCategoryView)
router.register('menu_item', MenuItemView)
router.register('menu', MenuList)

urlpatterns = [
    re_path(r'admin/category/$', MenuCategory.as_view()),
    re_path(r'admin/category/(?P<pk>][0-9]+)$', MenuCategory.as_view()),
    re_path(r'admin/item/$', MenuItems.as_view()),
    re_path(r'admin/item/(?P<pk>\d+)/$', MenuItems.as_view()),
    # path('menu/', MenuList.as_view(),name='menu_list'),
]
urlpatterns += router.urls
