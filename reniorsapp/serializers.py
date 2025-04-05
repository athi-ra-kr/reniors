from rest_framework import serializers
from .models import *

# ---------------- Country, State, District, City Serializers ---------------- #

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

# ---------------- Facility Serializers ---------------- #

class FacilityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityImage
        fields = ['image']

class FacilityVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityVideo
        fields = ['video_link']

class FacilitySerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    state = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')
    district = serializers.SlugRelatedField(queryset=District.objects.all(), slug_field='name')
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')
    images = FacilityImageSerializer(many=True, read_only=True)
    videos = FacilityVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Facility
        fields = ['name', 'country', 'state', 'district', 'city', 'description', 'images', 'videos']

# ---------------- Other Models Serializers ---------------- #

class QuickServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickService
        fields = ['name', 'image']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['name', 'details', 'price']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_name', 'article_image', 'article_description']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['image']

# ---------------- Enquiry Serializers ---------------- #

class QuickServiceEnquirySerializer(serializers.ModelSerializer):
    quick_service = serializers.SlugRelatedField(queryset=QuickService.objects.all(), slug_field='name')
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    state = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')
    district = serializers.SlugRelatedField(queryset=District.objects.all(), slug_field='name')
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')

    class Meta:
        model = QuickServiceEnquiry
        fields = ['name', 'email', 'mobile_number', 'quick_service', 'country', 'state', 'district', 'city']

class FacilityEnquirySerializer(serializers.ModelSerializer):
    facility = serializers.SlugRelatedField(queryset=Facility.objects.all(), slug_field='name')
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    state = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')
    district = serializers.SlugRelatedField(queryset=District.objects.all(), slug_field='name')
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')

    class Meta:
        model = FacilityEnquiry
        fields = ['name', 'email', 'mobile_number', 'facility', 'country', 'state', 'district', 'city']

class PackageEnquirySerializer(serializers.ModelSerializer):
    package = serializers.SlugRelatedField(queryset=Package.objects.all(), slug_field='name')
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    state = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')
    district = serializers.SlugRelatedField(queryset=District.objects.all(), slug_field='name')
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')

    class Meta:
        model = PackageEnquiry
        fields = ['name', 'email', 'mobile_number', 'package', 'country', 'state', 'district', 'city']
