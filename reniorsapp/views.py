from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
import os
from rest_framework import viewsets
from .models import (
    Country, State, District, City, Facility, QuickService, Package, Article, Banner,
    QuickServiceEnquiry, FacilityEnquiry, PackageEnquiry, FacilityImage, FacilityVideo
)
from .serializers import (
    CountrySerializer, StateSerializer, DistrictSerializer, CitySerializer, FacilitySerializer,
    QuickServiceSerializer, PackageSerializer, ArticleSerializer, BannerSerializer,
    QuickServiceEnquirySerializer, FacilityEnquirySerializer, PackageEnquirySerializer
)
from functools import wraps

# Custom decorator to enforce admin authentication
def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('admin_logged_in', False):
            return redirect('admin_login')  # Redirect to login if not authenticated
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Admin panel
@admin_required
def adminpannel(request):
    return render(request, 'adminpannel.html')

# Country views
@admin_required
def add_country(request):
    if request.method == 'POST':
        country_name = request.POST.get('name')
        if country_name:
            Country.objects.create(name=country_name)
            return redirect('list_country')
    return render(request, 'add_country.html')

@admin_required
def list_country(request):
    countries = Country.objects.all()
    return render(request, 'list_country.html', {'countries': countries})

@admin_required
def edit_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            country.name = new_name
            country.save()
            return redirect('list_country')
    return render(request, 'edit_country.html', {'country': country})

@admin_required
def delete_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    country.delete()
    return redirect('list_country')

# State views
@admin_required
def add_state(request):
    if request.method == 'POST':
        state_name = request.POST.get('name')
        if state_name:
            State.objects.create(name=state_name)
            return redirect('list_state')
    return render(request, 'add_state.html')

@admin_required
def list_state(request):
    states = State.objects.all()
    return render(request, 'list_state.html', {'states': states})

@admin_required
def edit_state(request, state_id):
    state = get_object_or_404(State, id=state_id)
    if request.method == 'POST':
        state.name = request.POST.get('name')
        state.save()
        return redirect('list_state')
    return render(request, 'edit_state.html', {'state': state})

@admin_required
def delete_state(request, state_id):
    state = get_object_or_404(State, id=state_id)
    state.delete()
    return redirect('list_state')

# District views
@admin_required
def list_district(request):
    districts = District.objects.all()
    return render(request, 'list_district.html', {'districts': districts})

@admin_required
def add_district(request):
    if request.method == 'POST':
        name = request.POST['name']
        District.objects.create(name=name)
        return redirect('list_district')
    return render(request, 'add_district.html')

@admin_required
def edit_district(request, district_id):
    district = get_object_or_404(District, id=district_id)
    if request.method == 'POST':
        district.name = request.POST['name']
        district.save()
        return redirect('list_district')
    return render(request, 'edit_district.html', {'district': district})

@admin_required
def delete_district(request, district_id):
    district = get_object_or_404(District, id=district_id)
    district.delete()
    return redirect('list_district')

# City views
@admin_required
def add_city(request):
    if request.method == 'POST':
        city_name = request.POST.get('name')
        if city_name:
            City.objects.create(name=city_name)
            return redirect('list_city')
    return render(request, 'add_city.html')

@admin_required
def list_city(request):
    cities = City.objects.all()
    return render(request, 'list_city.html', {'cities': cities})

@admin_required
def edit_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    if request.method == 'POST':
        city.name = request.POST.get('name')
        city.save()
        return redirect('list_city')
    return render(request, 'edit_city.html', {'city': city})

@admin_required
def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect('list_city')

# Facility views
@admin_required
def create_facility(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country_id = request.POST.get('country')
        state_id = request.POST.get('state')
        district_id = request.POST.get('district')
        city_id = request.POST.get('city')
        description = request.POST.get('description')
        images = request.FILES.getlist('images[]')
        videos = request.POST.getlist('videos[]')

        facility = Facility.objects.create(
            name=name,
            country_id=country_id,
            state_id=state_id,
            district_id=district_id,
            city_id=city_id,
            description=description
        )

        for image in images[:10]:
            FacilityImage.objects.create(facility=facility, image=image)

        for video in videos[:10]:
            if video.strip():
                FacilityVideo.objects.create(facility=facility, video_link=video)

        return redirect('list_facilities')

    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()

    return render(request, 'create_facility.html', {
        'countries': countries,
        'states': states,
        'districts': districts,
        'cities': cities
    })

@admin_required
def list_facilities(request):
    facility_list = Facility.objects.all().prefetch_related('images', 'videos').order_by('-id')
    paginator = Paginator(facility_list, 4)
    page_number = request.GET.get('page')
    facilities = paginator.get_page(page_number)
    return render(request, 'list_facilities.html', {'facilities': facilities})

@admin_required
def edit_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        facility.name = request.POST.get('name')
        facility.country_id = request.POST.get('country')
        facility.state_id = request.POST.get('state')
        facility.district_id = request.POST.get('district')
        facility.city_id = request.POST.get('city')
        facility.description = request.POST.get('description')
        facility.save()

        new_images = request.FILES.getlist('images[]')
        if new_images:
            FacilityImage.objects.filter(facility=facility).delete()
            for image in new_images[:10]:
                FacilityImage.objects.create(facility=facility, image=image)

        new_videos = request.POST.getlist('videos')
        if new_videos:
            FacilityVideo.objects.filter(facility=facility).delete()
            for video in new_videos[:10]:
                if video.strip():
                    FacilityVideo.objects.create(facility=facility, video_link=video)

        return redirect('list_facilities')

    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    images = FacilityImage.objects.filter(facility=facility)
    videos = FacilityVideo.objects.filter(facility=facility)

    return render(request, 'edit_facility.html', {
        'facility': facility,
        'countries': countries,
        'states': states,
        'districts': districts,
        'cities': cities,
        'images': images,
        'videos': videos
    })

@admin_required
def delete_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    facility.delete()
    return redirect('list_facilities')

# Quick Service views
@admin_required
def list_quick_services(request):
    services = QuickService.objects.all()
    return render(request, 'quickservicelist.html', {'services': services})

@admin_required
def add_quick_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        if name:
            QuickService.objects.create(name=name, image=image)
            return redirect('list_quick_services')
    return render(request, 'quickserviceadd.html')

@admin_required
def edit_quick_service(request, service_id):
    service = get_object_or_404(QuickService, id=service_id)
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        if name:
            service.name = name
            if image:
                service.image = image
            service.save()
            return redirect('list_quick_services')
    return render(request, 'quickserviceedit.html', {'service': service})

@admin_required
def delete_quick_service(request, service_id):
    service = get_object_or_404(QuickService, id=service_id)
    if service.image:
        service.image.delete()
    service.delete()
    return redirect('list_quick_services')

# Package views
@admin_required
def package_list(request):
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

@admin_required
def add_package(request):
    if request.method == 'POST':
        name = request.POST['name']
        details = request.POST['details']
        price = request.POST['price']
        Package.objects.create(name=name, details=details, price=price)
        return redirect('package_list')
    return render(request, 'add_package.html')

@admin_required
def edit_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        package.name = request.POST['name']
        package.details = request.POST['details']
        package.price = request.POST['price']
        package.save()
        return redirect('package_list')
    return render(request, 'edit_package.html', {'package': package})

@admin_required
def package_enquiry_delete(request, enquiry_id):
    enquiry = get_object_or_404(PackageEnquiry, id=enquiry_id)
    enquiry.delete()
    return redirect('package_enquiry_list')

# Article views
@admin_required
def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'list_articles.html', {'articles': articles})

@admin_required
def add_article(request):
    if request.method == "POST":
        article_name = request.POST.get('article_name')
        article_description = request.POST.get('article_description')
        article_image = request.FILES.get('article_image')
        if article_name and article_image and article_description:
            Article.objects.create(
                article_name=article_name,
                article_image=article_image,
                article_description=article_description
            )
            return redirect('list_articles')
    return render(request, 'add_article.html')

@admin_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.article_name = request.POST.get('article_name')
        article.article_description = request.POST.get('article_description')
        if 'article_image' in request.FILES:
            article.article_image = request.FILES['article_image']
        article.save()
        return redirect('list_articles')
    return render(request, 'edit_article.html', {'article': article})

@admin_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('list_articles')

# Banner views
@admin_required
def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'banner_list.html', {'banners': banners})

@admin_required
def add_banner(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        Banner.objects.create(image=image)
        return redirect('banner_list')
    return render(request, 'add_banner.html')

@admin_required
def edit_banner(request, banner_id):
    banner = get_object_or_404(Banner, id=banner_id)
    if request.method == "POST" and request.FILES.get('image'):
        if banner.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(banner.image)))
        banner.image = request.FILES['image']
        banner.save()
        return redirect('banner_list')
    return render(request, 'edit_banner.html', {'banner': banner})

@admin_required
def delete_banner(request, banner_id):
    banner = get_object_or_404(Banner, id=banner_id)
    if banner.image:
        os.remove(os.path.join(settings.MEDIA_ROOT, str(banner.image)))
    banner.delete()
    return redirect('banner_list')

# Quick Service Enquiry views
@admin_required
def quick_service_enquiry_list(request):
    enquiry_list = QuickServiceEnquiry.objects.all().order_by('-id')
    paginator = Paginator(enquiry_list, 5)
    page_number = request.GET.get('page')
    enquiries = paginator.get_page(page_number)
    return render(request, "quick_service_enquiry_list.html", {"enquiries": enquiries})

@admin_required
def quick_service_enquiry_add(request):
    quick_services = QuickService.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    if request.method == "POST":
        QuickServiceEnquiry.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            mobile_number=request.POST["mobile_number"],
            quick_service_id=request.POST["quick_service"],
            country_id=request.POST.get("country"),
            state_id=request.POST.get("state"),
            district_id=request.POST.get("district"),
            city_id=request.POST.get("city")
        )
        return redirect("quick_service_enquiry_list")
    return render(request, "quick_service_enquiry_form.html", {
        "quick_services": quick_services,
        "countries": countries,
        "states": states,
        "districts": districts,
        "cities": cities
    })

@admin_required
def quick_service_enquiry_edit(request, enquiry_id):
    enquiry = get_object_or_404(QuickServiceEnquiry, id=enquiry_id)
    quick_services = QuickService.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    if request.method == "POST":
        enquiry.name = request.POST["name"]
        enquiry.email = request.POST["email"]
        enquiry.mobile_number = request.POST["mobile_number"]
        enquiry.quick_service_id = request.POST["quick_service"]
        enquiry.country_id = request.POST.get("country")
        enquiry.state_id = request.POST.get("state")
        enquiry.district_id = request.POST.get("district")
        enquiry.city_id = request.POST.get("city")
        enquiry.save()
        return redirect("quick_service_enquiry_list")
    return render(request, "quick_service_enquiry_form.html", {
        "enquiry": enquiry,
        "quick_services": quick_services,
        "countries": countries,
        "states": states,
        "districts": districts,
        "cities": cities
    })

@admin_required
def quick_service_enquiry_delete(request, enquiry_id):
    enquiry = get_object_or_404(QuickServiceEnquiry, id=enquiry_id)
    enquiry.delete()
    return redirect("quick_service_enquiry_list")

# Facility Enquiry views
@admin_required
def facility_enquiry_list(request):
    enquiry_list = FacilityEnquiry.objects.all().order_by('-id')
    paginator = Paginator(enquiry_list, 5)
    page_number = request.GET.get('page')
    enquiries = paginator.get_page(page_number)
    return render(request, "facility_enquiry_list.html", {"enquiries": enquiries})

@admin_required
def facility_enquiry_add(request):
    facilities = Facility.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_number = request.POST.get("mobile_number")
        facility_id = request.POST.get("facility")
        country_id = request.POST.get("country")
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        city_id = request.POST.get("city")
        facility = Facility.objects.get(id=facility_id) if facility_id else None
        country = Country.objects.get(id=country_id) if country_id else None
        state = State.objects.get(id=state_id) if state_id else None
        district = District.objects.get(id=district_id) if district_id else None
        city = City.objects.get(id=city_id) if city_id else None
        FacilityEnquiry.objects.create(
            name=name, email=email, mobile_number=mobile_number,
            facility=facility, country=country, state=state,
            district=district, city=city
        )
        return redirect("facility_enquiry_list")
    return render(request, "facility_enquiry_form.html", {
        "facilities": facilities,
        "countries": countries,
        "states": states,
        "districts": districts,
        "cities": cities
    })

@admin_required
def facility_enquiry_edit(request, enquiry_id):
    enquiry = get_object_or_404(FacilityEnquiry, id=enquiry_id)
    facilities = Facility.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    if request.method == "POST":
        enquiry.name = request.POST.get("name")
        enquiry.email = request.POST.get("email")
        enquiry.mobile_number = request.POST.get("mobile_number")
        facility_id = request.POST.get("facility")
        country_id = request.POST.get("country")
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        city_id = request.POST.get("city")
        enquiry.facility = Facility.objects.get(id=facility_id) if facility_id else None
        enquiry.country = Country.objects.get(id=country_id) if country_id else None
        enquiry.state = State.objects.get(id=state_id) if state_id else None
        enquiry.district = District.objects.get(id=district_id) if district_id else None
        enquiry.city = City.objects.get(id=city_id) if city_id else None
        enquiry.save()
        return redirect("facility_enquiry_list")
    return render(request, "facility_enquiry_form.html", {
        "enquiry": enquiry,
        "facilities": facilities,
        "countries": countries,
        "states": states,
        "districts": districts,
        "cities": cities
    })

@admin_required
def facility_enquiry_delete(request, enquiry_id):
    enquiry = get_object_or_404(FacilityEnquiry, id=enquiry_id)
    enquiry.delete()
    return redirect("facility_enquiry_list")

# Package Enquiry views
@admin_required
def package_enquiry_list(request):
    enquiry_list = PackageEnquiry.objects.all().order_by('-id')
    paginator = Paginator(enquiry_list, 5)
    page_number = request.GET.get('page')
    enquiries = paginator.get_page(page_number)
    return render(request, "package_enquiry_list.html", {"enquiries": enquiries})

@admin_required
def package_enquiry_add(request):
    packages = Package.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_number = request.POST.get("mobile_number")
        package_id = request.POST.get("package")
        country_id = request.POST.get("country")
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        city_id = request.POST.get("city")
        package = Package.objects.get(id=package_id) if package_id else None
        country = Country.objects.get(id=country_id) if country_id else None
        state = State.objects.get(id=state_id) if state_id else None
        district = District.objects.get(id=district_id) if district_id else None
        city = City.objects.get(id=city_id) if city_id else None
        PackageEnquiry.objects.create(
            name=name, email=email, mobile_number=mobile_number,
            package=package, country=country, state=state,
            district=district, city=city
        )
        return redirect("package_enquiry_list")
    return render(request, "package_enquiry_form.html", {
        "packages": packages,
        "countries": countries,
        "states": states,
        "districts": districts,
        "cities": cities
    })

@admin_required
def package_enquiry_edit(request, enquiry_id):
    enquiry = get_object_or_404(PackageEnquiry, id=enquiry_id)
    packages = Package.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    if request.method == "POST":
        enquiry.name = request.POST.get("name")
        enquiry.email = request.POST.get("email")
        enquiry.mobile_number = request.POST.get("mobile_number")
        package_id = request.POST.get("package")
        country_id = request.POST.get("country")
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        city_id = request.POST.get("city")
        enquiry.package = Package.objects.get(id=package_id) if package_id else None
        enquiry.country = Country.objects.get(id=country_id) if country_id else None
        enquiry.state = State.objects.get(id=state_id) if state_id else None
        enquiry.district = District.objects.get(id=district_id) if district_id else None
        enquiry.city = City.objects.get(id=city_id) if city_id else None
        enquiry.save()
        return redirect("package_enquiry_list")
    return render(request, "package_enquiry_form.html", {
        "enquiry": enquiry,
        "packages": packages,
        "countries": countries,
        "states": states,
        "districts": districts,
        "cities": cities
    })

@admin_required
def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    package.delete()
    return redirect('package_list')

# Authentication views (no decorator needed)
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'reniors':
            request.session['admin_logged_in'] = True
            return redirect('list_facilities')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')




from rest_framework import viewsets
from .models import *
from .serializers import *

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class QuickServiceViewSet(viewsets.ModelViewSet):
    queryset = QuickService.objects.all()
    serializer_class = QuickServiceSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class QuickServiceEnquiryViewSet(viewsets.ModelViewSet):
    queryset = QuickServiceEnquiry.objects.all()
    serializer_class = QuickServiceEnquirySerializer

class FacilityEnquiryViewSet(viewsets.ModelViewSet):
    queryset = FacilityEnquiry.objects.all()
    serializer_class = FacilityEnquirySerializer

class PackageEnquiryViewSet(viewsets.ModelViewSet):
    queryset = PackageEnquiry.objects.all()
    serializer_class = PackageEnquirySerializer


























