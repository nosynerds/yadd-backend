from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import Schemas, Tables, Columns

def getSchemas(schemas):
    id=[]
    schema_name=[]
    schema_description=[]

    for schema in schemas:
        id.append(schema.id)
        schema_name.append(schema.schema_name)
        schema_description.append(schema.schema_description)

    return {"id": id, "schema_name":schema_name, "schema_description": schema_description}

def getTables(tables):
    id = []
    schema_name = []
    table_name = []
    table_description = []

    for table in tables:
        id.append(table.id)
        schema_name.append(table.schema_name)
        table_name.append(table.table_name)
        table_description.append(table.table_description)

    return {"id": id , "schema_name": schema_name ,
            "table_description": table_description, "table_name": table_name}

# Create your views here.
class SchemaView(APIView):

    # Method GET
    def get(self, request, *args):

        item_id = request.GET.get('item_id')

        headers = [f.name for f in Schemas._meta.get_fields()]
        data = Schemas.objects.all()

        response = {
            "headers": headers,
            "data": getSchemas(data)
        }

        return JsonResponse(
            response,
            status=status.HTTP_200_OK,
            safe=False
        )

class TableView(APIView):

    # Method GET
    def get(self, request, *args):

        item_id = request.GET.get('item_id')

        selected_schema_name = Schemas.objects.filter(id=item_id)[0].schema_name

        headers = [f.name for f in Tables._meta.get_fields()]

        data = Tables.objects.filter(schema_name=selected_schema_name)

        response = {
            "headers": headers,
            "data": getTables(data)
        }

        return JsonResponse(
            response,
            status=status.HTTP_200_OK,
            safe=False
        )