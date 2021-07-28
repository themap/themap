
from .functions import delete_layer
from .functions import update_layer
from .functions import apply_bucket_colors
from .functions import apply_category_colors
from .functions import apply_gradient_colors
from .functions import apply_gradient_sizes
from .functions import apply_category_opacity
from .functions import apply_category_outline_colors
from .functions import download_layer
from .functions import import_file
from .functions import get_layer_fields
from ..common import config
from ..layer import create_layer

class Layer:
    def __init__(self, params):
        self.assign_props(params)

    def __repr__(self): 
        return repr(self.to_dict())
    
    def __str__(self): 
        return str(self.to_dict())


    def assign_props(self,params):
        for key in params:
            setattr(self,key,params[key])
        return self

    def to_dict(self):
        return self.__dict__

    def delete(self):
        return delete_layer(self.ID,self.GLSource,config.token)

    def download(self, as_file = None):
        return download_layer(self.ID,config.token,as_file)

    def fields(self):
        return get_layer_fields(self.ID,config.token)

    def import_file(self, filepath, name_prop):
        layer_dict =  import_file(filepath,name_prop,self.TourMapID,config.token,self.ID)
        return self.assign_props(layer_dict)

    def update(self, options = {}):
        for key in options:
            setattr(self,key,options[key])
        layer_dict = update_layer(self.to_dict(),config.token)
        return self.assign_props(layer_dict)
    
    def color_by(self, field, type, colors = {}):
        if field == 'bucket':
            layer_dict = apply_bucket_colors(self.to_dict(),field,colors,config.token)
            return self.assign_props(layer_dict)
        if field == 'category':
            layer_dict = apply_category_colors(self.to_dict(),field,config.token,colors)
            return self.assign_props(layer_dict)
        if field == 'gradient':
            layer_dict = apply_gradient_colors(self.to_dict(),field,colors,config.token)
            return self.assign_props(layer_dict)
    
    def size_by(self, field, type, sizes = {}):
        if field == 'gradient':
            layer_dict = apply_gradient_sizes(self.to_dict(),field,sizes,config.token)
            return self.assign_props(layer_dict)
    
    def opacity_by(self, field, type, opacities = {}):
        if field == 'category':
            layer_dict = apply_category_opacity(self.to_dict(),field,config.token,opacities)
            return self.assign_props(layer_dict)

    def outline_color_by(self, field, type, colors = {}):
        if field == 'category':
            layer_dict = apply_category_outline_colors(self.to_dict(),field,config.token,colors)
            return self.assign_props(layer_dict)
