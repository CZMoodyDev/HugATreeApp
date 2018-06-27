from django.contrib import admin
from .models import TreeInfo, Tree, FoodTree, Park, UserProfile, Photo

admin.site.register(TreeInfo)
admin.site.register(Tree)
admin.site.register(FoodTree)
admin.site.register(Park)
admin.site.register(UserProfile)
admin.site.register(Photo)

