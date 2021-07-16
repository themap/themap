
from .functions import delete_map
from .functions import update_map
from .functions import get_all_features
from .functions import generate_screenshot
from ..common import config
from ..layer import create_layer
from ..layer import create_link_layer
from ..layer import create_image_layer
from ..layer.layer_class import Layer
from ..layer.link_layer_class import LinkLayer
from ..layer.image_layer_class import ImageLayer

class Map:
    def __init__(self, params):
        self.assign_props(params)
        setattr(self,'Layers',params['Layers'])
        setattr(self,'LinkLayers',params['LinkLayers'])
        setattr(self,'ImageLayers',params['ImageLayers'])
        if self.Layers == None:
            self.Layers = []
        self.Layers = list(map(lambda x : Layer(x),self.Layers))
        if self.LinkLayers == None:
            self.LinkLayers = []
        self.LinkLayers = list(map(lambda x : LinkLayer(x),self.LinkLayers))
        if self.ImageLayers == None:
            self.ImageLayers = []
        self.ImageLayers = list(map(lambda x : ImageLayer(x),self.ImageLayers))

    def __repr__(self): 
        return repr(self.to_dict())
    
    def __str__(self): 
        return str(self.to_dict())


    def assign_props(self,params):
        for key in params:
            if key not in ['Layers','LinkLayers','ImageLayers']:
                setattr(self,key,params[key])
        return self

    def to_dict(self):
        return self.__dict__

    def delete(self):
        return delete_map(self.ID,config.token)

    def update(self, options = {}):
        for key in options:
            setattr(self,key,options[key])
        map_dict = update_map(self.to_dict(),config.token)
        return self.assign_props(map_dict)
    
    def add_layer(self,options):
        options['TourMapID'] = self.ID
        layer = create_layer(options)
        self.Layers.append(layer)
        return layer
    
    def add_link_layer(self,options):
        options['TourMapID'] = self.ID
        layer = create_link_layer(options)
        self.LinkLayers.append(layer)
        return layer
    
    def add_image_layer(self,options):
        options['TourMapID'] = self.ID
        layer = create_image_layer(options)
        self.ImageLayers.append(layer)
        return layer
    
    def all_features(self):
        return get_all_features(self.ID,config.token)
    
    def generate_screenshot(self):
        map_dict = generate_screenshot(self,config.token)
        return self.assign_props(map_dict)
        