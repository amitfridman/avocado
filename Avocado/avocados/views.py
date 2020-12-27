from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Avocado
from .serializers import AvocadoSerializer


@api_view(['POST'])
def avocado_predict(request):
    """
    get the data about the avocado from the user and return whether the input is fine and the prediction results.
    """

    serializer = AvocadoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        prediction = calc_average_price(serializer.data)
        return Response({'average_price': prediction}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def calc_average_price(data):
    # todo: create an actual model for prediction
    data['average_price'] = 1.5
    return data['average_price']
