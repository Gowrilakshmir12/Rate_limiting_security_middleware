from django.contrib import admin
from .models import RequestLog,BlockedIP,WhitelistedIP,FailedLogin
admin.site.register(WhitelistedIP)


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display=(
        'ip_address',
        'endpoint',
        'method',
        'status_code',
        'timestamp'
    )
    search_fields=(
        'ip_address',
        'endpoint'
    )
    list_filter=(
        'method',
        'status_code'
    )
@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display=(
        'ip_address',
        'violation_count',
        'reason'
    )
@admin.register(FailedLogin)
class FailedLoginAdmin(admin.ModelAdmin):
    list_display=(
        'username',
        'ip_address',
        'timestamp'
    )
    search_fields=(
        'username',
        'ip_address'
    )

# Register your models here.
