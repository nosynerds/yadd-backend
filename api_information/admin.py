from django.contrib import admin
from .models import Schemas, Tables, Columns, Catalog

# Register your models here.
class SchemaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Schemas, SchemaAdmin)


class TableAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tables, TableAdmin)


class ColumnAdmin(admin.ModelAdmin):
    pass
admin.site.register(Columns, ColumnAdmin)


class CatalogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Catalog, CatalogAdmin)