from rest_framework.views import APIView
from rest_framework.response import Response


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
