from database_connection import *
from pop_up import msg

class CRUD:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.is_connected = False

    def create_table(self):
        try:
            self.cursor.execute(f"CREATE TABLE {TABLE_NAME}(ID INT IDENTITY(1, 1), NAME VARCHAR(50) NOT NULL, ADDRESS VARCHAR(255) NOT NULL)")
            #    , EMAIL VARCHAR(50) UNIQUE, PHONE_NUMBER VARCHAR(11), COUNTRY CHAR(3))")
            print("Table created successfully!!!")
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass
       



    def modify_table(self):
        try:
            self.cursor.execute(f"ALTER TABLE {TABLE_NAME} ADD EMAIL VARCHAR(50) UNIQUE, PHONE_NUMBER VARCHAR(11), COUNTRY CHAR(3)")
            print("Table successfully modified!!!")
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass
       


    # def transmitter(self):
    #     return False



    def insert_person(self,*details):
        try:
            # if type(self.connection) != 'NoneType' or type(self.cursor()) != "NoneType":
            self.cursor.execute(f"INSERT INTO {DB_NAME}.dbo.{TABLE_NAME} values(?,?)", details)
            # msg("Success!")
            self.connection.commit()
            return True
            
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass



    def update_person(self, *others):
        try:
            self.cursor.execute(f"UPDATE {DB_NAME}.dbo.{TABLE_NAME} SET NAME=?, ADDRESS=? WHERE ID=?", others)
            msg("Record successfully updated!")
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass
       



    def get_person_by_id(self, id):
        try:
            self.cursor.execute(f"SELECT * FROM {DB_NAME}.dbo.{TABLE_NAME} WHERE ID=?", id)
            user = self.cursor.fetchone()
            # for row in user:
            # print(user)
            print("Record Selected!")
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass
       



    def get_all_people(self):
        try:
            self.cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            result = self.cursor.fetchall()

            self.connection.commit()
            return result
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass
       



    def delete_by_id(self,id):
        try:
            self.cursor.execute(f"DELETE FROM {DB_NAME}.dbo.{TABLE_NAME} WHERE ID=?", id)
            print("Deleted successfully")
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass


    def delete_table(self):
        try:
            self.cursor.execute(f"DROP TABLE {DB_NAME}.dbo.{TABLE_NAME}")
            print("Table deleted successfully!!!")
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            if self.connection:
                self.connection.rollback()
                print(e)
            pass
       

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
            

    def toggle_connection(self):
        if self.is_connected:
            self.close_connection()
            self.is_connected = False
        else:
            self.connection = connection
            self.cursor = self.connection.cursor()
            self.is_connected = True
            print("Connection started")



    # def restart_connection(self):
    #     self.close_connection()
    #     self.connection = connection
    #     self.cursor = self.connection.cursor()
    #     print("Connection restarted")



crud_operations = CRUD()


# crud_operations.create_table()
# crud_operations.delete_by_id(3)
# crud_operations.delete_table()
# crud_operations.get_person_by_id(5)
# crud_operations.get_all_people()
# crud_operations.toggle_connection()
# crud_operations.insert_person("tyugfxfryl", "fdja pokemi")
# crud_operations.modify_table()
# crud_operations.update_person( "Ebuk's", "Abuja Kano Road", 4)