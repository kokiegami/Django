from django.contrib import admin
from .models import Question, Choice

# Questionの管理画面設定
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # 新しい選択肢を1つ追加できるようにする

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Questionを管理画面に登録
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

