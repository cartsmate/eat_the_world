from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

GUI = Builder.load_file('main.kv')


class EatTheWorld(App):
    def build(self):
        return GUI


if __name__ == '__main__':
    EatTheWorld().run()
