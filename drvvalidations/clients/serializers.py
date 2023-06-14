from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        pass

    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError('The CPF must have 11 digits')
    #     return cpf

    # def validate_name(self, name):
    #     if not name.isalpha():
    #         raise serializers.ValidationError('The name must not be numeric')
    #     return name

    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError('The RG must have 9 digits')
    #     return rg
    
    # def validate_phone(self, phone):
    #     if len(phone) < 11:
    #         raise serializers.ValidationError('The phone must have 11 digits')
    #     return phone
