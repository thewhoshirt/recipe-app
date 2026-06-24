from kivy.uix.screenmanager import Screen
from recipe_scrapers import scrape_me




class RecipeCardScreen(Screen):
    def show_recipe(self, url):
        scraper = scrape_me(url)

        steps = scraper.instructions_list()

        numbered = '\n\n'.join(f"[b]Step {i+1}:[/b] {step}" for i, step in enumerate(steps))

        self.ids['recipe_title'].text = scraper.title()
        self.ids['recipe_meta'].text = f"Time: {scraper.total_time()} mins | Yield: {scraper.yields()} "
        self.ids['recipe_source'].text = f"From the Website: {scraper.site_name()}"
        self.ids['recipe_ingredients'].text = '\n'.join(scraper.ingredients())
        self.ids['recipe_instructions'].text = numbered
