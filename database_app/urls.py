from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('brand_table', views.brand_table, name='brand_table'),
    path('client_table', views.client_table, name='client_table'),
    path('commercial_organization_table', views.commercial_organization_table, name='commercial_organization_table'),
    path('country_table', views.country_table, name='country_table'),
    path('establishment_form_table', views.establishment_form_table, name='establishment_form_table'),
    path('order_table', views.order_table, name='order_table'),
    path('product_table', views.product_table, name='product_table'),
    path('receipt_table', views.receipt_table, name='receipt_table'),
    # path('sales_point_table', views.sales_point_table, name='sales_point_table')
    path('clients_total_receipt_price_report', views.clients_total_receipt_price_report,
         name='clients_total_receipt_price_report'),
    path('organizations_total_delivered_orders_report', views.organizations_total_delivered_orders_report,
         name='organizations_total_delivered_orders_report'),

]
