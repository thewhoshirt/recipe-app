from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screens.url_input import UrlInputScreen
from screens.recipe_card import RecipeCardScreen
Builder.load_file('recipe_tin.kv')

class RecipeTinApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(UrlInputScreen(name='url_input'))
        sm.add_widget(RecipeCardScreen(name='recipe_card'))
        return sm

if __name__ == '__main__':
    RecipeTinApp().run()