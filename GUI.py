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
		self.panel = BoxSizerPanel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.panel, 1, wx.EXPAND)
		self.SetSizer(sizer)
		image_file = os.path.abspath("./images/Icon.png")
		icon = wx.Icon(image_file,wx.BITMAP_TYPE_PNG)
		self.SetIcon(icon)
		self.SetInitialSize()
		
		
class BoxSizerPanel(wx.Panel):
	def __init__(self, parent,id=wx.ID_ANY,title="Main Page",pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name="Main_Window", *args,**kwargs):
		super(BoxSizerPanel,self).__init__(parent,*args,**kwargs)
		image_file = os.path.abspath("./images/back.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		# image's upper left corner anchors at panel coordinates (0, 0)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)
		
		
class Angle_sensor(wx.Frame)
	def __init__(self,parent,*arfs,**kwargs)
		self.panel = AnglePanel(self)
		
		

class AnglePanel(wx.Panel):
	def __init__(self, parent,id=wx.ID_ANY,title="AngleSensor",pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name="Main_Window", *args,**kwargs):
		super(AnglePanel,self).__init__(parent,*args,**kwargs)
		image_file = os.path.abspath("./images/back.png")
		bmp1 = wx.Bitmap(image_file, wx.BITMAP_TYPE_PNG)
		# image's upper left corner anchors at panel coordinates (0, 0)
		self.bitmap1 = wx.StaticBitmap(self, bitmap=bmp1)		
		
if __name__=="__main__":
	app = OIKOS(False)
	app.MainLoop()