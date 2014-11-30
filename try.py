import wx
import os
import wx.lib.platebtn as pbtn
import wx.lib.agw.gradientbutton as gbtn 

class OIKOS(wx.App):
	def OnInit(self):
		self.frame = Main_Window(None, title="OIKOS Demo Board")
		self.SetTopWindow(self.frame)
		self.frame.Show()
		return True


class Main_Window(wx.Frame):
	def __init__(self, parent,id=wx.ID_ANY,title="Main Page",pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name="Main_Window",*args, **kwargs):
		super(Main_Window, self).__init__(parent,id,title,pos,size,style,name="Main_Window",*args,**kwargs)
		vsizer = wx.BoxSizer(wx.VERTICAL)
		hsizer = wx.BoxSizer(wx.HORIZONTAL)
		
		#self.Panel1 = gui1(self)
		#self.Panel2 = gui2(self)
		#self.Panel3 = gui3(self)
		
		self.Panel1 = gui1(self)
		self.Panel2 = gui2(self)
		self.Panel3 = gui3(self)
		vsizer.AddSpacer(100)
		vsizer.Add(self.Panel2,1)
		vsizer.AddSpacer(15)
		vsizer.Add(self.Panel3,2)
		
		hsizer.AddSpacer(50)
		hsizer.Add(self.Panel1,1)
		hsizer.AddSpacer(15)
		hsizer.Add(vsizer,2)
		hsizer.AddSpacer(50)
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetAutoLayout(True)
		self.SetSizer(hsizer)
		image_file = os.path.abspath("./images/back.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		# image's upper left corner anchors at panel coordinates (0, 0)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)
		self.Layout()
		image_file = os.path.abspath("./images/Icon.png")
		icon = wx.Icon(image_file,wx.BITMAP_TYPE_PNG)
		self.SetIcon(icon)
		self.SetInitialSize()
		
		
class gui1(wx.Panel):
	def __init__(self, parent,id=wx.ID_ANY,title="Main Page",style=wx.DEFAULT_FRAME_STYLE,name="Main_Window", *args,**kwargs):
		super(gui1,self).__init__(parent,*args,**kwargs)
		image_file = os.path.abspath("./images/red.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)


class gui2(wx.Panel):
	def __init__(self, parent,id=wx.ID_ANY,title="Main Page",style=wx.DEFAULT_FRAME_STYLE,name="Sensors_window", *args,**kwargs):
		super(gui2,self).__init__(parent,*args,**kwargs)
		image_file = os.path.abspath("./images/green.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)	
		
class gui3(wx.Panel):
	def __init__(self, parent,id=wx.ID_ANY,title="Main Page",style=wx.DEFAULT_FRAME_STYLE,name="Additional", *args,**kwargs):
		super(gui3,self).__init__(parent,*args,**kwargs)
		image_file = os.path.abspath("./images/blue.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)
		
		
#class gui1(wx.Panel):
#	def __init__(self, parent,id=wx.ID_ANY,title="Main Page",pos=wx.DefaultPosition, size=wx.DefaultSize*.5,style=wxTAB_TRAVERSAL|wxNO_BORDER,name="GUI1", *args,**kwargs):
		
		
		
class Angle_sensor(wx.Frame):
	def __init__(self,parent,*arfs,**kwargs):
		self.panel = AnglePanel(self)
		image_file = os.path.abspath("./images/back.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		# image's upper left corner anchors at panel coordinates (0, 0)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)
		

class AnglePanel(wx.Panel):
	def __init__(self, parent,id=wx.ID_ANY,title="AngleSensor",pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name="Main_Window", *args,**kwargs):
		super(AnglePanel,self).__init__(parent,*args,**kwargs)
				
		
if __name__=="__main__":
	app = OIKOS(False)
	app.MainLoop()