from django.core.management.base import BaseCommand, CommandError
from hug_project_app.models import Tree
import os, json

class Command(BaseCommand):
    
    def handle(self, *args, **options):
    
        #Clear out old data
        Tree.objects.all().delete()
            
        #Get data set directory path
        dirname = os.path.dirname(__file__)
        relpath_to_jsons = '../../../dataset/Trees/'
        path_to_jsons = os.path.join(dirname, relpath_to_jsons)
        json_files = [pos_json for pos_json in os.listdir(path_to_jsons) if pos_json.endswith('.json')]
    
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_jsons, js)) as json_file:
                json_text = json.load(json_file)
                
                features = json_text['features']
                for idx, val in enumerate(features):
                    properties = features[idx]['properties']
                    
                    if (properties['LATITUDE'] and properties['LONGITUDE']):
                        tree = Tree()
                                       
                        tree.TREE_ID = properties['TREE_ID']
                        tree.CIVIC_NUMBER = properties['CIVIC_NUMBER']
                        tree.STD_STREET = properties['STD_STREET']
                        tree.NEIGHBOURHOOD_NAME = properties['NEIGHBOURHOOD_NAME']
                        tree.ON_STREET = properties['ON_STREET']
                        tree.ON_STREET_BLOCK = properties['ON_STREET_BLOCK']
                        tree.STREET_SIDE_NAME = properties['STREET_SIDE_NAME']
                        tree.ASSIGNED = properties['ASSIGNED']
                        tree.HEIGHT_RANGE_ID = properties['HEIGHT_RANGE_ID']
                        tree.DIAMETER = properties['DIAMETER']
                        tree.DATE_PLANTED = properties['DATE_PLANTED']
                        tree.PLANT_AREA = properties['PLANT_AREA']
                        tree.ROOT_BARRIER = properties['ROOT_BARRIER']
                        tree.CURB = properties['CURB']
                        tree.CULTIVAR_NAME = properties['CULTIVAR_NAME']
                        tree.SPECIES_NAME = properties['SPECIES_NAME']
                        tree.COMMON_NAME = properties['COMMON_NAME']
                        tree.LATITUDE = properties['LATITUDE']
                        tree.LONGITUDE = properties['LONGITUDE']
                        
                        self.stdout.write("Added tree ID " + str(tree.TREE_ID))
                        tree.save()
                    else:
                        self.stdout.write("Bad lat lon. Skipped.")   