from job_hunt_helper.listings_scraper import ListingsScraper
from job_hunt_helper.posting_scraper import PostingScraper
from job_hunt_helper.job_match import JobMatch

import csv

search_words = ['software', 'engineer']
exclude_words = ['senior', 'staff', 'principal', 'lead', 'manager', 'intern', 'co-op']


print("""
##############################
Welcome to job-hunt-helper!
Get key data for all listings of company or a specific posting.
Type 'quit' or 'exit' to stop program.
##############################
      """)

def get_sorted_keys(unsorted_dict):
    return sorted(unsorted_dict.keys())

listings = {}
with open('data/companies.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        listings[row[0]] = row[1]


while True:
    get_input = input("all listings or specific posting [l/p]? ")

    if get_input == "quit" or get_input == "exit":
        break
    
    if get_input == "l":

        supported_companies = get_sorted_keys(listings)
        print("choose company from list, or paste url directly")
        print("supported companies:")
        for company in supported_companies:
            print(f"  - {company}")
        
        company_input = input("company or url: ")

        company_name = "unspecified"
        url = company_input.strip()
        if company_input.strip() in listings:
            company_name = company_input.strip()
            url = listings[company_name]

        print(f"chosen url {url}")

        search_words_input = input("search words (separate by comma): ")
        exclude_words_input = input("exclude words (separate by comma): ")

        search_words += search_words_input.strip().split(",")
        exclude_words += exclude_words_input.strip().split(",")

        print(f"search words {search_words}")
        print(f"exclude words {exclude_words}")

        print(f"\nSearching for listings from {company_input}...\n")
        job_matcher = JobMatch(company_name, url, search_words, exclude_words)
        job_matcher.get_matches()
    
    if get_input == "p":
        company_input = input("posting url: ")

        url = company_input.strip()
        print(f"chosen url {url}")
        posting_scraper = PostingScraper("unspecified", url)
        title, location, yoes = posting_scraper.print_data()

print("\njob-hunt-helper has ended")
