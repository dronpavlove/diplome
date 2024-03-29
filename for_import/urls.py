from django.urls import path

from for_import.views import update_product_list, FileFieldView
from for_import.services import list_prop_category, export_file_csv


urlpatterns = [
    path('products/', update_product_list, name='import-product'),
    path("ajax/", list_prop_category),
    path('export/<int:pk>', export_file_csv, name='export-file'),
    path('update/', FileFieldView.as_view(), name='update-file'),
]
