from ._anvil_designer import Form3Template
from anvil import *
import anvil.media
import anvil.server

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    


    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    knowledge_graph = anvil.server.call('category_subclasses',self.category_dropdown_copy.selected_value)
    text_explanation = anvil.server.call('category_subclasses1',self.category_dropdown_copy.selected_value)
    self.generated_explanation_copy.visible = True
    self.generated_knowledge_graph_copy.visible = True
    self.download_link.visible = True

    self.generated_explanation_copy.text = text_explanation 
    self.generated_knowledge_graph_copy.source = knowledge_graph
    self.download_link.url = knowledge_graph
    #anvil.media.download(knowledge_graph)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')



