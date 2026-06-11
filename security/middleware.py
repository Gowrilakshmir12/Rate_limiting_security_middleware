from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from .models import RequestLog, BlockedIP,WhitelistedIP


class RateLimitMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR')
        if WhitelistedIP.objects.filter(ip_address=ip).exists():
            return self.get_response(request)

        blocked_ip = BlockedIP.objects.filter(
            ip_address=ip,
            violation_count__gte=3
        ).first()

        if blocked_ip:
            return JsonResponse(
                {
                    "error": "You are permanently blocked due to suspicious activity."
                },
                status=403
            )

        one_minute_ago = timezone.now() - timedelta(minutes=1)

        request_count = RequestLog.objects.filter(
            ip_address=ip,
            timestamp__gte=one_minute_ago
        ).count()

        if request_count >= 10:

            blocked_ip, created = BlockedIP.objects.get_or_create(
                ip_address=ip,
                defaults={
                    "reason": "Too many requests",
                    "violation_count": 0
                }
            )

            # Count only one violation per minute
            if (
                blocked_ip.last_violation_time is None
                or blocked_ip.last_violation_time < one_minute_ago
            ):
                blocked_ip.violation_count += 1
                blocked_ip.last_violation_time = timezone.now()
                blocked_ip.save()

            if blocked_ip.violation_count >= 3:
                return JsonResponse(
                    {
                        "error": "You are permanently blocked"
                    },
                    status=403
                )

            return JsonResponse(
                {
                    "error":
                    f"Too many requests. Warning {blocked_ip.violation_count}/3"
                },
                status=429
            )

        response = self.get_response(request)

        if hasattr(response, 'render'):
            response = response.render()

        return response