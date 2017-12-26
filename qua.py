# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from shapely.geometry import *

class Building:
    """
    qua-kit building class. 
    each Building instance represents a qua-kit building object, which is wrapped as a feature in the GeoJSON file.
    applicable to GeoJSON files imported from both OpenStreetMap and 3D creation softwares.
    """
    
    def __init__(self, feature):
        """
        :type feature: dict
        """
        # default params
        self.geometry = None
        self.properties = {}
        self.tags = {}
        
        if 'properties' in feature:
            if isinstance(feature['properties'], dict):
                self.properties = feature['properties']
        
        if 'geometry' in feature:
            if 'coordinates' in feature['geometry']:
                self.geometry = shape(feature['geometry'])

    
    ###############
    ### Plotter ###
    ###############
    
    def plot(self, c='k'):
        """
        plot the polygon with matplotlib.
        :type c: str
        """
        plt.plot(self.convex_vertices()[0], self.convex_vertices()[1], c)
        plt.axis('equal')
    
    
    ###########
    ### Tag ###
    ########### 
    
    def tag(self, category_tagger={}):
        """
        updates and returns the categorical tags of the building.
        :type category_tagger: dict
        :rtype: dict
        """
        self.tags.update(category_tagger)
        return self.tags

    
    
class Scenario:
    """
    qua-kit scenario class. 
    a Scenario instance represents a qua-kit scenario contained in a GeoJSON file.
    applicable to GeoJSON files imported from both OpenStreetMap and 3D creation softwares.
    """

    def __init__(self, file):
        """
        initialize a Scenario instance with a GeoJSON file already parsed by json library.
        :type file: dict
        """
        # default params
        self.lonlat = None
        self.name = None
        self.map_zoom_level = None
        
        self.tags = []
        self.buildings = []
                
        # osm-based geometry is based on explicit lat, lon coordinates,
        # while geometry rendered from 3D creation software(i.e. blender) is based on relative [x, y, z] coordinates
        # and baseline longitude, latutide coordiantes as scenario properties.
        
        if 'name' in file:
            self.name = file['name']
        
        if 'lon' in file and 'lat' in file:
            self.lonlat = [float(file['lon']), float(file['lat'])]

        if 'properties' in file:
            if 'mapZoomLevel' in file['properties']:
                self.map_zoom_level = int(file['properties']['mapZoomLevel'])
                
        if 'geometry' in file:
            if 'features' in file['geometry']:
                self.buildings = [Building(feature) for feature in file['geometry']['features']]

    
    ############
    ### Area ###
    ############ 
    
    def buildings_in_area(self, polygon):
        """
        returns a list of buildings within the area given.
        :type polygon: shapely.geometry.polygon
        """
        return [b for b in self.buildings if polygon.contains(b.geometry())]
    
    
    ###############
    ### Plotter ###
    ###############
    
    def plot(self, area=False):
        """
        plot the buildings in the scenario with matplotlib.
        """
        for b in self.buildings:
            b.plot()
            
    
    ##############
    ### Tagger ###
    ##############
    
    def tag(self, prop, tagger_dict):
        """
        tag all buildings by given property with a pre-defined tagger dictionary.
        :type tagger: dict
        :type prop: str
        """
        for tag_label, tagger in tagger_dict.items():
            self._category_tagger(prop, tag_label, tagger)
            if tag_label not in self.tags:
                self.tags.append(tag_label)
    
    def _category_tagger(self, prop, tag_label, tagger):
        """
        categorical tagger.
        """
        for b in self.buildings:
            if prop in b.properties:
                if b.properties[prop] in tagger.keys():
                    tag = tagger[b.properties[prop]]
                    b.tag({tag_label:tag}) 