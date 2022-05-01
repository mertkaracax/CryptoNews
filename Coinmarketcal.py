from logging import error
import requests
import json

url = "https://developers.coinmarketcal.com/v1/events"
querystring = {'max':'30', 'sortBy': 'created_desc',  'showOnly': 'significant_events'}#'coins':'icp'
payload = ""
headers = {
    'x-api-key': "rA8kiOqu7V7U3rPWkwgis296bua20EcDgPoo0dPj",
    'Accept-Encoding': "deflate, gzip",
    'Accept': "application/json"
}
try:
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print('\n****REQUEST SUCCEED****')
except(error):
    print("aa",error)

res = json.loads(response.text)
# print(res)
eventArray = res.get('body')
for event in eventArray:
    print("\nCoins:",end=' ')
    for coin in event.get('coins'):
        print(coin.get('symbol'), end=' ')
    print() #for new line
    print("EVENT:",(event.get('title')).get('en'))
    datePreFormat = event.get('created_date')[0:10]
    print("Created Date:",datePreFormat[8:10]+'-'+datePreFormat[5:7]+'-'+datePreFormat[0:4])
    datePreFormat = event.get('date_event')[0:10]
    print("Event Date:",datePreFormat[8:10]+'-'+datePreFormat[5:7]+'-'+datePreFormat[0:4])
    print("Source:",event.get('source'))
    print('--------------')
    

# Writing data to a txt file
# file = open('NEWS.txt','w')
# for event in eventArray:
#     file.write("\nCoins: ")
#     for coin in event.get('coins'):
#         file.write(coin.get('symbol')+' ')
#     file.write('\n') #for new line
#     file.write("EVENT: "+(event.get('title')).get('en')+'\n')
#     datePreFormat = event.get('created_date')[0:10]
#     file.write("Created Date: "+datePreFormat[8:10]+'-'+datePreFormat[5:7]+'-'+datePreFormat[0:4]+'\n')
#     datePreFormat = event.get('date_event')[0:10]
#     file.write("Event Date: "+datePreFormat[8:10]+'-'+datePreFormat[5:7]+'-'+datePreFormat[0:4]+'\n')
#     file.write("Source: "+event.get('source')+'\n')
#     file.write('--------------')
input() # For avoiding from autoclose 