from ._anvil_designer import Form4Template
from anvil import *
import anvil.server

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = ""
    self.generated_explanation_copy.visible = True
    if self.keyword_dropdown_copy.selected_value == "source nodes":
      result = anvil.server.call('all_source_nodes')
      
    elif self.keyword_dropdown_copy.selected_value == "target nodes":
      result = anvil.server.call('all_target_nodes') 
    
    elif self.keyword_dropdown_copy.selected_value == "edges":
      result = anvil.server.call('all_keywords')

    self.generated_explanation_copy.text = result

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')


