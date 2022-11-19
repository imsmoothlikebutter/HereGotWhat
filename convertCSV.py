
##https://www.youtube.com/watch?v=f3q5aM9onnc

import pandas as pd
import json
import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:adminPassword@cluster0.ivh8z2v.mongodb.net/?retryWrites=true&w=majority")
#db = client.test


#client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["HereGotWhat"]
counter = 0;

df=pd.read_csv("CSV/ListofLicensedPharmacies/listing-of-licensed-pharmacies-dec-2021-town.csv")
data = df.to_dict(orient = "records")
db.LicensedPharmacies.insert_many(data)
counter += 1
print("Licensed Pharmacies CSV converted! (",counter,")")

df=pd.read_csv("CSV/ListofSupermarkets/listing-of-supermarkets(cleaned).csv")
data = df.to_dict(orient = "records")
db.Supermarkets.insert_many(data)
counter += 1
print("Supermarkets CSV converted! (",counter,")")

df=pd.read_csv("CSV/RentalFlatsPrices/renting-out-of-flats.csv")
data = df.to_dict(orient="records")
db.RentalFlats.insert_many(data)
counter += 1
print("Rental Flats CSV converted! (",counter,")")

df = pd.read_csv("CSV/ResaleFlatPrices/resale-flat-prices-based-on-approval-date-1990-1999.csv")
data = df.to_dict(orient="records")
db.ResaleFlats1990_1999.insert_many(data)
counter += 1
print("Resale Flats 1990-1999 CSV converted! (",counter,")")

df = pd.read_csv("CSV/ResaleFlatPrices/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv")
data = df.to_dict(orient="records")
db.ResaleFlats2000_2012.insert_many(data)
counter += 1
print("Resale Flats 2000-2012 CSV converted! (",counter,")")

df = pd.read_csv("CSV/ResaleFlatPrices/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv")
data = df.to_dict(orient="records")
db.ResaleFlats2012_2014.insert_many(data)
counter += 1
print("Resale Flats 2012-2014 Onwards CSV converted! (",counter,")")

df = pd.read_csv("CSV/ResaleFlatPrices/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv")
data = df.to_dict(orient="records")
db.ResaleFlats2015_2016.insert_many(data)
counter += 1
print("Resale Flats 2015-2016 CSV converted! (",counter,")")

df = pd.read_csv("CSV/ResaleFlatPrices/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv")
data = df.to_dict(orient="records")
db.ResaleFlats2017onwards.insert_many(data)
counter += 1
print("Resale Flats 2017 Onwards CSV converted! (",counter,")")

df = pd.read_csv("CSV/SchoolDirectoryandInformation/co-curricular-activities-ccas.csv")
data = df.to_dict(orient="records")
db.SchoolCCAs.insert_many(data)
counter += 1
print("School CCAs CSV converted! (",counter,")")

df = pd.read_csv("CSV/SchoolDirectoryandInformation/general-information-of-schools.csv")
data = df.to_dict(orient="records")
db.SchoolGeneralInformation.insert_many(data)
counter += 1
print("School General Information CSV converted! (",counter,")")

df = pd.read_csv("CSV/SchoolDirectoryandInformation/moe-programmes.csv")
data = df.to_dict(orient="records")
db.MOEProgrammes.insert_many(data)
counter += 1
print("MOE Programmes CSV converted! (",counter,")")

df = pd.read_csv("CSV/SchoolDirectoryandInformation/school-distinctive-programmes.csv")
data = df.to_dict(orient="records")
db.SchoolDistinctiveProgrammes.insert_many(data)
counter += 1
print("School Distinctive Programmes CSV converted! (",counter,")")

df = pd.read_csv("CSV/SchoolDirectoryandInformation/subjects-offered.csv")
data = df.to_dict(orient="records")
db.SchoolSubjectsOffered.insert_many(data)
counter += 1
print("School Subjects Offered CSV converted! (",counter,")")
########
df = pd.read_csv("CSV/PopulationSize/estimated-percentage-of-singapore-resident-population-in-hdb-flats.csv")
data = df.to_dict(orient="records")
db.SGHDBPopulationByPercentage.insert_many(data)
counter += 1
print("Population of Singapore Residents in HDB by % CSV converted! (",counter,")")

df = pd.read_csv("CSV/PopulationSize/estimated-resident-population-in-hdb-flats-by-town.csv")
data = df.to_dict(orient="records")
db.SGHDBPopulationEstimate.insert_many(data)
counter += 1
print("Estimated Resident Population in HDB CSV converted! (",counter,")")