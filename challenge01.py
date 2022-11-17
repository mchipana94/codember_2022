input_file = './users.txt'

class User():
    def __init__(self, usr=None, eme=None, psw=None, age=None, loc=None, fll=None, **kwargs):
        # valid_fields = ['usr', 'eme', 'psw', 'age', 'loc', 'fll']
        self.usr = usr
        self.eme = eme
        self.psw = psw
        self.age = age
        self.loc = loc
        self.fll = fll
        self.is_valid = usr is not None and eme is not None and psw is not None and age is not None and loc is not None and fll is not None
    
    def __repr__(self):
        return "User<%s>"%self.usr

    def __str__(self):
        #return "< %s -> %s >"%(self.usr,'Valid' if self.is_valid else 'Not Valid')
        return '{usr:' + str(self.usr) + ', eme:' + str(self.eme) + ', psw:' + str(self.psw) + ', age:' + str(self.age) + ', loc:' + str(self.loc) + ', fll:' + str(self.fll)+ '}'

def text2obj(user_text):
    """
    Converts text user's data into a user dict
    """
    data_pairs = user_text.split()
    arguments = dict()
    for data_pair in data_pairs:
        pair = data_pair.split(':')
        arguments[pair[0]] = pair[1]
    return User(**arguments)

def read_user(filename):
    archive = open(filename,'r')
    user_lines = archive.read().split('\n\n') # split data for every user
    archive.close()

    valid_users = list()
    invalid_users = list()

    for user_line in user_lines:
        user = text2obj(user_line)
        if user.is_valid:
            valid_users.append(user)
        else:
            invalid_users.append(user)

    print('Total Valid Users: ', len(valid_users))
    print('Last Valid User:')
    print(valid_users[-1])

    print('Total Invalid Users: ', len(invalid_users))
    print('Last Invalid User:')
    print(invalid_users[-1])
    

read_user(input_file)