from django.contrib import admin

from .models import Product, OrderDetail


admin.site.site_header = "Административная панель"
admin.site.site_title = "Админ"
admin.site.index_title = "Раздел администрирования"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ("description",)
    list_editable = ("price", "description",)
    actions = ('make_zero',)

    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail)