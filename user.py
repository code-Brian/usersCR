from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data ):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # other methods go here

    # define a class method which will interact with our database connection
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL('users_schema').query_db(query)
        # create an empty list to store our results in
        users = []
        # iterate over the db results and create instances of users with cls
        for user in results:
            users.append(cls(user))
        return users
    
    # now we need to define a class method to save our results in the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s,%(lname)s, %(email)s, NOW(), NOW() );"

        return connectToMySQL('users_schema').query_db(query, data)
