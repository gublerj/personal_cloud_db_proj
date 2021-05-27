
# pip install firebase-admin
import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
# connect to firebase and initialize
cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# create collection called users
col_ref = db.collection(u'users')


# setup printng in bold
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



def add_contact():
    # get inputs
    first = input("First Name: ")
    last = input("Last Name: ")
    phone = input("Phone Number: ")
    bday = input("Birthday: ")
    
    # create document titeld with the first name
    doc_ref = col_ref.document(first)

    # set the fields in the document to the user input
    doc_ref.set({
        'first': first,
        'last': last,
        'phone': phone,
        'birthday': bday
    })

"""
def test():
    data = {
    u'stringExample': u'Hello, World!',
    u'booleanExample': True,
    u'numberExample': 3.14159265,
    u'dateExample': datetime.datetime.now(),
    u'arrayExample': [5, True, u'hello'],
    u'nullExample': None,
    u'objectExample': {
        u'a': 5,
        u'b': True
    }
    }

    db.collection(u'data').document(u'one').set(data)
"""

def query():
    who = input("Who do you want to see? ")
    # get the document with the name the user just chose
    results = col_ref.where('first', '==', who).get()
    # access results that are in a list and turn it into a dict
    results = results[0].to_dict()
    print("")

    # for each item in the dict
    #   print the key in bold
    #   print the value
    for i in results:
        print(color.BOLD + i + color.END)
        print(results[i])
        print(" ")
        print(" ")
        
def display_all():
    # get all the documents in the users collection
    docs = db.collection(u'users').stream()

    # for every document
    #   get the document
    #   turn it into a dict
    #   
    for doc in docs:
        info = col_ref.document(doc.id).get()
        person = info.to_dict()
        print(color.BOLD + person['first'] + color.END)
        print(person['last'])
        print(" ")
        print(" ")

    


def update_contact():
    
    first = input("Who do you want to update? (first name): ")

    # initialize sub menue
    update_choice = None
    print("")

    # sub menue setup
    print("What do you want to update? (you can't change a first name)")
    print("2) Last Name")
    print("3) Phone")
    print("4) Birthday")
    update_choice = input("> ")
    print(" ")
    print(" ")

    # get the document for the contact specified by the user
    # turn to dictionary
    info = col_ref.where(u'first', u'==', first).limit(1).stream()
    info = { el.id: el.to_dict() for el in info }

    """
    if update_choice == "1":
        # get new name and update the database
        new = input("enter new first name: ")

        col_ref.document(first).set({
            'birthday': info[first]['birthday'],
            'first': new,
            'last': info[first]['last'],
            'phone': info[first]['phone']
        })
    """
    
    if update_choice == "2":
        # get new address and update the database
        new = input("enter new last name: ")

        col_ref.document(first).set({
            'birthday': info[first]['birthday'],
            'first': info[first]['first'],
            'last': new,
            'phone': info[first]['phone']
        })

    if update_choice == "3":
        # get new phone and update the database
        new = input("enter new phone: ")

        col_ref.document(first).set({
            'birthday': info[first]['birthday'],
            'first': info[first]['first'],
            'last': info[first]['last'],
            'phone': new
        })


    if update_choice == "4":
        # get new bday and update the database
        new = input("enter new birthday: ")

        col_ref.document(first).set({
            'birthday': new,
            'first': info[first]['first'],
            'last': info[first]['last'],
            'phone': info[first]['phone']
        })



def delete_contact():
    who = input("Who do you want to delete? ")
    # delete users "name specified"
    db.collection(u'users').document(who).delete()


choice = None

while choice != "6":
    print("1) Display Contacts")
    print("2) Add Contact")
    print("3) Update Contact")
    print("4) Delete contact") 
    print("5) Open Contact")
    print("6) Quit")
    choice = input("> ")
    print(" ")
    print(" ")


    if choice == "1":
        #display all contacts
        display_all()

    elif choice =="2":
        # add new contact
        print("Adding new contact")
        add_contact()

    elif choice =="3":
        print("Update Contact")
        update_contact()

    elif choice =="4":
        # delete a contact
        delete_contact()

    elif choice =="5":
        query()
