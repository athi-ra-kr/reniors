from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API Documentation with Swagger",
    ),
    public=True,
)


router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'cities', CityViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'quick-services', QuickServiceViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'quick-service-enquiries', QuickServiceEnquiryViewSet)
router.register(r'facility-enquiries', FacilityEnquiryViewSet)
router.register(r'package-enquiries', PackageEnquiryViewSet)



# URL patterns
urlpatterns = [
    path("adminpannel/", views.adminpannel, name="adminpannel"),

    # Country URLs
    path("country/list/", views.list_country, name="list_country"),
    path("country/add/", views.add_country, name="add_country"),
    path("country/edit/<int:country_id>/", views.edit_country, name="edit_country"),
    path("country/delete/<int:country_id>/", views.delete_country, name="delete_country"),

    # State URLs
    path("state/list/", views.list_state, name="list_state"),
    path("state/add/", views.add_state, name="add_state"),
    path("state/edit/<int:state_id>/", views.edit_state, name="edit_state"),
    path("state/delete/<int:state_id>/", views.delete_state, name="delete_state"),

    # District URLs
    path("district/list/", views.list_district, name="list_district"),
    path("district/add/", views.add_district, name="add_district"),
    path("district/edit/<int:district_id>/", views.edit_district, name="edit_district"),
    path("district/delete/<int:district_id>/", views.delete_district, name="delete_district"),

    # City URLs
    path("city/list/", views.list_city, name="list_city"),
    path("city/add/", views.add_city, name="add_city"),
    path("city/edit/<int:city_id>/", views.edit_city, name="edit_city"),
    path("city/delete/<int:city_id>/", views.delete_city, name="delete_city"),

    # Facility URLs
    path("list_facilities/", views.list_facilities, name="list_facilities"),
    path("facility/add/", views.create_facility, name="create_facility"),
    path("facility/edit/<int:facility_id>/", views.edit_facility, name="edit_facility"),
    path("facility/delete/<int:facility_id>/", views.delete_facility, name="delete_facility"),

    # Quick Service URLs
    path("quickservice/list/", views.list_quick_services, name="list_quick_services"),
    path("quickservice/add/", views.add_quick_service, name="add_quick_service"),
    path("quickservice/edit/<int:service_id>/", views.edit_quick_service, name="edit_quick_service"),
    path("quickservice/delete/<int:service_id>/", views.delete_quick_service, name="delete_quick_service"),

    # Package URLs
    path("package/list/", views.package_list, name="package_list"),
    path("package/add/", views.add_package, name="add_package"),
    path("package/edit/<int:package_id>/", views.edit_package, name="edit_package"),
    path("package/delete/<int:package_id>/", views.delete_package, name="delete_package"),

    # Article URLs
    path("article/list/", views.list_articles, name="list_articles"),
    path("article/add/", views.add_article, name="add_article"),
    path("article/edit/<int:article_id>/", views.edit_article, name="edit_article"),
    path("article/delete/<int:article_id>/", views.delete_article, name="delete_article"),

    # Banner URLs
    path("banner/list/", views.banner_list, name="banner_list"),
    path("banner/add/", views.add_banner, name="add_banner"),
    path("banner/edit/<int:banner_id>/", views.edit_banner, name="edit_banner"),
    path("banner/delete/<int:banner_id>/", views.delete_banner, name="delete_banner"),

    # Quick Service Enquiry URLs
    path("quickservice-enquiry/list/", views.quick_service_enquiry_list, name="quick_service_enquiry_list"),
    path("quickservice-enquiry/add/", views.quick_service_enquiry_add, name="quick_service_enquiry_add"),
    path("quickservice-enquiry/edit/<int:enquiry_id>/", views.quick_service_enquiry_edit, name="quick_service_enquiry_edit"),
    path("quickservice-enquiry/delete/<int:enquiry_id>/", views.quick_service_enquiry_delete, name="quick_service_enquiry_delete"),

    # Facility Enquiry URLs
    path("facility-enquiry/list/", views.facility_enquiry_list, name="facility_enquiry_list"),
    path("facility-enquiry/add/", views.facility_enquiry_add, name="facility_enquiry_add"),
    path("facility-enquiry/edit/<int:enquiry_id>/", views.facility_enquiry_edit, name="facility_enquiry_edit"),
    path("facility-enquiry/delete/<int:enquiry_id>/", views.facility_enquiry_delete, name="facility_enquiry_delete"),

    # Package Enquiry URLs
    path("package-enquiry/list/", views.package_enquiry_list, name="package_enquiry_list"),
    path("package-enquiry/add/", views.package_enquiry_add, name="package_enquiry_add"),
    path("package-enquiry/edit/<int:enquiry_id>/", views.package_enquiry_edit, name="package_enquiry_edit"),
    path("package-enquiry/delete/<int:enquiry_id>/", views.package_enquiry_delete, name="package_enquiry_delete"),
    path('',views.admin_login, name='admin_login'),
    path('admin-logout/',views.admin_logout, name='admin_logout'),

    # API Routes
    path("api/", include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    

    
]
