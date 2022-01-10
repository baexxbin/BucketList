from django.contrib import admin
from .models import Buckets, Member

# Register your models here.
class BucketsAdmin(admin.ModelAdmin):
    list_display = ('bk_idx','title','body','photo','category','created_at','target_at','completed_at','owner')

admin.site.register(Buckets)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','id','pw','point','grade')

admin.site.register(Member)