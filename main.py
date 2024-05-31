# lETS START IMPORTING THE MODULES
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
import folium

# our sexy banner funcation

def banner():
  font = """


   /$$$$$$$  /$$                     /$$             /$$   /$$             /$$           /$$   /$$ /$$                                                                                            
  | $$__  $$| $$                    | $$            | $$  | $$            | $$          | $$$ | $$|__/                                                                                            
  | $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$      | $$  | $$  /$$$$$$  /$$$$$$        | $$$$| $$ /$$ /$$$$$$$  /$$  /$$$$$$                                                                     
  | $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/      | $$$$$$$$ |____  $$|_  $$_/        | $$ $$ $$| $$| $$__  $$|__/ |____  $$                                                                    
  | $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/       | $$__  $$  /$$$$$$$  | $$          | $$  $$$$| $$| $$  \ $$ /$$  /$$$$$$$                                                                    
  | $$  \ $$| $$ /$$__  $$| $$      | $$_  $$       | $$  | $$ /$$__  $$  | $$ /$$      | $$\  $$$| $$| $$  | $$| $$ /$$__  $$                                                                    
  | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$      | $$  | $$|  $$$$$$$  |  $$$$/      | $$ \  $$| $$| $$  | $$| $$|  $$$$$$$                                                                    
  |_______/ |__/ \_______/ \_______/|__/  \__/      |__/  |__/ \_______/   \___/        |__/  \__/|__/|__/  |__/| $$ \_______/                                                                    
                                                                                                           /$$  | $$                                                                              
                                                                                                          |  $$$$$$/                                                                              
                                                                                                           \______/                                                                               
   /$$$$$$$  /$$                                           /$$   /$$                         /$$                                 /$$$$$$$$                           /$$                          
  | $$__  $$| $$                                          | $$$ | $$                        | $$                                |__  $$__/                          | $$                          
  | $$  \ $$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$          | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
  | $$$$$$$/| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
  | $$____/ | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/         | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
  | $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$               | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
  | $$      | $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$               | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
  |__/      |__/  |__/ \______/ |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/               |__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/      

coded by: @blackhatninja
mentained by: @blackhatninja
"""
  print(font)
if __name__ == "__main__":
  banner()
#geocoder api key from the website get it for free !
KEY = "7085e81373e642669ec24b701a6c6ea3"

number = input("Enter the number you want to track with the country code \n (example : +91xxxxxxxxxx): ")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(KEY)
query = str(location)
result = geocoder.geocode(query)

#Now we will print the results 

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print("Black Hat Ninjas are finding your Target's location.........")

print(lat, lng)

#Now we will save the map in a .html file

myMap = folium.Map(location = [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("myLocation.html")

#end of the fucking program
#support blackhatninjas
