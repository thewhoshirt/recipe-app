from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import requests
from recipe_scrapers import scrape_html

# gets recipe data from the url using recipe scraper library
def recipe_scraper(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
        }
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        html = resp.text
        scraper = scrape_html(html, org_url=url)
        return scraper.to_json()
    except Exception as e:
        print(e)
        return None


class RecipeWidgets(BoxLayout):
    def update_recipe_card(self, recipe):
        # if an error occurs in the recipe_scraper function, displays that no recipe was found
        if recipe is None:
            self.ids.recipe_card.text = "No Recipe Found"
        else:
            # sets displayable ingredients and instructions
            ingredients = ""
            instructions = ""
            index = 1
            for i in recipe["ingredients"]:
                ingredients += i + "\n"
            for i in recipe["instructions_list"]:
                instructions += str(index) + ". " + i + "\n"
                index += 1

            # formats recipe card
            new_recipe = ("\n"+ recipe["title"] + "\n\n----------------------------\n" +
                        "Author: " + recipe["author"] + "\n" +
                        "Total time: " +
                        str(recipe["total_time"]) + "\n----------------------------\n" +
                        "Ingredients\n----------------------------\n" +
                        ingredients + "\n----------------------------\n"+
                        "Instructions\n----------------------------\n"
                        + instructions)

            # sets recipe_card label
            self.ids.recipe_card.text = new_recipe

    def recipe_card(self):
        url = self.ids.url_input.text.strip()
        # checks if anything is in the input box
        if not url:
            self.ids.recipe_card.text = "No Recipe Found"
            return

        # gets recipe from scraper and update recipe card
        recipe = recipe_scraper(url)
        self.update_recipe_card(recipe)

class RecipeApp(App):
    def build(self):
        return RecipeWidgets()

if __name__ == '__main__':
    RecipeApp().run()