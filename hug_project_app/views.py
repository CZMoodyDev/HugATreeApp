from django.shortcuts import render, get_object_or_404
from hug_project_app.models import Tree

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
