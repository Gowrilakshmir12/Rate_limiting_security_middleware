from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RequestLog,BlockedIP,FailedLogin,WhitelistedIP
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate


@api_view(['GET'])
def test_endpoint(request):
    
    # 🔹 Get IP address
    ip = request.META.get('REMOTE_ADDR')

    


    

    # 🔹 Store in database
    RequestLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        ip_address=ip,
        endpoint=request.path,
        method=request.method,
        status_code=200
    )

    return Response({
        "message": "API is working"
        
    })
@api_view(['GET'])
def security_stats(request):
    total_requests=RequestLog.objects.count()
    blocked_ips=BlockedIP.objects.count()
    top_ip=(
        RequestLog.objects
        .values('ip_address')
        .annotate(total=Count('ip_address'))
        .order_by('-total')
        .first()
    )
    top_endpoint=(
        RequestLog.objects.values('endpoint').annotate(total=Count('id')).order_by('-total').first()
    )

    return Response({
        "total_requests":total_requests,
        "blocked_ips":blocked_ips,
        "top_ip":top_ip,
        "top_endpoint":top_endpoint
    })
@api_view(['GET'])
def suspicious_ips(request):
    suspicious=(
        RequestLog.objects
        .values('ip_address')
        .annotate(total=Count('id'))
        .filter(total__gte=20)
        .order_by('-total')
    )
    return Response(suspicious)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    total_requests=RequestLog.objects.count()

    blocked_ips=BlockedIP.objects.filter(
        violation_count__gte=3
    ).count()
    top_ip=(
        RequestLog.objects
        .values('ip_address')
        .annotate(total=Count('id'))
        .order_by('-total')
        .first()
    )
    top_endpoint=(
        RequestLog.objects
        .values('endpoint')
        .annotate(total=Count('id'))
        .order_by('-total')
        .first()
    )
    suspicious_count=(
        RequestLog.objects
        .values('ip_address')
        .annotate(total=Count('id'))
        .filter(total__gte=20)
        .count()
    )
    return Response({
        "total_requests":total_requests,
        "blocked_ips":blocked_ips,
        "top_ip":top_ip,
        "top_endpoint":top_endpoint,
        "suspicious_count":suspicious_count,
        "user":request.user.username
    })
@api_view(['POST'])
def custom_login(request):
    username=request.data.get('username')
    password=request.data.get('password')

    ip=request.META.get('REMOTE_ADDR')
    user=authenticate(request,username=username,password=password)
    if user :
        return Response({
            "message":"Login successful"
        })
    FailedLogin.objects.create(
        username=username,
        ip_address=ip
    )
    return Response({
        "error":"Invalid credentials"
    },status=401)