#!/usr/bin/python

import subprocess
from pymongo import MongoClient

# setup
client = MongoClient('127.0.0.1:27017')
db = client.exampledb

# insert dummy data
entries = [
  {
    "index": 0,
    "guid": "6aea0421-196f-4ff4-a699-e44ab7e5f848",
    "isActive": False,
    "balance": "$3,451.48",
    "age": 32,
    "eyeColor": "blue",
    "name": "Rhonda Wall",
    "gender": "female",
    "company": "IDETICA",
    "email": "rhondawall@idetica.com",
    "phone": "+1 (923) 564-3326",
    "address": "484 Remsen Street, Basye, District Of Columbia, 2165",
    "registered": "2019-03-28T06:24:28 -11:00",
    "latitude": 86.422523,
    "longitude": -107.727407
  },
  {
    "index": 1,
    "guid": "27e64da2-5eb1-45df-810d-65736266eaf7",
    "isActive": False,
    "balance": "$1,592.74",
    "age": 26,
    "eyeColor": "green",
    "name": "Bolton Rutledge",
    "gender": "male",
    "company": "NUTRALAB",
    "email": "boltonrutledge@nutralab.com",
    "phone": "+1 (905) 537-3455",
    "address": "740 Murdock Court, Florence, Kentucky, 1129",
    "registered": "2017-04-30T05:42:45 -10:00",
    "latitude": -39.786105,
    "longitude": -110.168496
  },
  {
    "index": 2,
    "guid": "e0b140c0-1345-4f38-ab19-e4e96ce70c17",
    "isActive": False,
    "balance": "$3,007.26",
    "age": 30,
    "eyeColor": "blue",
    "name": "Whitehead Stuart",
    "gender": "male",
    "company": "VERTON",
    "email": "whiteheadstuart@verton.com",
    "phone": "+1 (876) 507-2191",
    "address": "628 Gallatin Place, Whitestone, Wisconsin, 7096",
    "registered": "2019-03-30T10:24:30 -11:00",
    "latitude": -55.89631,
    "longitude": -67.938777
  },
  {
    "index": 3,
    "guid": "ebd63344-f3a4-4a4c-9045-3742eb24d268",
    "isActive": False,
    "balance": "$1,039.72",
    "age": 37,
    "eyeColor": "brown",
    "name": "Wood Conrad",
    "gender": "male",
    "company": "TERASCAPE",
    "email": "woodconrad@terascape.com",
    "phone": "+1 (876) 584-2140",
    "address": "644 Seaview Avenue, Westboro, Rhode Island, 8949",
    "registered": "2020-08-14T10:24:23 -10:00",
    "latitude": 68.36854,
    "longitude": -93.789759
  },
  {
    "index": 4,
    "guid": "16bfb315-4c5a-4694-8849-73b3ee8d5477",
    "isActive": False,
    "balance": "$2,466.22",
    "age": 24,
    "eyeColor": "green",
    "name": "Ebony Phillips",
    "gender": "female",
    "company": "ARCTIQ",
    "email": "ebonyphillips@arctiq.com",
    "phone": "+1 (952) 404-3472",
    "address": "564 Falmouth Street, Hall, Michigan, 2937",
    "registered": "2014-05-17T06:21:24 -10:00",
    "latitude": -17.644943,
    "longitude": -41.674618
  },
  {
    "index": 5,
    "guid": "c2d984d2-659b-41f8-988c-9cafcfe2cb9a",
    "isActive": True,
    "balance": "$1,583.21",
    "age": 34,
    "eyeColor": "brown",
    "name": "Olsen Gould",
    "gender": "male",
    "company": "JAMNATION",
    "email": "olsengould@jamnation.com",
    "phone": "+1 (807) 449-2598",
    "address": "848 Cumberland Street, Loma, Vermont, 6940",
    "registered": "2018-10-22T07:24:05 -11:00",
    "latitude": -18.916431,
    "longitude": -106.32294
  },
  {
    "index": 6,
    "guid": "8b6eebc3-6131-4a2b-8604-3e8530347298",
    "isActive": False,
    "balance": "$1,640.88",
    "age": 25,
    "eyeColor": "blue",
    "name": "Gould Mendez",
    "gender": "male",
    "company": "INRT",
    "email": "gouldmendez@inrt.com",
    "phone": "+1 (978) 592-2269",
    "address": "303 Miller Avenue, Greenbackville, Montana, 2754",
    "registered": "2019-05-28T02:50:54 -10:00",
    "latitude": -5.230598,
    "longitude": -167.137723
  },
  {
    "index": 7,
    "guid": "4ad00668-7c68-4c07-b018-ff890545b283",
    "isActive": True,
    "balance": "$1,916.69",
    "age": 33,
    "eyeColor": "green",
    "name": "Carolina Williamson",
    "gender": "female",
    "company": "XPLOR",
    "email": "carolinawilliamson@xplor.com",
    "phone": "+1 (898) 462-3038",
    "address": "889 Flatbush Avenue, Slovan, New Mexico, 4081",
    "registered": "2019-04-16T04:01:22 -10:00",
    "latitude": 14.010128,
    "longitude": 152.379504
  },
  {
    "index": 8,
    "guid": "46b7d4a8-280c-43ff-93f1-dc30937ab340",
    "isActive": True,
    "balance": "$2,540.32",
    "age": 26,
    "eyeColor": "brown",
    "name": "Spencer Oliver",
    "gender": "male",
    "company": "ACCUFARM",
    "email": "spenceroliver@accufarm.com",
    "phone": "+1 (931) 406-2700",
    "address": "314 Rapelye Street, Cliffside, Guam, 2115",
    "registered": "2016-02-26T11:47:11 -11:00",
    "latitude": 30.044149,
    "longitude": -24.308558
  },
  {
    "index": 9,
    "guid": "d94e6e53-ec82-4a50-b37e-d9cf51256039",
    "isActive": False,
    "balance": "$2,002.39",
    "age": 33,
    "eyeColor": "brown",
    "name": "Deanna Gates",
    "gender": "female",
    "company": "EPLODE",
    "email": "deannagates@eplode.com",
    "phone": "+1 (841) 487-2298",
    "address": "544 Richardson Street, Needmore, Virginia, 3264",
    "registered": "2019-12-18T03:14:34 -11:00",
    "latitude": -31.69702,
    "longitude": 60.417172
  },
  {
    "index": 10,
    "guid": "62a484e5-058e-419b-879f-4c4b669e2c69",
    "isActive": True,
    "balance": "$3,334.14",
    "age": 21,
    "eyeColor": "blue",
    "name": "Prince Palmer",
    "gender": "male",
    "company": "REALYSIS",
    "email": "princepalmer@realysis.com",
    "phone": "+1 (962) 449-2215",
    "address": "331 Columbia Place, Murillo, Iowa, 6963",
    "registered": "2020-09-12T08:35:33 -10:00",
    "latitude": 74.718805,
    "longitude": -10.49673
  },
  {
    "index": 11,
    "guid": "d6905ca4-a938-4247-9a0a-8b924ce901b8",
    "isActive": False,
    "balance": "$3,312.60",
    "age": 37,
    "eyeColor": "blue",
    "name": "Lesley Phelps",
    "gender": "female",
    "company": "BUZZWORKS",
    "email": "lesleyphelps@buzzworks.com",
    "phone": "+1 (811) 512-2244",
    "address": "990 Lewis Place, Caledonia, Massachusetts, 6079",
    "registered": "2019-04-09T07:09:27 -10:00",
    "latitude": 14.67732,
    "longitude": 145.64746
  },
  {
    "index": 12,
    "guid": "bb987357-112c-43a4-b375-d7dc34bcd09f",
    "isActive": True,
    "balance": "$3,446.22",
    "age": 32,
    "eyeColor": "blue",
    "name": "Angelina Mullins",
    "gender": "female",
    "company": "PEARLESEX",
    "email": "angelinamullins@pearlesex.com",
    "phone": "+1 (964) 435-3530",
    "address": "349 Raleigh Place, Juntura, Utah, 3264",
    "registered": "2016-11-27T03:17:00 -11:00",
    "latitude": 49.156522,
    "longitude": -175.890873
  },
  {
    "index": 13,
    "guid": "019d4252-bd39-4e7c-8c79-54d101b0e23b",
    "isActive": True,
    "balance": "$2,196.21",
    "age": 21,
    "eyeColor": "blue",
    "name": "Riddle House",
    "gender": "male",
    "company": "BRISTO",
    "email": "riddlehouse@bristo.com",
    "phone": "+1 (864) 572-2971",
    "address": "502 Lake Street, Aberdeen, Delaware, 999",
    "registered": "2020-11-26T01:03:14 -11:00",
    "latitude": 23.770064,
    "longitude": -49.583915
  },
  {
    "index": 14,
    "guid": "1844a010-be7e-49ad-a647-d18eaf0a07d2",
    "isActive": False,
    "balance": "$2,904.36",
    "age": 23,
    "eyeColor": "brown",
    "name": "Tiffany Petty",
    "gender": "female",
    "company": "ISOLOGIA",
    "email": "tiffanypetty@isologia.com",
    "phone": "+1 (931) 474-3339",
    "address": "790 Gatling Place, Matheny, Marshall Islands, 7087",
    "registered": "2020-07-06T05:13:03 -10:00",
    "latitude": 71.676901,
    "longitude": 156.363469
  },
  {
    "index": 15,
    "guid": "83c6853e-d47b-4fa8-831e-a36b7ae09e6a",
    "isActive": True,
    "balance": "$2,237.72",
    "age": 29,
    "eyeColor": "green",
    "name": "Rochelle Patterson",
    "gender": "female",
    "company": "EARTHPURE",
    "email": "rochellepatterson@earthpure.com",
    "phone": "+1 (837) 466-3362",
    "address": "617 Thames Street, Jeff, South Dakota, 2090",
    "registered": "2016-01-15T10:54:59 -11:00",
    "latitude": 43.665843,
    "longitude": 98.334513
  },
  {
    "index": 16,
    "guid": "ec2de8c9-64e4-4aeb-ae50-8c730b3757f3",
    "isActive": False,
    "balance": "$1,549.63",
    "age": 39,
    "eyeColor": "green",
    "name": "Cochran Ford",
    "gender": "male",
    "company": "EMTRAC",
    "email": "cochranford@emtrac.com",
    "phone": "+1 (949) 555-2040",
    "address": "360 Rose Street, Grapeview, Maryland, 5834",
    "registered": "2015-08-24T02:32:45 -10:00",
    "latitude": -51.482544,
    "longitude": 169.103321
  },
  {
    "index": 17,
    "guid": "3474b081-47bb-4859-b029-fe6c61450954",
    "isActive": True,
    "balance": "$1,733.37",
    "age": 24,
    "eyeColor": "brown",
    "name": "Garner Hardy",
    "gender": "male",
    "company": "QUADEEBO",
    "email": "garnerhardy@quadeebo.com",
    "phone": "+1 (962) 565-2935",
    "address": "993 Woodpoint Road, Linganore, Kansas, 7630",
    "registered": "2015-02-24T11:41:09 -11:00",
    "latitude": -69.397633,
    "longitude": 120.742058
  },
  {
    "index": 18,
    "guid": "6e2b0933-d4e7-42bb-b691-99aaca51a31f",
    "isActive": False,
    "balance": "$3,389.43",
    "age": 33,
    "eyeColor": "blue",
    "name": "Viola Melton",
    "gender": "female",
    "company": "BOILCAT",
    "email": "violamelton@boilcat.com",
    "phone": "+1 (848) 494-3814",
    "address": "473 Brown Street, Oasis, Colorado, 2133",
    "registered": "2020-08-19T08:04:58 -10:00",
    "latitude": 48.443894,
    "longitude": -110.554817
  },
  {
    "index": 19,
    "guid": "64be3ea6-e2b8-48f9-81a5-5f5b013ebbd0",
    "isActive": True,
    "balance": "$2,409.98",
    "age": 24,
    "eyeColor": "green",
    "name": "Mable Hendricks",
    "gender": "female",
    "company": "JIMBIES",
    "email": "mablehendricks@jimbies.com",
    "phone": "+1 (937) 563-2945",
    "address": "417 Whitwell Place, Norris, Maine, 1387",
    "registered": "2019-02-14T08:30:38 -11:00",
    "latitude": 30.934779,
    "longitude": 60.980889
  }
]

users = db.users
result = users.insert_many(entries)

#persist the window to view output
# input("\n Press enter to close window...")