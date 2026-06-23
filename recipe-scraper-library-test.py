# https://github.com/hhursev/recipe-scrapers/tree/main
# https://docs.recipe-scrapers.com/


#    pip install recipe-scrapers

import requests
from recipe_scrapers import scrape_html
from recipe_scrapers._exceptions import WebsiteNotImplementedError, NoSchemaFoundInWildMode

try:
    # example test input:
    # https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/
    url = input("Enter the recipe URL: ").strip()




    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
    }
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status() # will raise an HTTPError if the HTTP request returns an unsuccessful status code

    html = resp.text 
    # print(html[:800])  # verify this is the actual recipe HTML

    scraper = scrape_html(html, org_url=url) # scraper object to use with library methods




    # example of use

    # help(scraper) # to see all available methods and properties of the scraper object


    saved_recipe = scraper.to_json() # saves all available data to json

    # prints example recipe "card"
    print("---------------------------------------")
    print("---", saved_recipe["title"], "---")
    
    print("Total Time:", saved_recipe["total_time"])
    print("--- Ingredients ---")
    for i in saved_recipe["ingredients"]:
        print(i)
    print("--- Instructions ---")
    print(saved_recipe["instructions"])
    print("---------------------------------------")

    
except WebsiteNotImplementedError as e:
    # print(f"Website not supported: {e}")
    print(f"Website not supported.")
    
except NoSchemaFoundInWildMode as e:
    # print(f"No recipe schema found: {e}")
    print(f"Website not supported and no recipe schema found.")
    
except Exception as e:
    print(f"Other error occurred: {e}")