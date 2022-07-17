from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('menu_cat', MenuCategoryView)
router.register('menu_item', MenuItemView)
router.register('menu', MenuList)

urlpatterns = [
    re_path(r'admin/category/$', MenuCategory.as_view()),
    re_path(r'admin/category/(?P<pk>][0-9]+)$', MenuCategory.as_view()),
    re_path(r'admin/item/$', MenuItem.as_view()),
    re_path(r'admin/item/(?P<pk>[0-9]+)/$', MenuItem.as_view()),
    # path('menu/', MenuList.as_view(),name='menu_list'),
]
urlpatterns += router.urls
