from django.core.management.base import BaseCommand, CommandError
from hug_project_app.models import FoodTree
import os, json, string

class Command(BaseCommand):
    
    def handle(self, *args, **options):
    
        #Clear out old data
        FoodTree.objects.all().delete()
            
        #Get data set directory path
        dirname = os.path.dirname(__file__)
        relpath_to_jsons = '../../../dataset/FoodTrees/'
        path_to_jsons = os.path.join(dirname, relpath_to_jsons)
        json_files = [pos_json for pos_json in os.listdir(path_to_jsons) if pos_json.endswith('.json')]
    
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_jsons, js)) as json_file:
                json_text = json.load(json_file)
                
                for idx, val in enumerate(json_text):                
                    foodTree = FoodTree()
                                   
                    json_obj = json_text[idx]  
                    
                    #We will skip adding it if we can not plot it
                    if json_obj["LATITUDE"] and json_obj["LONGITUDE"]:
                        foodTree.MAPID = json_obj["MAPID"]
                        foodTree.YEAR_CREATED = json_obj["YEAR_CREATED"]
                        foodTree.NAME = json_obj["NAME"]
                        foodTree.STREET_NUMBER = json_obj["STREET_NUMBER"]
                        foodTree.STREET_DIRECTION = json_obj["STREET_DIRECTION"]
                        foodTree.STREET_NAME = json_obj["STREET_NAME"]
                        foodTree.STREET_TYPE = json_obj["STREET_TYPE"]
                        foodTree.MERGED_ADDRESS = json_obj["MERGED_ADDRESS"]
                        foodTree.LATITUDE = json_obj["LATITUDE"]
                        foodTree.LONGITUDE = json_obj["LONGITUDE"]   

                        numPlots = ''.join(c for c in str(json_obj["NUMBER_OF_PLOTS"]) if c.isdigit())
                        foodTree.NUMBER_OF_PLOTS = int(numPlots) if numPlots else 0
                        
                        numFoodTrees = ''.join(c for c in str(json_obj["NUMBER_OF_FOOD_TREES"]) if c.isdigit())
                        foodTree.NUMBER_OF_FOOD_TREES = int(numFoodTrees) if numFoodTrees else 0
                        foodTree.NOTES = json_obj["NOTES"]
                        
                        cleanVarieties = ''.join(i for i in json_obj["FOOD_TREE_VARIETIES"] if not i.isdigit())
                        cleanVarieties = str.replace(cleanVarieties, 'and', ',')
                        cleanVarieties = str.replace(cleanVarieties, ';', ',')
                        foodTree.FOOD_TREE_VARIETIES = cleanVarieties
                        
                        foodTree.OTHER_FOOD_ASSETS = json_obj["OTHER_FOOD_ASSETS"]
                        foodTree.JURISDICTION = json_obj["JURISDICTION"]
                        foodTree.STEWARD_OR_MANAGING_ORGANIZATION = json_obj["STEWARD_OR_MANAGING_ORGANIZATION"]
                        foodTree.PUBLIC_E_MAIL = json_obj["PUBLIC_E_MAIL"]
                        foodTree.WEBSITE = json_obj["WEBSITE"]                    
                    
                        self.stdout.write("Added food tree ID " + foodTree.MAPID)
                        foodTree.save()
                    else:
                            self.stdout.write("Bad lat lon. Skipped.")                           