from django.urls import path, re_path

from . import views

app_name = 'PoManager'
urlpatterns = [
    # display lists of Po items:
    # path('poitem/ponum/<str:po_num>/', views.getPoitem, name='list_po_item_from_po_num'),
    re_path(r'poitem/ponum/(?P<po_num>[\w_-]+)/$', views.listPoItemFromPoNum, name='list_po_item_from_po_num'),
    re_path(r'poitem/ponum/(?P<po_num>[\w_-]+)/(?P<minDateText>\d{4}-\d{2}-\d{2})/$', views.listPoItemFromPoNum, name='list_po_item_from_po_num_mindate'),
    re_path(r'poitem/ponum/(?P<po_num>[\w_-]+)/(?P<minDateText>\d{4}-\d{2}-\d{2})/(?P<maxDateText>\d{4}-\d{2}-\d{2})/$', views.listPoItemFromPoNum, name='list_po_item_from_po_num_mindate_maxdate'),

    path('poitem/pn/<str:pn>/', views.listPoItemFromPn, name='list_po_item_from_pn'),
    re_path(r'poitem/pn/(?P<pn>[\w_-]+)/(?P<minDateText>\d{4}-\d{2}-\d{2})/$', views.listPoItemFromPn, name='list_po_item_from_pn_num_mindate'),
    re_path(r'poitem/pn/(?P<pn>[\w_-]+)/(?P<minDateText>\d{4}-\d{2}-\d{2})/(?P<maxDateText>\d{4}-\d{2}-\d{2})/$', views.listPoItemFromPn, name='list_po_item_from_pn_num_mindate_maxdate'),

    re_path(r'poitem/desc/(?P<description>[\w_-]+)/$', views.listPoItemFromDescription, name='list_po_item_from_description'),
    re_path(r'poitem/desc/(?P<description>[\w_-]+)/(?P<minDateText>\d{4}-\d{2}-\d{2})/$', views.listPoItemFromDescription, name='list_po_item_from_description_mindate'),
    re_path(r'poitem/desc/(?P<description>[\w_-]+)/(?P<minDateText>\d{4}-\d{2}-\d{2})/(?P<maxDateText>\d{4}-\d{2}-\d{2})/$', views.listPoItemFromDescription, name='list_po_item_from_description_mindate_maxdate'),
    path('product/pn/<str:pn>/', views.listProductFromPn, name='list_product_from_pn'),
    path('product/desc/<str:description>/', views.listProductFromDescription, name='list_product_from_description'),
    # test views
    # path('<int:pk>/ach/', views.AchView.as_view(), name='ach')
    re_path(r'test_ach/(?P<une_valeur>\d{4}-\d{2}-\d{2})/', views.test_ach, name='test_ach'),
    path('ach/', views.AchView.as_view(), name='ach'),
]

