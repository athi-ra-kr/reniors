from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class FacilityImage(models.Model):
    facility = models.ForeignKey(Facility, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='facility_images/')

class FacilityVideo(models.Model):
    facility = models.ForeignKey(Facility, related_name='videos', on_delete=models.CASCADE)
    video_link = models.URLField()


class QuickService(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to='quickservice_images/', blank=True, null=True)

    def __str__(self):
        return self.name




class Package(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name




class Article(models.Model):
    article_name = models.CharField(max_length=255)
    article_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    article_description = models.TextField()

    def __str__(self):
        return self.article_name




class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Banner {self.id}"




class QuickServiceEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    quick_service = models.ForeignKey("QuickService", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return f"Quick Service Enquiry - {self.name}"

class FacilityEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    facility = models.ForeignKey("Facility", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
   
    
    def __str__(self):
        return f"Facility Enquiry - {self.name}"

class PackageEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    package = models.ForeignKey("Package", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
   
    
    def __str__(self):
        return f"Package Enquiry - {self.name}"










