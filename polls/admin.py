from django.contrib import admin
from .models import Question, Choice

# モデルを管理サイトに登録
admin.site.register(Question)
admin.site.register(Choice)

