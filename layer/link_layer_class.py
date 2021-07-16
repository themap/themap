
from .functions import delete_link_layer
from .functions import update_link_layer
from .functions import add_links_to_link_layer
from .functions import add_link_property
from ..common import config

class LinkLayer:
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
        return delete_link_layer(self.ID,config.token)

    def update(self, options = {}):
        for key in options:
            setattr(self,key,options[key])
        layer_dict = update_link_layer(self.to_dict(),config.token)
        return self.assign_props(layer_dict)
    
    def add_links(self, links):
        links = add_links_to_link_layer(self.ID,links,config.token)
        for link in links:
            self.Links.append(link)
        return links
    
    def add_link_property(self, link, name, value):
        add_link_property(link,name,value,config.token)
        
