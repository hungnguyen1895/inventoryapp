from django.contrib import admin

#check import
from models import Item

#list_display is how the item displays in database
class ItemAdmin(admin.ModelAdmin):
	list_display = ['title','description','amount']

admin.site.register(Item, ItemAdmin)
