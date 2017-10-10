class Server:

    def __init__(self):
        self.name = 'default'
        self.address = '127.0.0.1'
        self.password = ''
        self.identity_mode = False
        self.identity_key = './'

    def get_name(self):
        return self.name


