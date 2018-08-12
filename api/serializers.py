from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id',
    )
    update = serializers.HyperlinkedIdentityField(
        view_name = 'api-update',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id',
    )
    delete = serializers.HyperlinkedIdentityField(
        view_name = 'api-delete',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id',
    )
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'details',
            'update',
            'delete',
            'opening_time',
            'closing_time',
            ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name = 'api-update',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id',
    )
    delete = serializers.HyperlinkedIdentityField(
        view_name = 'api-delete',
        lookup_field = 'id',
        lookup_url_kwarg = 'restaurant_id',
    )
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'update',
            'delete',
            ]

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]