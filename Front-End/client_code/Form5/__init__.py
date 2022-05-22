from ._anvil_designer import Form5Template
from anvil import *
import anvil.server

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    knowledge_graph = anvil.server.call('relations_based_on_keyword',self.keyword_dropdown_copy.selected_value)
    text_explanation = anvil.server.call('relations_based_on_keyword1',self.keyword_dropdown_copy.selected_value)
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



