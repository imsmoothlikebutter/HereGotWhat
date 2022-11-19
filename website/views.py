from flask import Blueprint, render_template,redirect,session, request, flash
from functools import wraps
import pymongo

views = Blueprint('views', __name__)

client = pymongo.MongoClient("mongodb+srv://admin:adminPassword@cluster0.ivh8z2v.mongodb.net/?retryWrites=true&w=majority")
db = client.HereGotWhat

def capFirstLetterEveryWord(word):
    wordlist = word.split()
    print(wordlist)
    for x in range(len(wordlist)):
        wordlist[x] = wordlist[x].capitalize()
    print(wordlist)
    word = " ".join(wordlist)
    return word

#redirect to homepage when not logged; when trying to access other parts of the site by changing url
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@views.route('/pharmacies', methods=['GET','POST'])
@login_required
def viewPharmacy():
    PharmaciesQuery = db.LicensedPharmacies.find({},{'_id':0})
    listOfTowns = db.LicensedPharmacies.distinct('Town')
    index = db.LicensedPharmacies.count_documents({})
    print(index)

    if request.method == 'POST':
        townFilter = request.form.get('location')
        townFilter = capFirstLetterEveryWord(townFilter)
        if townFilter != "":
            PharmaciesQuery = db.LicensedPharmacies.find({'Town':townFilter})
        else:
            PharmaciesQuery = db.LicensedPharmacies.find({},{'_id':0})

    print(listOfTowns)
    return render_template("viewpharmacy.html",PharmaciesQuery = PharmaciesQuery)

@views.route('/supermarkets', methods=['GET', 'POST'])
@login_required
def viewSupermarket():
    SupermarketQueries = db.Supermarkets.find({},{'_id':0})
    listOfTowns = db.Supermarkets.distinct('town')
    index = db.Supermarkets.count_documents({})
    print(index)

    if request.method == 'POST':
        townFilter = request.form.get('location')
        townFilter = townFilter.upper()
        if townFilter != "":
            SupermarketQueries = db.Supermarkets.find({'town':townFilter})
        else:
            SupermarketQueries = db.Supermarkets.find({},{'_id':0})

    print(listOfTowns)
    return render_template("viewsupermarkets.html", SupermarketQueries=SupermarketQueries)

@views.route('/rentalflats', methods=['GET', 'POST'])
@login_required
def viewRentalFlats():
    RentalFlats = db.RentalFlats.find({},{'_id':0})
    listOfTowns = db.RentalFlats.distinct('town')
    index = db.RentalFlats.count_documents({})

    if request.method == 'POST':
        townFilter = request.form.get('location')
        townFilter = townFilter.upper()
        if townFilter != "":
            RentalFlats = db.RentalFlats.find({'town':townFilter})
        else:
            RentalFlats = db.RentalFlats.find({},{'_id':0})

    return render_template("viewRentalFlats.html", RentalFlats=RentalFlats)

@views.route('/MOEprogrammes', methods=['GET', 'POST'])
@login_required
def viewMOEprogrammes():
    MOEProgrammes = db.MOEProgrammes.find({},{'_id':0})
    listOfSchools = db.MOEProgrammes.distinct('school_name')
    index = db.MOEProgrammes.count_documents({})

    if request.method == 'POST':
        schoolFilter = request.form.get('school_name')
        schoolFilter = schoolFilter.upper()
        if schoolFilter != "":
            MOEProgrammes = db.MOEProgrammes.find({'school_name':{'$regex': schoolFilter}})
        else:
            MOEProgrammes = db.MOEProgrammes.find({},{'_id':0})

    return render_template("viewMOEProgrammes.html", MOEProgrammes=MOEProgrammes)

@views.route('/CCAs', methods=['GET', 'POST'])
@login_required
def viewCCAs():
    SchoolCCAs = db.SchoolCCAs.find({},{'_id':0})
    listofCCAs = db.SchoolCCAs.distinct('cca_generic_name')
    index = db.SchoolCCAs.count_documents({})

    if request.method == 'POST':
        ccaFilter = request.form.get('CCA_name')
        ccaFilter = ccaFilter.upper()
        print(ccaFilter)
        if ccaFilter != "":
            SchoolCCAs = db.SchoolCCAs.find({'cca_generic_name':{'$regex':ccaFilter}})
        else:
            SchoolCCAs = db.SchoolCCAs.find({},{'_id':0})

    return render_template("viewCCAs.html", SchoolCCAs=SchoolCCAs)

@views.route('/schoolInfo', methods=['GET', 'POST'])
@login_required
def viewSchoolInfo():
    SchoolGeneralInformation = db.SchoolGeneralInformation.find({},{'_id':0})
    schoolListName = db.SchoolGeneralInformation.distinct('school_name')
    index = db.SchoolGeneralInformation.count_documents({})

    if request.method == 'POST':
        schoolFilter = request.form.get('school_name')
        schoolFilter = schoolFilter.upper()
        if schoolFilter != "":
            SchoolGeneralInformation = db.SchoolGeneralInformation.find({'school_name':{'$regex': schoolFilter}})
        else:
            SchoolGeneralInformation = db.SchoolGeneralInformation.find({},{'_id':0})

    return render_template("viewSchoolInfo.html", SchoolGeneralInformation=SchoolGeneralInformation)

@views.route('/SGpopulation', methods=['GET', 'POST'])
@login_required
def viewSGpopulation():
    SGHDBPopulationEstimate = db.SGHDBPopulationEstimate.find({},{'_id':0})
    townListName = db.SGHDBPopulationEstimate.distinct('town_name')
    index = db.SGHDBPopulationEstimate.count_documents({})

    if request.method == 'POST':
        townFilter = request.form.get('town_name')
        townFilter = capFirstLetterEveryWord(townFilter)
        if townFilter != "":
            SGHDBPopulationEstimate = db.SGHDBPopulationEstimate.find({'town_or_estate':townFilter})
        else:
            SGHDBPopulationEstimate = db.SGHDBPopulationEstimate.find({},{'_id':0})

    return render_template("viewPopulation.html", SGHDBPopulationEstimate=SGHDBPopulationEstimate)

@views.route('/ResaleFlats', methods=['GET', 'POST'])
@login_required
def viewResaleFlats():
    ResaleFlats2017onwards = db.ResaleFlats2017onwards.find({},{'_id':0}).limit(1000)
    townListName = db.ResaleFlats2017onwards.distinct('town')
    index = db.ResaleFlats2017onwards.count_documents({})

    if request.method == 'POST':
        townFilter = request.form.get('town_name')
        townFilter = townFilter.upper()
        if townFilter != "":
            ResaleFlats2017onwards = db.ResaleFlats2017onwards.find({'town':townFilter})
        else:
            ResaleFlats2017onwards = db.ResaleFlats2017onwards.find({},{'_id':0}).limit(1000)

    return render_template("viewResaleFlats.html", ResaleFlats2017onwards=ResaleFlats2017onwards)