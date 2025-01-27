from rest_framework import serializers
from .models import Person, Team, MONTHS, SHIRT_SIZES, Stanowisko, Osoba
from datetime import date


class PersonSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True)

    pseudonim = serializers.CharField(max_length=100, allow_null=True)

    def validate_name(self, value):

        if not value.istitle():
            raise serializers.ValidationError(
                "Nazwa osoby powinna rozpoczynać się wielką literą!",
            )
        return value

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.month_added = validated_data.get('month_added', instance.month_added)
        instance.team = validated_data.get('team', instance.team)
        instance.pseudonim = validated_data.get('pseudonim', instance.pseudonim)
        instance.save()
        return instance
    
class StanowiskoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(max_length = 80)
    opis = serializers.CharField()
    
    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance
    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'country']
        read_only_fields = ['id']
    
class OsobaSerializer(serializers.ModelSerializer):
    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole 'imie' musi zawierać tylko litery!!!")
        return value
    
    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole 'nazwisko' musi zawierać tylko litery!!!")
        return value
    
    def validate_data_dodania(self, value):
        if value > date.today():
            raise serializers.ValidationError("Pole 'data_dodania' nie może być z przyszłości!!!")
        return value
    
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko','plec', 'stanowisko', 'data_dodania']
        read_only_fields = ['id']
    