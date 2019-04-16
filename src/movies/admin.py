from django.contrib import admin

from .models import Movie, MovieRole, MovieStill, MovieQuote
# Register your models here.

class MovieStillInline(admin.TabularInline):
    model = MovieStill
class MovieQuoteInline(admin.TabularInline):
    model = MovieQuote

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (MovieStillInline, MovieQuoteInline)

@admin.register(MovieRole)
class MovieRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(MovieStill)
class MovieStillAdmin(admin.ModelAdmin):
    pass
