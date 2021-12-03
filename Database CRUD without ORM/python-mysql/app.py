from models.customers import database

data = {
    "params":[
        {
            "values" :{
                "username" : "userpertama",
                "namadepan" : "rudi",
                "namabelakang" : "roundhouse",
                "email" : "rudi.roundhouse@gmail.com"
            } 
        },
        {
            "values" :{
                "username" : "userkedua",
                "namadepan" : "shiroe",
                "namabelakang" : "ishigami",
                "email" : "shiroe.ishigami@gmail.com"
            } 
        },
        {
            "values" :{
                "username" : "userketiga",
                "namadepan" : "akatsuki",
                "namabelakang" : "horizon",
                "email" : "akatsuki.horizon@gmail.com"
            } 
        }
    ]
}

data_ubah = {
    "params":[
        {
            "userid": 1,
            "values" :{
                "namabelakang" : "pertest",
                "email" : "rudi.pertest@gmail.com"
            } 
        }
    ]
}

data_hapus = {
    "params":[
        {
            "userid": 3
        }
    ]
}

data_lihat = {
    "params":[
        {
            "userid": 1
        }
    ]
}

def tambahData(data):
    for param in data['params']:
        mysqldb.insertUser(**param)
    mysqldb.dataCommit()
    print("data berhasil ditambahkan")

def ubahData(data):    
    for param in data['params']:
        mysqldb.updateUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil diubah")

def hapusData(data):
    for param in data['params']:
        mysqldb.deleteUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil dihapus")

def lihatSemuaData():
    mysqldb.showUsers()
    print("semua data berhasil dilihat")

def lihatData(data):
    for param in data['params']:
        mysqldb.showUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil dilihat")

if __name__ == "__main__":
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')
    
    # tambahData(data)
    # ubahData(data_ubah)
    # hapusData(data_hapus)
    # lihatData(data_lihat)
    lihatSemuaData()

    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()