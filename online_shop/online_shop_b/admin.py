from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'display_date', 'updated_date', 'auction', 'user', 'display_photo']
    list_filter = ['created_at', 'auction']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        (
            "Общее", {
                'fields':('title', 'description', 'user', 'image')
            }
        ),
        (
            "Остальное", {
                'fields':('price', 'auction')
            }
        )
    )

    @admin.display(description='Сделать торг true')
    def make_auction_as_true(self, req, queryset):
        queryset.update(auction=True)

    @admin.display(description='Сделать торг false')
    def make_auction_as_false(self, req, queryset):
        queryset.update(auction=False)

admin.site.register(Advertisement, AdvertisementAdmin)
