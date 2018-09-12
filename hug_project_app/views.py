from django.shortcuts import render, get_object_or_404
from hug_project_app.models import Tree, FoodTree, Park, UserProfile
from datetime import datetime
import calendar
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django import forms


def index(request):
    return render(request, 'index.html')

def trees(request):
    response = {} #Default empty response

    trees = []
    parks = []
    food_trees = []

    if request.method == "POST":
        tree_objects = {}
        park_objects = {}
        food_tree_objects = {}

        if (request.POST['mood'] == "3"):
            food_tree_objects = FoodTree.objects.all() #TODO: Figure out how to filter out by neighbourhood

        if (request.POST['mood'] == "4"):
            park_objects = Park.objects.filter(NeighbourhoodName__contains = request.POST['park_neighbourhood'])

        if request.POST['tree_neighbourhood'] != "":
            tree_objects = Tree.objects.filter(NEIGHBOURHOOD_NAME__exact = request.POST["tree_neighbourhood"])

            if request.POST['mood'] not in ["", "3", "4"]:
                #TODO: If mood is 0, 1, 2, filter based on diameter
                tree_objects = Tree.objects.filter(DIAMETER__gt=0)

        #TODO: Handle favourites by checking if ID is in list of user favourites. Swap icon if yes
        for tree in tree_objects:
            single_tree = {}

            single_tree["name"] = tree.COMMON_NAME
            single_tree["type"] = "Tree"
            single_tree["icon"] = "/static/images/tree"
            single_tree["id"] = tree.id
            single_tree["lat"] = tree.LATITUDE
            single_tree["lon"] = tree.LONGITUDE
            single_tree["neighbourhood"] = tree.NEIGHBOURHOOD_NAME
            single_tree["diameter"] = tree.DIAMETER
            single_tree["details"] = "TODO"
            single_tree["TREE_ID"] = tree.TREE_ID

            trees.append(single_tree)

        for park in park_objects:
            single_park = {}
            single_park["name"] = park.Name
            single_park["type"] = "Park"
            single_park["icon"] = "/static/images/park" #TODO: Not sure is this is correct way to call icon from google marker
            single_park["id"] = park.id
            single_park["lat"] = park.LATITUDE
            single_park["lon"] = park.LONGITUDE
            single_park["neighbourhood"] = park.NeighbourhoodName
            single_park["details"] = "TODO"
            single_park["ParkID"] = tree.ParkID

            parks.append(single_park)

        for food_tree in food_tree_objects:
            single_tree = {}

            single_tree["name"] = food_tree.Name
            single_tree["type"] = "FoodTree"
            single_tree["icon"] = "/static/images/fruit-tree" #TODO: Not sure is this is correct way to call icon from google marker
            single_tree["id"] = food_tree.id
            single_tree["lat"] = food_tree.LATITUDE
            single_tree["lon"] = food_tree.LONGITUDE
            single_tree["details"] = "TODO"
            single_tree["MAPID"] = food_tree.MAPID

            food_trees.append(single_tree)

    all_trees = trees + parks + food_trees

    responseData = dict(enumerate(all_trees))

    return JsonResponse(responseData)

def about(request):
    return render(request, 'about.html')


def tree_detail(request, id):
    context_dict = {}
    try:
        tree = Tree.objects.get(id__exact=id)
        context_dict['tree_id'] = tree.TREE_ID
        context_dict['common_name'] = tree.COMMON_NAME
        context_dict['diameter'] = tree.DIAMETER

        # get and break date apart
        date = tree.DATE_PLANTED
        year = int(str(date)[:4])
        month = int(str(date)[4:6])
        day = int(str(date)[6:8])

        # get current date to find age of tree
        today = datetime.today()
        current_year = today.year
        age = current_year - year

        # get name of the month eg: December rather than 12
        month_name = calendar.month_name[month]

        # birthdate eg: December 12, 1979 (39 years old)
        context_dict['plant_date'] = month_name + ' ' + str(day) + ', ' + str(year) + ' (' + str(age) + ' years)'

        # address eg: 2799 W 23rd Av
        address_number = tree.CIVIC_NUMBER
        street = tree.STD_STREET
        context_dict['address'] = str(address_number) + ' ' + street
        context_dict['neighbourhood'] = tree.NEIGHBOURHOOD_NAME
    except Tree.DoesNotExist:
        pass
    return render(request, 'tree_detail.html', context_dict)


def park_detail(request, id):
    context_dict = {}
    try:
        park = Park.objects.get(id__exact=id)
        context_dict['park_id'] = park.ParkID
        context_dict['park_name'] = park.Name
        # .normalize() strips trailing zeroes off 2.8900 becomes 2.89
        context_dict['park_size'] = park.Hectare.normalize()
        park_address_number = park.StreetNumber
        park_street = park.StreetName
        context_dict['park_address'] = str(park_address_number) + ' ' + park_street
        context_dict['park_neighbourhood'] = park.NeighbourhoodName
    except Park.DoesNotExist:
        pass
    return render(request, 'tree_detail.html', context_dict)


def food_tree_detail(request, id):
    context_dict = {}
    try:
        food = FoodTree.objects.get(id__exact=id)
        context_dict['food_id'] = food.MAPID
        context_dict['garden_name'] = food.NAME
        context_dict['year_created'] = food.YEAR_CREATED
        # today = datetime.today()
        # current_year = today.year
        # garden_age = current_year - food.YEAR_CREATED
        # context_dict['garden_age'] = str(garden_age)
        context_dict['number_of_trees'] = food.NUMBER_OF_FOOD_TREES
        context_dict['food_varieties'] = food.FOOD_TREE_VARIETIES
        context_dict['garden_address'] = food.MERGED_ADDRESS
        # Need to create neighbourhood field to Community
        # Garden data set and add data manually
        # context_dict['garden_neighbourhood'] = food.Neighbourhood
    except FoodTree.DoesNotExist:
        pass
    return render(request, 'tree_detail.html', context_dict)

class HugUserCreationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    fname = forms.CharField(label='First Name', max_length=100)
    lname = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput())


def register(request):

    status = 'fail'

    if request.method == "POST":
        form = HugUserCreationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('rpassword')
            firstname = form.cleaned_data.get('fname')
            lastname = form.cleaned_data.get('lname')
            username = form.cleaned_data.get('username')

            # We'll need to add first/last to a new profile
            user = User.objects.create_user(username, email, raw_password)

            user = authenticate(username=username, password=raw_password, email=email, firstname=firstname, lastname=lastname)
            login(request, user)
            status = 'success'
    return JsonResponse({'status': status})


def favourites(request):
    return render(request, 'favourites.html')
