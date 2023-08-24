from .listings_scraper import ListingsScraper
from .posting_scraper import PostingScraper

class JobMatch:
    def __init__(self, company_name, listings_url, search_words, exclude_words):
        self.company = company_name
        self.url = listings_url
        self.search_words = search_words
        self.exclude_words = exclude_words
    
    def get_matches(self, top = -1):
        listings_scraper = ListingsScraper(self.url, self.search_words, self.exclude_words)
        roles = listings_scraper.get_all_roles()
        
        up_to = len(roles)
        if top > 0:
            up_to = min(top, len(roles))
        
        for role_title, role_url in roles[0:up_to]:
            posting_scraper = PostingScraper(role_title, role_url)
            title, location, yoes = posting_scraper.get_data()

            print(f"==================== title: {title} ====================")
            print(f"role_title: {role_title}")
            print(role_url)
            print(f"location: {location}")
            
            print("experience information:")
            for exp in yoes:
                print(f"    - {exp}...")
            
            print()
            print()

        print(f"found {len(roles)} jobs!")
