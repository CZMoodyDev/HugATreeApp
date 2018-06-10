from django.core.management.base import BaseCommand, CommandError
from hug_project_app.models import Park
import os, json, string

class Command(BaseCommand):
    
    def handle(self, *args, **options):
    
        #Clear out old data
        Park.objects.all().delete()
            
        #Get data set directory path
        dirname = os.path.dirname(__file__)
        relpath_to_jsons = '../../../dataset/Parks/'
        path_to_jsons = os.path.join(dirname, relpath_to_jsons)
        json_files = [pos_json for pos_json in os.listdir(path_to_jsons) if pos_json.endswith('.json')]
    
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_jsons, js)) as json_file:
                json_text = json.load(json_file)
                
                for idx, val in enumerate(json_text):

                    json_obj = json_text[idx]
                    
                    if json_obj["GoogleMapDest"]:
                        
                        latAndLon = [x.strip() for x in json_obj["GoogleMapDest"].split(',')]
                                              
                        if len(latAndLon) == 2:                      
                            park = Park()
                                           
                            park.ParkID = json_obj["ParkID"]
                            park.Name = json_obj["Name"]
                            park.Official = json_obj["Official"]
                            park.StreetNumber = json_obj["StreetNumber"]
                            park.StreetName = json_obj["StreetName"]
                            park.EWStreet = json_obj["EWStreet"]
                            park.NSStreet = json_obj["NSStreet"]
                            park.GoogleMapDest = json_obj["GoogleMapDest"]
                            park.Hectare = json_obj["Hectare"]
                            park.NeighbourhoodName = json_obj["NeighbourhoodName"]
                            park.NeighbourhoodURL = json_obj["NeighbourhoodURL"]
                            park.Advisories = json_obj["Advisories"]
                            park.Facilities = json_obj["Facilities"]
                            park.SpecialFeatures = json_obj["SpecialFeatures"]
                            park.Washrooms = json_obj["Washrooms"]
                            park.LATITUDE = float(latAndLon[0])
                            park.LONGITUDE = float(latAndLon[1])
                            
                            self.stdout.write("Added park ID " + str(park.ParkID))
                            park.save()
                        else:
                            self.stdout.write("Bad lat lon. Skipped.")   
                    else:
                            self.stdout.write("No GoogleMapDest. Skipped.")                    
                    