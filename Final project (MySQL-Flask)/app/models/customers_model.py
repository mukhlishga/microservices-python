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
    
    def insertUser(self, **params):
        column = ', '.join(list(params['values'].keys()))
        values = tuple(list(params['values'].values()))
        crud_query = '''insert into customers ({0}) values {1};'''.format(column, values)
        cursor = self.db.cursor()
        cursor.execute(crud_query)

    def updateUserById(self, **params):
        userid = params['userid']
        values = self.restructureParams(**params['values'])
        crud_query = '''update customers set {0} where userid = {1};'''.format(values, userid)

        cursor = self.db.cursor()
        cursor.execute(crud_query)

    def deleteUserById(self, **params):
        userid = params['userid']
        crud_query = '''delete from customers where userid = {0};'''.format(userid)
        cursor = self.db.cursorcursor.execute(crud_query)

    def dataCommit(self):
        self.db.commit()

    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result

    # def closeConnection(self):
    #     if self.db is not None and self.db.is_connected():
    #         self.db.close()