from django.db import models
from django.contrib.auth.models import User

class Tree(models.Model):
    TREE_ID = models.IntegerField(blank=True, null=True)
    CIVIC_NUMBER = models.IntegerField(blank=True, null=True)
    STD_STREET = models.CharField(max_length=50, blank=True, null=True)
    NEIGHBOURHOOD_NAME = models.CharField(max_length=50, blank=True, null=True)
    ON_STREET = models.CharField(max_length=50, blank=True, null=True)
    ON_STREET_BLOCK = models.IntegerField(blank=True, null=True)
    STREET_SIDE_NAME = models.CharField(max_length=50, blank=True, null=True)
    ASSIGNED = models.CharField(max_length=10, blank=True, null=True)
    HEIGHT_RANGE_ID = models.IntegerField(blank=True, null=True)
    DIAMETER = models.IntegerField(blank=True, null=True)
    DATE_PLANTED = models.CharField(max_length=50, blank=True, null=True)
    PLANT_AREA = models.CharField(max_length=10, blank=True, null=True)
    ROOT_BARRIER = models.CharField(max_length=10, blank=True, null=True)
    CURB = models.CharField(max_length=10, blank=True, null=True)
    CULTIVAR_NAME = models.CharField(max_length=50, blank=True, null=True)
    SPECIES_NAME = models.CharField(max_length=50, blank=True, null=True)
    COMMON_NAME = models.CharField(max_length=50, blank=True, null=True)
    LATITUDE = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    LONGITUDE = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    
class Park(models.Model):
    ParkID = models.IntegerField(blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Official = models.CharField(max_length=50, blank=True, null=True)
    StreetNumber = models.CharField(max_length=50, blank=True, null=True)
    StreetName = models.CharField(max_length=50, blank=True, null=True)
    EWStreet = models.CharField(max_length=50, blank=True, null=True)
    NSStreet = models.CharField(max_length=50, blank=True, null=True)
    GoogleMapDest = models.CharField(max_length=50, blank=True, null=True)
    Hectare = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    NeighbourhoodName = models.CharField(max_length=50, blank=True, null=True)
    NeighbourhoodURL = models.CharField(max_length=250, blank=True, null=True)
    Advisories = models.CharField(max_length=3, blank=True, null=True)
    Facilities = models.CharField(max_length=3, blank=True, null=True)
    SpecialFeatures = models.CharField(max_length=3, blank=True, null=True)
    Washrooms = models.CharField(max_length=3, blank=True, null=True)
    LATITUDE = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    LONGITUDE = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

class FoodTree(models.Model):
    MAPID = models.CharField(max_length=10, blank=True, null=True)
    YEAR_CREATED = models.CharField(max_length=50, blank=True, null=True)
    NAME = models.CharField(max_length=50, blank=True, null=True)
    STREET_NUMBER = models.CharField(max_length=50, blank=True, null=True)
    STREET_DIRECTION = models.CharField(max_length=50, blank=True, null=True)
    STREET_NAME = models.CharField(max_length=50, blank=True, null=True)
    STREET_TYPE = models.CharField(max_length=50, blank=True, null=True)
    MERGED_ADDRESS = models.CharField(max_length=50, blank=True, null=True)
    LATITUDE = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    LONGITUDE = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    NUMBER_OF_PLOTS = models.IntegerField(blank=True, null=True)
    NUMBER_OF_FOOD_TREES = models.IntegerField(blank=True, null=True)
    NOTES = models.CharField(max_length=250, blank=True, null=True)
    FOOD_TREE_VARIETIES = models.CharField(max_length=250, blank=True, null=True)
    OTHER_FOOD_ASSETS = models.CharField(max_length=250, blank=True, null=True)
    JURISDICTION = models.CharField(max_length=50, blank=True, null=True)
    STEWARD_OR_MANAGING_ORGANIZATION = models.CharField(max_length=50, blank=True, null=True)
    PUBLIC_E_MAIL = models.CharField(max_length=100, blank=True, null=True)
    WEBSITE = models.CharField(max_length=250, blank=True, null=True)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    tree = models.ManyToManyField(Tree, blank=True)

class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    approved = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='tree_photo', blank=True)
    caption = models.TextField(blank=True)
    
    

