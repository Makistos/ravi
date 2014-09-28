# -*- coding: utf-8 -*-
### required - do no delete

from pygeocoder import Geocoder

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
    
def index():
    db.t_kiinnostuneet.f_area.requires = IS_IN_SET(AREAS, error_message='Valitse alue')
    form = SQLFORM(db.t_kiinnostuneet)

    if form.validate():
        result = Geocoder.geocode(form.vars.f_lahiosoite + ', ' + form.vars.f_postitoimipaikka + ', finland')
        if result.valid_address == True:
            form.vars.f_lat = result[0].coordinates[0]
            form.vars.f_long = result[0].coordinates[1]
        else:
            form.vars.f_lat = ''
            form.vars.f_long = ''
            
        form.vars.f_status = ''
        db.t_kiinnostuneet.insert(**dict(form.vars))
        
        response.flash = 'Kiitos! Tietosi on tallennettu.'
        
    elif form.errors:
       response.flash = 'Ole hyvä ja korjaa virheet.'
    #else:
       #response.flash = 'Yritä uudelleen - kentät eivät voi olla tyhjiä.'
    return dict(form=form)

def error():
    return dict()

def kiinnostuneet_manage():
    db.t_kiinnostuneet.id.readable = False
    db.t_kiinnostuneet.f_nimi.readable = False
    db.t_kiinnostuneet.f_puhelin.readable = False
    db.t_kiinnostuneet.f_sahkoposti.readable = False
    db.t_kiinnostuneet.f_kommentit.readable = False
    db.t_kiinnostuneet.created_on.readable = True
    
    query = db.t_kiinnostuneet
    return dict(form=SQLFORM.grid(query, fields=[db.t_kiinnostuneet.f_lahiosoite, db.t_kiinnostuneet.f_postinumero, db.t_kiinnostuneet.f_postitoimipaikka, db.t_kiinnostuneet.f_area, db.t_kiinnostuneet.created_on],
        orderby=db.t_kiinnostuneet.f_lahiosoite,
        editable=False,
        deletable=False,
        create=False))

@auth.requires_login()
def muokkaa():
    db.t_kiinnostuneet.f_lat.readable=True
    db.t_kiinnostuneet.f_lat.writable=True
    db.t_kiinnostuneet.f_long.readable=True
    db.t_kiinnostuneet.f_long.writable=True
    db.t_kiinnostuneet.f_status.readable=True
    db.t_kiinnostuneet.f_status.writable=True
    db.t_kiinnostuneet.f_area.writable=True
    db.t_kiinnostuneet.f_area.readable=True
    db.t_kiinnostuneet.f_area.requires = IS_IN_SET(AREAS)    
    db.t_kiinnostuneet.created_on.readable=True
    query = db.t_kiinnostuneet
    return dict(form=SQLFORM.grid(query,
        orderby=db.t_kiinnostuneet.f_lahiosoite,
        editable=True,
        deletable=True,
        create=True))

def kartta():
     latitude = 65.00
     longitude = 24.00
     return dict(latitude=latitude, longitude=longitude)
