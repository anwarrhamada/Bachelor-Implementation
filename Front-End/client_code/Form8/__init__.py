from ._anvil_designer import Form8Template
from anvil import *
import anvil.server

class Form8(Form8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = ""
    self.generated_explanation_copy.visible = True
    self.generated_knowledge_graph_copy.visible = True
    
    if self.keyword_dropdown_copy.selected_value == "Random Forest Regressor":
      knowledge_graph = anvil.server.call('most_important_features_by_forward_feature_selection')
      result = anvil.server.call('most_important_features_by_forward_feature_selection1')
      
    elif self.keyword_dropdown_copy.selected_value == "Decision Tree Regressor":
      knowledge_graph = anvil.server.call('most_important_features_by_decision_tree')
      result = anvil.server.call('most_important_features_by_decision_tree1') 
    
    elif self.keyword_dropdown_copy.selected_value == "GBRT":
      knowledge_graph = anvil.server.call('most_important_features_by_gbrt')      
      result = anvil.server.call('most_important_features_by_gbrt1')      
      
    self.generated_explanation_copy.text = result  
    self.generated_knowledge_graph_copy.source = knowledge_graph
    self.download_link.visible = True
    self.download_link.url = knowledge_graph

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')


