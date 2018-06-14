from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Image import Image
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.RadioButton import RadioButton
from pyjamas.ui.Label import Label
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Button import Button
class emfDemo(simplePanel):
	def __init__(self):
		SimplePanel.__init__(self)
	panel= VerticalPanel()

	panel0=HorizontalPanel()
	panel0.add(RadioButton("group1","INFINITE")
	panel0.add(RadioButton("group1","finite")
	
	panel.add(panel0)
	
	wire=Image("pictures/wire.png")
	wire.addClickListener(getattr(self, "wireClick"))
	box=Image("pictures/box.png")
	box.addClickListener(getattr(self, "boxClick"))
	block=Image("pictures/block.png")
	block.addClickListener(getattr(self,"blockClick"))
	rod=Image("pictures/rod.png")
	rod.addClickListener(getattr(self,"rodClick"))
	tube=Image("pictures/tube.png")
	tube.addClickListener(getattr(self."tubeClick"))
	plates=Image("pictures/plates.png")
	plates.addClickListener(getattr(self."tubeClick"))

	panel1=HorizontalPanel()
	panel1.add(wire)
	panel1.add(box)
	panel1.add(block)
	panel1.add(rod)
	panel1.add(tube)
	panel1.add(plates)
	
	panel.add(panel1)

	panel2=HorizontalPanel()
	
	label1=Label("Wire", wordwrap=False)
	panel2.add(label1)
	label2=Label("Box", wordwrap=False)
	panel2.add(label2)
	label3=Label("Block", wordwrap=False)
	panel2.add(label3)
	label4=Label("Rod", wordwrap=False)
	panel2.add(label4)
	label5=Label("Tube", wordwrap=False)
	panel2.add(label5)
	label6=Label("Plates", wordwrap=False)
	panel2.add(label6)

	panel.add(panel2)

	panel3=HorizontalPanel()
	
	lambda=Label("string",wordwrap=False)

	self.add(panel)

	def shapeClick(self,sender=None):
		if 
		render the rest of the form
	def platesClick(self,sender=None):
		render the rest of the form
