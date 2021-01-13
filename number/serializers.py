from rest_framework import serializers
from .models import Number


class NumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Number
        fields = (
            'id',
            'number_array',
            'result_array',
        )
        read_only_fields = (
            'id',
            'result_array',
        )

    def validateSingularNumber(self, list_number):
        if list_number[0] >= 1 and  list_number[0] <= 1000:
            return True

        raise serializers.ValidationError(
            {'Erro': 'O número selecionado não satisfaz as condições: 1000 <= N >= 1'})

    def validatePluralNumber(self, list_numbers):
        for number in list_numbers:
            if not number <= 1000 and number >= -1000:
                raise serializers.ValidationError(
                    {'Erro': 'O número(s) selecionado(s) não satisfaz(em) as condições: -1000 <= K >= 1000'})

        return True

    def validate(self, attrs):
        list_number = attrs.get('number_array', '')
        counting_numbers = len(list_number)

        if counting_numbers == 0:
            raise serializers.ValidationError(
                {'Erro': 'A lista está vazia'})

        elif counting_numbers == 1:
            result = self.validateSingularNumber(list_number)
            if result:
                return super().validate(attrs)

        else:
            result = self.validatePluralNumber(list_number)
            if result:
                return super().validate(attrs)


class NumberResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Number
        fields = (
            'id',
            'number_array',
            'result_array',
        )
