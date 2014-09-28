from gluon.storage import Storage
plugin_gmap=Storage()

#plugin_gmap.key='AIzaSyCggaGxqeYzbBpwrBYm6ED3utlV-PMPkzw' # key for localhost  
plugin_gmap.set=db(db.t_kiinnostuneet.id>0).select() ### change this to a query that lists records with latitude and longitute
points=db(db.t_kiinnostuneet.id>0).select()
plugin_gmap.represent=lambda row: '%(row.f_lahiosoite)s, %(row.f_postitoimipaikka)s' % row
# include plugin in views with {{=LOAD('plugin_gmap')}}
