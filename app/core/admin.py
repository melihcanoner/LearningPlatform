from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Learningspace, Comment

admin.site.register(User, UserAdmin)




class CommentInline(admin.StackedInline):
    model = Comment
    


class LearningspaceAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    class Meta:
        model = Comment


admin.site.register(Learningspace, LearningspaceAdmin)
