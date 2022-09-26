print("\n ----EXERCICE ----")
print("\n Consist in request a temperature of 'Provincia' of Italy with API [Open Meteo].")
import requests
import json
import datetime

answer='Y'
while answer!='N':
    ins_provinc=input("insert a italian provincia :")

    print(" we take latitude and longitude by data: 'provincia.json' ")

    link_prov=r'Data\province.json'
    with open(link_prov, 'r') as f:
        provincia=json.load(f)
        

    while ins_provinc.capitalize() not in provincia:
        ins_provinc=input("Error pls insert a right provincia:")

    print("the coordinate are : ",provincia[ins_provinc.capitalize()])

    latitude=provincia[ins_provinc.capitalize()]['lat']
    longitude=provincia[ins_provinc.capitalize()]['lon']

    print("\n Now use API Open meteo that it want the coordinate of provincia")


    link_API='https://api.open-meteo.com/v1/forecast?'
    Link_tot= link_API + "latitude="+latitude+"&longitude="+longitude+"&hourly=apparent_temperature&current_weather=true"
    print("this is link of request",Link_tot)
    MeteoOpen=requests.get(Link_tot).json()

    #print(MeteoOpen)

    now = datetime.datetime.now().date()
    hour = datetime.datetime.now().strftime("%H")

    current_weather = MeteoOpen["current_weather"]["temperature"]

    ## array of time and temperature
    ap_temperature_list = MeteoOpen["hourly"]["apparent_temperature"]

    print("\n temperature now is :", ap_temperature_list[int(hour)],"°C")
    print(" winds speed is :", MeteoOpen["current_weather"]["windspeed"],"km/h")
    print(" wind direction now is :", MeteoOpen["current_weather"]["winddirection"],"°")
    answer=input(" do you want insert another provincia?[Y/N] ")