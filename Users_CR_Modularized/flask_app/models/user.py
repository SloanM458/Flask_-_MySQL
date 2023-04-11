from mysqlconnection import connectToMySQL



class User:
    DB = "users"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# Data is a dictionary 
# Column names MUST match up with worbkench names
#Running a select query will return a dictionary


# Crud Methods:

# Create:
@classmethod
def save(cls,data):
    query = """
            INSERT into users (first_name, last_name, email)
            VALUES ( %(), %(), %() );
    """

    results = connectToMySQL(cls.DB).query_db(query, data)
    return results
# Read:

# Update:

# Delete: