# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    DB = "users_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        # ^^^The get_all() will get all the data from db and put it into instances of our class^^^
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        new_user = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            new_user.append( cls(user) )
        return new_user

    @classmethod
    def save(cls, data ):
        query = """
        INSERT INTO friends ( first_name , last_name , email, created_at) 
        VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(CURRENT_TIMESTAMP)s );
        """
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(cls.DB).query_db( query, data ) 
        return results


