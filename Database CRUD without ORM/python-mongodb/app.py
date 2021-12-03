from models.books import database as db
import csv

def add_book():
    data = open('bestsellers-with-categories.csv', encoding='utf-8')
    books = csv.reader(data, delimiter=',')
    next(books) # because we dont need the first row containing column headers

    for book in books:
        try:
            data = {
                'nama' : book[0],
                'pengarang' : book[1],
                'tahun terbit' : book[5],
                'genre' : book[6]
            }
            db.insertBook(data)
        except Exception as e:
            print('Kesalahan pada saat memasukkan data: {}'.format(e))
            break

def search_book(params):
    for book in db.searchBookByName(params):
        print(book)

def show_book():
    for book in db.showBooks():
        print(book)
        
def show_book_by_id(params):
    for book in db.showBookById(params):
        print(book)

def delete_book_by_id(params):    
    for book in db.deleteBookById(params):
        print("data berhasil dihapus")

data_ubah = {
    "_id":"61a9b2e9529f0182ac6cddf4",
    "nama":"Detective Conan",
    "pengarang":"Aoyama Gosho",
    "tahun terbit":"1999",
    "genre":"Fiction"
}

def update_book_by_id(data):    
    db.updateBookById(data)

if __name__ == '__main__':
    db = db()
    # add_book()
    # search_book('harry')
    # show_book()
    # update_book_by_id(data_ubah)
    show_book_by_id("61a9b2e9529f0182ac6cddf4")
    # delete_book_by_id('61a9b2e9529f0182ac6cddf4')
    db.nosql_db.close()