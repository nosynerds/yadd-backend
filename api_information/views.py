from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class SchemaView(APIView):

    # Method GET
    def get(self, request, *args):

        item_id = request.GET.get('item_id')

        print(item_id)

        return JsonResponse(
            {"reason": "I am old"},
            status=status.HTTP_200_OK,
            safe=False
        )