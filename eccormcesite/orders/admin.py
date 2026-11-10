from django.contrib import admin

from .models import Orders,OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model =OrderItem
    raw_id_fields=['product']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','full_name','email']
    inlines =[OrderItemInline]
    readonly_fields=('created_at',)

admin.site.register(Orders,OrderAdmin)



