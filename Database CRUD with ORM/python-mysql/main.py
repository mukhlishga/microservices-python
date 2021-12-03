from models import Customers, session

def showUsers(model):
    result = session.query(model).all()
    for row in result:
        print(row.userid, row.username, row.namadepan, row.namabelakang, row.email)

show_data = {
    'userid' : 1
}

def showUserById(model, **params):
    result = session.query(model).filter(model.userid==params['userid'])
    for row in result:
        print(row.userid, row.username, row.namadepan, row.namabelakang, row.email)
        
new_user = {
    'userid' : 7,
    'username' : 'harunyahya',
    'namadepan' : 'Harun',
    'namabelakang' : 'Yahya',
    'email' : 'harunyahya@gmail.com'
}

def insertUser(model, **param):
    session.add(model(**param))
    session.commit()

new_data = {
    'userid' : 4, # or can be emptied becuse userid is auto increment
    'username' : 'harrypotter',
    'namadepan' : 'Harry',
    'namabelakang' : 'Potter',
    'email' : 'harrypotter@gmail.com'
}

def updateUserById(model,**params):
    result = session.query(model).filter(model.userid==params['userid']).one()
    result.username = params['username']
    result.namadepan = params['namadepan']
    result.namabelakang = params['namabelakang']
    result.email = params['email']
    session.commit()
    print(result.userid, result.username, result.namadepan, result.namabelakang, result.email)

delete_data = {
    'userid' : 4
}

def deleteUserById(model, **params):
    result = session.query(model).filter(model.userid==params['userid']).one()
    session.delete(result)
    session.commit()

if __name__ == '__main__':

    if session:
        print("Connection Success")
    
    showUsers(Customers)
    # showUserById(Customers, **show_data)
    # insertUser(Customers, **new_user)
    # updateUserById(Customers, **new_data)
    # deleteUserById(Customers, **delete_data)
