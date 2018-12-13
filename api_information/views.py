from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import Schemas, Tables, Columns, Catalog

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

def getColumns(columns):
    id = []
    schema_name = []
    table_name = []
    column_name = []
    column_description = []
    data_type = []
    data_type_length = []
    data_type_precision = []

    for column in columns:
        id.append(column.id)
        schema_name.append(column.schema_name)
        table_name.append(column.table_name)
        column_name.append(column.column_name)
        column_description.append(column.column_description)

        column_meta_data = Catalog.objects.filter(column_name=column.column_name,
                                                  table_name=column.table_name,
                                                  schema_name=column.schema_name)


        if len(column_meta_data)>0:
            data_type.append(column_meta_data[0].data_type)
            data_type_length.append(column_meta_data[0].data_type_length)
            data_type_precision.append(column_meta_data[0].data_type_precision)

        else:
            data_type.append('')
            data_type_length.append('')
            data_type_precision.append('')

    return {"id": id , "schema_name": schema_name ,
            "column_description": column_description, "table_name": table_name,
            "column_name": column_name, "data_type": data_type, "data_type_length": data_type_length,
            "data_type_precision": data_type_precision}

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


class ColumnView(APIView):

    # Method GET
    def get(self, request, *args):

        item_id = request.GET.get('item_id')

        selected_table_name = Tables.objects.filter(id=item_id)[0].table_name

        headers = [f.name for f in Columns._meta.get_fields()]
        headers += ['data_type', 'data_type_length', 'data_type_precision']

        data = Columns.objects.filter(table_name=selected_table_name)

        response = {
            "headers": headers,
            "data": getColumns(data)
        }

        return JsonResponse(
            response,
            status=status.HTTP_200_OK,
            safe=False
        )