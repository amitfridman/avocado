from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AvocadoSerializer
import pandas as pd
from model_pkg.modeling_avocados import pred_price


@api_view(['POST'])
def avocado_predict(request):
    """
    get the data about the avocado from the user and
     return whether the input is fine and the prediction results.
    """

    serializer = AvocadoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        prediction = calc_average_price(serializer.data)
        return Response({'average_price': prediction},
                        status=status.HTTP_200_OK)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


def calc_average_price(data):
    pairs = {'total_volume': 'Total Volume', 'total_bags': 'Total Bags',
             'small_bags': 'Small Bags', 'large_bags': 'Large Bags',
             'x_large_bags': 'XLarge Bags', 'type': 'type', 'year': 'year',
             'region': 'region', 't_4046': '4046',
             't_4225': '4225', 't_4770': '4770'}
    data_reordered = {}
    for key in data:
        if key == 'id':
            continue
        data_reordered[pairs[key]] = [data[key]]
    data['average_price'] = pred_price(pd.DataFrame(
        data_reordered, columns=['Total Volume', '4046',
                                 '4225', '4770', 'Total Bags',
                                 'Small Bags', 'Large Bags',
                                 'XLarge Bags', 'type',
                                 'year', 'region']))
    return data['average_price'][0]
