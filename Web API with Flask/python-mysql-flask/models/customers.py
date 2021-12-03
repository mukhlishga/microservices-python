from mysql.connector import connect

class database:
    def __init__(self):
        try:
            self.db = connect(host='localhost',
                              database='perpustakaan',
                              user='root',
                              password='')
        except Exception as e:
            print(e)
    
    def showUsers(self):
        try:  
            cursor = self.db.cursor()
            query ='''select * from customers'''
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    
    def showUserById(self, **params):
        try:
            cursor = self.db.cursor()
            query = '''
                select * 
                from customers 
                where userid = {0};
            '''.format(params["userid"])
            
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
    
    def insertUser(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            crud_query = '''insert into customers ({0}) values {1};'''.format(column, values)
            # print(crud_query)
            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def updateUserById(self, **params):
        try:
            userid = params['userid']
            values = self.restructureParams(**params['values'])
            crud_query = '''update customers set {0} where userid = {1};'''.format(values, userid)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def deleteUserById(self, **params):
        try:
            userid = params['userid']
            crud_query = '''delete from customers where userid = {0};'''.format(userid)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def dataCommit(self):
        self.db.commit()
        
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result