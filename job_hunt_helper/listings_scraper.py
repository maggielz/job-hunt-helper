from utils.scrape_html import ScrapeHTML
from utils.text_search import TextSearch

class ListingsScraper:
    def __init__(self, url, search_words, exclude_words):
        self.url = url
        self.search_words = search_words
        self.exclude_words = exclude_words

    # return true if link is valid
    def link_url_valid(self, href):
        if not (href.startswith("https://")):
            return False
        if not ('job' in href or 'career' in href):
            return False
        return True
    
    # return true if text is valid
    def link_text_valid(self, txt):
        if not TextSearch.text_contains(txt, self.search_words):
            return False
        if TextSearch.text_contains(txt, self.exclude_words):
            return False
        return True

    def get_all_roles(self):
        soup = ScrapeHTML.get_html_with_driver(self.url)

        roles = []
        job_count = 0

        for link in soup.find_all('a'):
            href = link.attrs.get("href", "")
            txt = link.text.lower().strip()

            # filter links by url
            if not self.link_url_valid(href):
                continue

            # filter links by text
            if not self.link_text_valid(txt):
                continue

            job_count += 1
            roles.append((txt, href))
        
        print(f"found {job_count} jobs!")
        return roles