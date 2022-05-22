from ._anvil_designer import Form7Template
from anvil import *
import anvil.server

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.generated_knowledge_graph_copy.visible = False
    self.download_link.visible = False
    knowledge_graph = anvil.server.call('most_important_features',self.text_box_1.text)
    result = anvil.server.call('most_important_features1',self.text_box_1.text)
    if self.text_box_1.text == "":
      self.generated_explanation_copy.visible = True
      self.generated_explanation_copy.text = "Please enter a value."
    else:  
      self.generated_explanation_copy.visible = True
      self.generated_knowledge_graph_copy.visible = True
      self.download_link.visible = True

      self.generated_explanation_copy.text = result 
      self.generated_knowledge_graph_copy.source = knowledge_graph
      self.download_link.url = knowledge_graph

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')


