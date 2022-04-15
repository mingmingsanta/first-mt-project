from django.contrib import admin
from .models import worker, workplace, 아이디



admin.site.register(아이디)
admin.site.register(worker)


class workerLine(admin.TabularInline):
    model = worker
    extra = 3

class workplaceAdmin(admin.ModelAdmin):
    fieldsetes = [
        ('workplace',               {'fields' : {'작업장'}}),
        ]
    inlines=[workerLine]
admin.site.register(workplace,workplaceAdmin)



