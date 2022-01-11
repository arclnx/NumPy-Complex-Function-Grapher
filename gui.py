import wx


class Gui(wx.Frame):

    def __init__(self, parent, title):
        super(Gui, self).__init__(parent, title=title,
            size=(350, 250))
        
        self.Center()

def main():

    app = wx.App()
    ex = Gui(None, title='Sizing')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()