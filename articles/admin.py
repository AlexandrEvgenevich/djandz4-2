from django.contrib import admin
from .models import Article, Tags, Scopes
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


# class TagsInLineFormSet(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             form.cleaned_data.get()
#             raise ValidationError('хрень')
#         return super().clean()


class TagsInline(admin.TabularInline):
    model = Tags.tag.through
    # formset = TagsInLineFormSet


# class UniqInline(admin.TabularInline):
#     model = Scopes.is_uniq


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [TagsInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['topic']
