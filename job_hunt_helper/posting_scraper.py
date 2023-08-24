from utils.scrape_html import ScrapeHTML
import re

class PostingScraper:
    def __init__(self, role_title, url):
        self.role_title = role_title
        self.url = url
    
    # works for greenhouse and lever postings
    def get_job_title(self, soup):
        title_tags = ["h1", "h2"]
        title = "not found"
        for tag in title_tags:
            titles = soup.find_all(tag)
            if len(titles) > 0:
                title = titles[0].text.lower().strip()
                break
        return title
    
    # works for greenhouse and lever postings
    def get_location(self, soup):
        locations = soup.find_all("div", attrs = {"class": 'location'})
        location = "not found"
        if len(locations) > 0:
            location = locations[0].text.lower().strip()
        return location
    
    # kinda works
    def get_years_experience(self, soup):
        regex_string = r'.*(?:years|yoe).*'
        lines = soup.find_all(string = re.compile(regex_string))

        experiences = []
        for line in lines:
            text_to_search = line.text.lower().strip()

            regex_string = r'^.*[0-9][a-z +]{0,30}?(?:years|yoe).{0,100}'
            regex_string = r'^.*[0-9][a-z +]{0,30}?years.{0,100}'
            matches = re.findall(regex_string, text_to_search)
            experiences += matches

        return experiences

    def print_data(self):
        soup = ScrapeHTML.get_html(self.url)
        job_title = self.get_job_title(soup)
        location = self.get_location(soup)
        yoes = self.get_years_experience(soup)

        print(f"==================== title: {job_title} ====================")
        print(f"role_title: {self.role_title}")
        print(self.url)
        print(f"location: {location}")
        
        print("experience information:")
        for exp in yoes:
            print(f"    - {exp}...")
            
        return job_title, location, yoes

    def get_data(self):
        soup = ScrapeHTML.get_html(self.url)
        job_title = self.get_job_title(soup)
        location = self.get_location(soup)
        yoes = self.get_years_experience(soup)
        return job_title, location, yoes
