from django.db import models

class UserModel(models.Model):
    id = None
    name = None
    email = None
    ph_no  = None
    city = None
    state = None
    accounts = None

    def __init__(self, _id, full_name, email, ph_no, city, state, accounts) :
        self.id = _id
        self.name = full_name
        self.email = email
        self.ph_no = ph_no 
        self.city = city
        self.state = state
        self.accounts= accounts
