from flask import Flask, jsonify, request,flash,session,redirect
from passlib.hash import pbkdf2_sha256
import uuid
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:adminPassword@cluster0.ivh8z2v.mongodb.net/?retryWrites=true&w=majority")
UsersDB = client.HereGotWhat



class User:

    def start_session(self,user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        session['username'] = user['email']
    
    def log_out(self):
        session.clear()
        return redirect('/')

    def signUp(self, email, password):
        user = {
            "_id": uuid.uuid4().hex,
            "email": email,
            "password": password
        }

        user["password"]=pbkdf2_sha256.encrypt(user["password"])

        #checking for existing email in db

        if(UsersDB.Users.find_one({"email": user['email']})):
            return flash('Email already exists!', category='error')
        else:
            UsersDB.Users.insert_one(user)
            self.start_session(user)
            return flash('Account created!', category='success')
            
    def login(self, email,password):
        user = UsersDB.Users.find_one({
            "email": email 
        })

        if user and pbkdf2_sha256.verify(password,user['password']):
            return self.start_session(user)
        return flash('Wrong email or password!', category='error')

    def checkPassword(self, email,password):
        user = UsersDB.Users.find_one({
            "email": email 
        })
        if user and pbkdf2_sha256.verify(password,user['password']):
            return True
        else:
           return flash('Wrong password!', category='error')
    
    def updatePassword(self,email,newPassword):
        filter = {'email': email}
        encryptedNewPassword = pbkdf2_sha256.encrypt(newPassword)
        newValues = {"$set": {'password':encryptedNewPassword}}
        UsersDB.Users.update_one(filter,newValues)
        return flash('Password Changed!', category='success')

    def deleteAccount(self,email):
        filter = {'email':email}
        UsersDB.Users.delete_one(filter)
        self.log_out()
        return flash('Account Deleted', category='success')


        