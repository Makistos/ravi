def index():
    width = request.vars.width or 700
    height = request.vars.height or 700
    #rows = plugin_gmap.set    
    db.t_kiinnostuneet.f_lat.readable = True
    db.t_kiinnostuneet.f_long.readable = True
    rows = db(db.t_kiinnostuneet.id>0).select()
    for row in rows:
        if row.f_lat and row.f_long:
            row.plugin_gmap_popup = plugin_gmap.represent(row)
    return dict(width=width,height=height,rows=rows,GOOGLEMAP_KEY=plugin_gmap.key)
