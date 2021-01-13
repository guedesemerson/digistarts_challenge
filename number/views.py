from .serializers import NumberSerializer, NumberResultSerializer
from .models import Number
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status




class ExecuteAlgorithmNumberApi(generics.GenericAPIView):
    serializer_class = NumberSerializer

    def threating_list(self, list_numbers):
        removing_duplicates = []
        [removing_duplicates.append(x) for x in list_numbers if x not in removing_duplicates]
        number_array = removing_duplicates
        number_array_sorted = sorted(number_array)
        return number_array_sorted

    def post(self, request):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            number_array = request.data['number_array']
            number_array_sorted = self.threating_list(number_array)
            results = Number.objects.create(number_array=number_array, result_array=number_array_sorted)
            final_object = {'id': results.id,
                            'number_array': results.number_array,
                            'result_array': results.result_array}

            return Response(final_object, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListRegister(generics.ListAPIView):
    serializer_class = NumberResultSerializer

    def get_queryset(self):
        return Number.objects.filter()


class RetrieveRegister(generics.RetrieveAPIView):

    serializer_class = NumberResultSerializer
    lookup_field = "id"
    def get_queryset(self):
        return Number.objects.filter()


class DeleteRegister(generics.DestroyAPIView):

    lookup_field = "id"

    def get_queryset(self):
        queryset = Number.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class UpdateRegister(generics.UpdateAPIView):
    serializer_class = NumberSerializer
    lookup_field = "id"

    def threating_list(self,list_numbers):
        removing_duplicates = []
        [removing_duplicates.append(x) for x in list_numbers if x not in removing_duplicates]
        number_array = removing_duplicates
        number_array_sorted = sorted(number_array)
        return number_array_sorted

    def put(self, request, id):
        serializer = NumberSerializer(data=self.request.data)

        if serializer.is_valid():
            id_object = self.kwargs['id']
            number_array = self.request.data['number_array']
            number_array_sorted = self.threating_list(number_array)
            Number.objects.filter(id=id_object).update(number_array=number_array,
                                                       result_array=number_array_sorted)

            final_object = {'id': id_object,
                            'number_array': number_array,
                            'result_array': number_array_sorted}

            return Response(final_object, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
