from mysql.connector import connect

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
    
    def showUsers(self):
        cursor = self.db.cursor()
        query ='''select * from customers'''
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def showUserById(self, **params):
        cursor = self.db.cursor()
        query = '''
            select * 
            from customers 
            where userid = {0};
        '''.format(params["userid"])
        
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def showUserByEmail(self, **params):
            cursor = self.db.cursor()
            query = '''
                select * 
                from customers 
                where email = "{0}" ;
            '''.format(params["email"])
            
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    
    def closeConnection(self):
        if self.db is not None and self.db.is_connected():
            self.db.close()