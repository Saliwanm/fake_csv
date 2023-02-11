from django.contrib import admin
from . import models


admin.site.register(models.Schema)
admin.site.register(models.ColumnSeparator)
admin.site.register(models.StringCharacter)
admin.site.register(models.ColumnSeparatorView)
admin.site.register(models.StringCharacterView)
admin.site.register(models.TypeOfSchemasFullname)
admin.site.register(models.TypeOfSchemasJob)
admin.site.register(models.TypeOfSchemasEmail)
admin.site.register(models.TypeOfSchemasDomainName)
admin.site.register(models.TypeOfSchemasPhoneNumber)
admin.site.register(models.TypeOfSchemasCompanyName)
admin.site.register(models.TypeOfSchemasText)
admin.site.register(models.TypeOfSchemasInteger)
admin.site.register(models.TypeOfSchemasAddress)
admin.site.register(models.TypeOfSchemasDate)
admin.site.register(models.TypeCategories)
admin.site.register(models.ColumnsSchemas)