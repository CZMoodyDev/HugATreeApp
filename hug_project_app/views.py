from django.shortcuts import render, get_object_or_404
from hug_project_app.models import Tree
from datetime import datetime
import calendar


def index(request):
    trees = []

    tree_objects = Tree.objects.all()

    for tree in tree_objects:
        single_tree = {}

        single_tree["name"] = tree.COMMON_NAME
        single_tree["type"] = "Tree"
        single_tree["icon"] = "TODO"
        single_tree["id"] = tree.id
        single_tree["lat"] = tree.LATITUDE
        single_tree["lon"] = tree.LONGITUDE
        single_tree["neighbourhood"] = tree.NEIGHBOURHOOD_NAME
        single_tree["diameter"] = tree.DIAMETER
        single_tree["details"] = "TODO"
        single_tree["TREE_ID"] = tree.TREE_ID

        trees.append(single_tree)

    return render(request, 'index.html', {"trees": trees})

def about(request):
    return render(request, 'about.html')

def tree_detail(request):
    context_dict = {}
    try:
        # TODO: Curtis add TREE_ID parameter where 'id__exact=12' is
        # (The tree_id is a parameter passed to this view via the index page when someone clicks on a tree link)
        # This: tree = Tree.objects.get(id__exact=12) should be replaced with something like
        # tree = Tree.objects.get(id=id)
        tree = Tree.objects.get(id__exact=12)
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
        context_dict['birthdate'] = month_name + ' ' + str(day) + ', ' + str(year) + ' (' + str(age) + ' years old)'

        # address eg: 2799 W 23rd Av
        address_number = tree.CIVIC_NUMBER
        street = tree.STD_STREET
        context_dict['address'] = str(address_number) + ' ' + street

        context_dict['neighbourhood'] = tree.NEIGHBOURHOOD_NAME

    except Tree.DoesNotExist:
        pass
    return render(request, 'tree_detail.html', context_dict)


def favourites(request):
    return render(request, 'favourites.html')
