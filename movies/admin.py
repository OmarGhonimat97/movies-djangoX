from django.contrib import admin

from .models import Movie
# Register your models here.


class CustomMovieAdmin(admin.ModelAdmin):
    model = Movie
    fieldsets = (
        ('Owner', {
            'fields': ('user',)
        }),
        ('Movie Info', {
            'fields': (
                'name',
                'description'
            )
        })
    )

    list_display = ('name', 'user')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Movie, CustomMovieAdmin)