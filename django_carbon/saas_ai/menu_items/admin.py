from django.contrib import admin

# Register your models here.
from menu_items.models import CarbonTable,Carbon,StructuralElement,ElementGroup
# ,InputTable,CarbonReference,Singer,Song,Item,Category

admin.site.register(CarbonTable)
admin.site.register(Carbon)
admin.site.register(StructuralElement)
admin.site.register(ElementGroup)
# admin.site.register(CarbonReference)
# admin.site.register(InputTable)
# admin.site.register(Singer)
# admin.site.register(Song)
# admin.site.register(Item)
# admin.site.register(Category)