from ._anvil_designer import Form6Template
from anvil import *
import anvil.server

class Form6(Form6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    knowledge_graph = anvil.server.call('query',self.category_dropdown.selected_value,self.keyword_dropdown.selected_value)
    text_explanation = anvil.server.call('query1',self.category_dropdown.selected_value,self.keyword_dropdown.selected_value)
    self.generated_explanation.visible = True
    self.generated_knowledge_graph.visible = True   
    self.generated_explanation.text = text_explanation 
    self.generated_knowledge_graph.source = knowledge_graph
    
    if text_explanation.__contains__('chosen'):
        self.download_link.visible = False
        
        #anvil.media.download(knowledge_graph)
    else:
        self.download_link.visible = True
        self.download_link.url = knowledge_graph

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')


