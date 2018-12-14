from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import Schemas, Tables, Columns, Catalog
from .util import executeQuery

def getCustomJSON(data, columns):
    response = {}
    data = data.fillna('')
    for column in columns:
        response[column] = list(data[column])

    return response

# Create your views here.
class SchemaView(APIView):

    # Method GET
    def get(self, request, *args):

        item_id = request.GET.get('item_id')

        query = "select id, table_schema, table_name, column_name, column_description from " \
                "(SELECT id, schema_name, table_name, column_name, column_description FROM CA_TEST.dd_maf) " \
                "a full join (select distinct table_schema FROM columns) b on a.schema_name=b.table_schema " \
                "and a.table_name='**' and a.column_name='**';"
        columns = ["id", "schema_name", "table_name", "column_name", "column_description"]

        result = executeQuery(query=query , columns=columns , return_data=True)

        response = {
            "headers": columns ,
            "data": getCustomJSON(result, columns)
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

        query = "select id, b.table_name, table_schema, column_description from (SELECT id, " \
                "schema_name, table_name, column_name, column_description FROM CA_TEST.dd_maf) a " \
                "full join (select distinct table_name , table_schema FROM columns) b on " \
                "a.table_name=b.table_name and a.column_name='**';"
        columns = ["id" , "table_name" , "schema_name", "column_description"]

        result = executeQuery(query=query , columns=columns , return_data=True)

        response = {
            "headers": columns ,
            "data": getCustomJSON(result , columns)
        }

        return JsonResponse(
            response ,
            status=status.HTTP_200_OK ,
            safe=False
        )


class ColumnView(APIView):

    # Method GET
    def get(self, request, *args):

        item_id = request.GET.get('item_id')

        query = "SELECT table_schema, table_name, column_name, data_type, data_type_length, character_maximum_length FROM columns;"
        columns = ["table_schema", "table_name", "column_name", "data_type", "data_type_length", "character_maximum_length"]

        result = executeQuery(query=query, columns=columns, return_data=True)

        response = {
            "headers": columns,
            "data": getCustomJSON(result, columns)
        }

        return JsonResponse(
            response,
            status=status.HTTP_200_OK,
            safe=False
        )