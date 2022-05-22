from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form6')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form7')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form8')























 