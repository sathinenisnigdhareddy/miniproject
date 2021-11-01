from django.contrib import admin
from .models import grocery_store
from import_export.admin import ImportExportModelAdmin

@admin.register(grocery_store)
class userdat(ImportExportModelAdmin):
    pass