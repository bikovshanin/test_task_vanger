from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from website.models import CustomFile


@admin.register(CustomFile)
class SortableAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'get_image',
        'name',
        'my_order'
    )
    fields = (
        'name',
        'file'
    )

    def get_image(self, obj):
        print(obj.file.url)
        print(obj.file)
        return mark_safe(f'<img src={obj.file.url} width="50" height="50"')

    get_image.short_description = 'Картинка'
