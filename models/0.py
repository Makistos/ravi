from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Kiinnostuneet'
settings.subtitle = 'powered by web2py'
settings.author = 'Marko Poutiainen'
settings.author_email = 'olka@sofistes.net'
settings.keywords = ''
settings.description = 'T\xc3\xa4m\xc3\xa4n sovelluksen avulla OLKA:an liittymisest\xc3\xa4 kiinostuneet voivat ilmoittautua.\r\n\r\nOLKA ei voi luvata aikataulua, mutta otamme huomioon ilmoittautuneet kun suunnittelemme laajentumista.'
settings.layout_theme = 'Whitelight'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '964d1eb9-1390-426a-9091-f55be33c0167'
settings.email_server = 'localhost'
settings.email_sender = 'info@olka.fi'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['gmap', 'sortable']
