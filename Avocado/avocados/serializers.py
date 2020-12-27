from rest_framework import serializers
from .models import Avocado


class AvocadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avocado
        exclude = ('average_price', )
        extra_kwargs = {"region": {"error_messages": {"invalid_choice": "The given region isn't a valid region in"
                                                                        " the United States, please enter a valid"
                                                                        " one starting with a capital letter"}}}
    def validate(self, data):
        if data['total_bags'] != data['small_bags']+data['large_bags']+data['x_large_bags']:
            raise serializers.ValidationError("total bags must be equal to the sum of small, large and x_large bags")
        return data
