from django.contrib import admin
from .models import Article, Tags, Scopes
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class TagsInLineFormSet(BaseInlineFormSet):
    def clean(self):
        x = 0
        for form in self.forms:
            for f, r in form.cleaned_data.items():
                if f == 'is_main' and r:
                    x += 1
            if x >= 2:
                raise ValidationError('main tag must be only one')
        return super().clean()


class TagsInline(admin.TabularInline):
    model = Tags.tag.through
    formset = TagsInLineFormSet


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
