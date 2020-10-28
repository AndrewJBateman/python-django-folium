from django.shortcuts import render, redirect
import os
import folium

# Create your views here.
def home(request):
  shp_dir = os.path.join(os.getcwd(), 'media', 'shp')

  m = folium.Map(location=[-16.22,-71.59], zoom_start=9)

  ## New location
  # m = folium.Map(location=[48.858370, 2.294481], zoom_start=9)

  ## style
  style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
  style_river = {'color': 'blue'}

  ## add to view
  folium.GeoJson(os.path.join(shp_dir,'basin.geojson'),name='basin',style_function=lambda x:style_basin).add_to(m)
  folium.GeoJson(os.path.join(shp_dir,'rivers.geojson'),name='rivers',style_function=lambda x:style_river).add_to(m)
  folium.LayerControl().add_to(m)

  ## export map
  m=m._repr_html_()
  context = {'my_map': m}

  ## render
  return render(request,'geoApp/home.html', context)