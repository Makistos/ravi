response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Ilmoittaudu'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Kiinnostuneet'),URL('default','kiinnostuneet_manage')==URL(),URL('default','kiinnostuneet_manage'),[]),
(T('Kartta'), URL('default','kartta')==URL(),URL('default','kartta'),[]),
(T('Muokkaa'),URL('default','muokkaa')==URL(),URL('default','muokkaa'),[]),

]
