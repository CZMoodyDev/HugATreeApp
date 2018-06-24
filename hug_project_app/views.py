from django.shortcuts import render, get_object_or_404
from hug_project_app.models import Tree
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django import forms

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
    return render(request, 'tree_detail.html')

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
            
            #We'll need to add first/last to a new profile
            user = User.objects.create_user(username, email, raw_password)
            
            user = authenticate(username=username, password=raw_password, email=email, firstname=firstname, lastname=lastname)
            login(request, user)
            status = 'success'
        
    return JsonResponse({'status': status})