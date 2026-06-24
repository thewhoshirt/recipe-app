from kivy.uix.screenmanager import Screen

class UrlInputScreen(Screen):
    def submit_url(self):
        url = self.ids['url_input'].text

        recipe_screen = self.manager.get_screen('recipe_card')
        recipe_screen.show_recipe(url)
        self.manager.current = 'recipe_card'

        self.ids['url_input'].text = ''