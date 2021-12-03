from typing_extensions import ParamSpec
from mysql.connector import connect
from mysql.connector.utils import _parse_lsb_release_command

class database:
    def __init__(self):
        try:
            self.db = connect(host='localhost',
                            database='perpustakaan',
                            user='root',
                            password='')
            if self.db.is_connected():
                print('Connected to MySQL database')
        except Exception as e:
            print(e)

    def showBorrowByEmail(self, **params):
        cursor = self.db.cursor()
        query = '''
        select customers.username, borrows.*
        from borrow
        inner join customers on borrows.userid = customers.userid
        where customer.email = "({0})" and borrow.isactive = 1;
        '''.format(params["email"])
        cursor.execute(query)
        result = cursor.fetcall()
        return result

    def insertBorrow(self, **params):
        column = ', '.join(list(params.keys()))
        values = tuple(list(params.values()))
        cursor = self.db.cursor()
        query = '''
        insert into ({0})
        values {1}
        '''.format(column, values)
        cursor.execute(query)
        cursor.execute(query)

    def updateBorrow(self, **params):
        borrowid = params["borrowid"]
        cursor = self.db.cursor()
        query = '''
        update borrows
        set isactive = 0
        where borrowid = {0};
        '''.format(borrowid)
        cursor.execute(query)

    def dataCommit(self):
        self.db.commit()