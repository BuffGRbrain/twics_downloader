import requests
import json
#Modify the config.json before executing.
#The folder destinatio must exist.
#Pending unzip all files, this has to be done manually.
#Use your own path for the config file
f = open("your_Path/config.json")
data = json.load(f)
print(data)
initial_twic_2download = data["initial_twic_2download"]
final_twic_2download = data["final_twic_2download"]
file_folder = data["file_folder"]
f.close()


def get_twics(initial_twic_2download:int,final_twic_2download:int,file_folder:str)->None:
    total_twics_2download = final_twic_2download-initial_twic_2download+1
    print(total_twics_2download)
    for i in range(0,total_twics_2download):
        counter = initial_twic_2download+i
        url = 'https://theweekinchess.com/zips/twic{num}g.zip'.format(num = counter)
        print(url)
        twic = requests.get(url,headers={"User-Agent": "XY"})
        open('{folder}twic{num_file}.zip'.format(num_file = counter,folder = file_folder), 'wb').write(twic.content) 
    return None


get_twics(initial_twic_2download,final_twic_2download,file_folder)