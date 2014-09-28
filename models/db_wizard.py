### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_kiinnostuneet',
    Field('f_nimi', type='string',
          label=T('Nimi'), requires=[IS_NOT_EMPTY(error_message='Nimi puuttuu')]),
    Field('f_lahiosoite', type='string',
          label=T('Lähiosoite'), requires=[IS_NOT_EMPTY(error_message='Katuosoite puuttuu')]),
    Field('f_postinumero', type='string',
          label=T('Postinumero'), requires=[IS_NOT_EMPTY(error_message='Postinumero puuttuu')]),
    Field('f_postitoimipaikka', type='string',
          label=T('Postitoimipaikka'), requires=[IS_NOT_EMPTY(error_message='Postitoimipaikka puuttuu')]),
    Field('f_puhelin', type='string',
          label=T('Puhelin'), requires=[IS_NOT_EMPTY(error_message='Puhelinnumero puuttuu'), IS_ALPHANUMERIC(error_message='Puhelinnumero on muotoa 0501234567')]),
    Field('f_sahkoposti', type='string',
          label=T('Sähkoposti'), requires=[IS_EMAIL(error_message='Anna oikea sähköpostiosoite')]),
    Field('f_kommentit', type='string',
          label=T('Kommentit')),
    Field('f_lat', type='string',
          label=T('X'), readable=False, writable=False),
    Field('f_long', type='string',
          label=T('Y'), readable=False, writable=False),
    Field('f_status', type='string',
          label=T('Status'), readable=False, writable=False),
    Field('f_area', type='string',
          label=T('Alue'), requires=[IS_NOT_EMPTY(error_message='Alue puuttuu')]),
    auth.signature,
    format='%(f_nimi)s',
    migrate=settings.migrate)

db.define_table('t_kiinnostuneet_archive',db.t_kiinnostuneet,Field('current_record','reference t_kiinnostuneet',readable=False,writable=False))
