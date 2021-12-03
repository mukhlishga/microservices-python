from models import connection, customers

def showUsers(model):
    for doc in model.objects:
        print(doc.username, doc.fullname, doc.email)

show_data = {
    '_id' : 1
}

def showUserById(model, **params):
    for doc in model.objects(_id=params['_id']):
        print(doc._id, doc.username, doc.fullname, doc.email)
 
new_user = {
    '_id' : 4,
    'username' : 'Harun',
    'fullname' : 'Harun Yahya',
    'email' : 'harun@gmail.com'
}

def insertUser(model, **param):
    model(**param).save()
    for doc in model.objects:
        print(doc.username, doc.username, doc.fullname, doc.email)

new_data = {
    '_id' : 4,
    'username' : 'Harunnn',
    'fullname' : 'Harunnn Yahya',
    'email' : 'harunnn@gmail.com'
}

def updateUserById(model, **params):
    doc_1 = model.objects(_id=params['_id']).first()
    doc_1.username = params['username']
    doc_1.fullname = params['fullname']
    doc_1.email = params['email']
    doc_1.save()

delete_data = {
    '_id' : 4
}

def deleteUserById(model, **params):
    pass
    doc_1 = model.objects(_id=params['_id'])
    doc_1.delete()

if __name__ == '__main__':
    
    if connection:
        print('MongoDB Connected')

    showUsers(customers)
    # showUserById(customers, **show_data)
    # insertUser(customers, **new_user)
    # updateUserById(customers, **new_data)
    # deleteUserById(customers, **delete_data)