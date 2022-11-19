from flask import Blueprint, render_template,request, flash,redirect,session
from website.models import User
from website.views import login_required

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if len(email) < 4:
            flash('Enter valid email!', category='error')
        elif len(password) < 8:
            flash('Password too short!', category='error')
        else:
            #check in database
            User().login(email,password)
            return redirect('/dashboard')        
           
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return User().log_out()

@auth.route('/signUp', methods=['GET','POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Enter valid email!', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!!', category='error')
        elif len(password1) < 8:
            flash('Password too short!', category='error')
        else:
            #add user to database            
            User().signUp(email,password1)
            return redirect('/dashboard')        

    return render_template('signUp.html')

@auth.route('/changePassword',methods=['GET','POST'])
@login_required
def changePassword():
    if request.method == 'POST':
        email = session['username']
        currentPassword = request.form.get('currentpassword')
        newPassword1 = request.form.get('newpassword1')
        newPassword2 = request.form.get('newpassword2')


        if newPassword1 != newPassword2:
            flash('Passwords don\'t match!!', category='error')
        elif len(newPassword1) < 8:
            flash('Password too short!', category='error')
      
        if(User().checkPassword(email,currentPassword)):
            if newPassword1 == newPassword2:
                User().updatePassword(email,newPassword1)            

    return render_template('changePassword.html')

@auth.route('/deleteAccount',methods=['GET','POST'])
@login_required
def deleteAccount():
    if request.method == 'POST':
        email = session['username']
        currentPassword = request.form.get('currentpassword')

        if(User().checkPassword(email,currentPassword)):
            User().deleteAccount(email)
            return redirect('/')
    return render_template('deleteAccount.html')

