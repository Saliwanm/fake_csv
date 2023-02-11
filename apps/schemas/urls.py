from django.urls import path
from . import views


urlpatterns = [
    path("", views.schemas, name="schemas"),
    path("<int:id>", views.edit_schemas, name="edit_schemas"),
    path("create_schemas"   , views.create_schemas, name="create_schemas"),
    path("update_schemas/<int:id>", views.update_schemas, name="update_schemas"),
    path("schemas_update_view/<int:id>", views.SchemaUpdateView.as_view(), name="schemas_update_view"),
    path("update_schemas_columns_add/<int:id>", views.update_schemas_columns_add, name="update_schemas_columns_add"),
    path("delete/<int:pk>/<int:id>", views.column_delete, name="column_delete"),
]