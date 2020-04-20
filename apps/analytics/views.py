from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Analytics


class AnalyticsAPIView(APIView):

    def get(self, request):
        forwarded_address = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_address:
            client_address = forwarded_address.split(',')[0]
        else:
            client_address = request.META.get('REMOTE_ADDR')

        data = {
            'client_address': client_address,
        }

        return Response(data)

    def post(self, request):
        forwarded_address = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_address:
            client_address = forwarded_address.split(',')[0]
        else:
            client_address = request.META.get('REMOTE_ADDR')

        ips = Analytics.objects.values_list('ip_address', flat=True)
        ips_list = list(ips)

        if client_address in ips_list:
            obj = Analytics.objects.get(ip_address=client_address)
            obj.play_time += 1
            obj.save()
        else:
            Analytics.objects.create(ip_address=client_address)

        return Response(status=status.HTTP_200_OK)
