from kivy.uix.screenmanager import  SlideTransition
from kivy.app import App


class myMainApp(App):

    def setScreen(self, instance):
        if instance == self.root.ids.button_next:
            self.root.ids.screen1.parent.transition = SlideTransition(direction="left")
            self.root.ids.screen1.parent.current = "Screen 2"
        elif instance == self.root.ids.button_prev:
            self.root.ids.screen2.parent.transition = SlideTransition(direction="right")
            self.root.ids.screen2.parent.current = "Screen 1"


if __name__ == '__main__':
    myApp = myMainApp()
    myApp.run()