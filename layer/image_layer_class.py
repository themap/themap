
from .functions import delete_image_layer
from .functions import update_image_layer
from .functions import add_images_to_image_layer
from ..common import config

class ImageLayer:
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
        return delete_image_layer(self.ID,config.token)

    def update(self, options = {}):
        for key in options:
            setattr(self,key,options[key])
        layer_dict = update_image_layer(self.to_dict(),config.token)
        return self.assign_props(layer_dict)
    
    def add_images(self, images):
        images = add_images_to_image_layer(self.ID,images,config.token)
        for image in images:
            self.Images.append(image)
        return images