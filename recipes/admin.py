from django.contrib import admin
from .models import Category, Ingredient, Recipe, Step, RecipeIngredient, Rating 
# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class StepInline(admin.TabularInline):
    model = Step
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'prep_time', 'cook_time', 'created_at']
    list_filter = ['difficulty', 'categories']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RecipeIngredientInline, StepInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ingredient)
admin.site.register(Rating)
