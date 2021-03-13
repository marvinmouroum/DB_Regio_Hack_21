import gmaps
from ipywidgets.embed import embed_minimal_html
import numpy as np
gmaps.configure(api_key='AIzaSyD1pH2XRLolftuoiCWqeW3pbvqZgSq6VTg')


def gen_heat_map(x,name):
    locations = np.stack((x[:,0],x[:,1]),axis=-1)
    print(len(locations))
    weights = x[:,2]
    print(len(weights))
    fig = gmaps.figure()
    fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
    fig
    embed_minimal_html('export_{}.html'.format(name), views=[fig])