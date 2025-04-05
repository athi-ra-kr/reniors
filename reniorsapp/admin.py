from django.contrib import admin
from .models import Country,State,District,City,Facility,FacilityImage,FacilityVideo,QuickService,Package,Banner,QuickServiceEnquiry,FacilityEnquiry,PackageEnquiry

admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Facility)
admin.site.register(FacilityImage)
admin.site.register(FacilityVideo)
admin.site.register(QuickService)
admin.site.register(Package)
admin.site.register(Banner)
admin.site.register(QuickServiceEnquiry)
admin.site.register(FacilityEnquiry)
admin.site.register(PackageEnquiry)


