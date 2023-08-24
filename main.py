from job_hunt_helper.listings_scraper import ListingsScraper
from job_hunt_helper.posting_scraper import PostingScraper
from job_hunt_helper.job_match import JobMatch

# currently only supports when all listings are on one page
listings = {
    "kalshi": 'https://kalshi.com/careers',
    "figma": 'https://www.figma.com/careers/#job-openings',
    "indigo": 'https://careers.smartrecruiters.com/IndigoBooksMusic',
    "zoox": 'https://zoox.com/careers/',
    "oracle": 'https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/requisitions?keyword=software&lastSelectedFacet=LOCATIONS&mode=location&selectedFlexFieldsFacets=%22AttributeChar6%7C0+to+2%2B+years%22&selectedLocationsFacet=300000000149325%3B300000000106749',
    "gauntlet": 'https://jobs.lever.co/gauntlet/',
    "verkada": 'https://www.verkada.com/careers/#open-positions',
    "qorvo": 'https://careers.qorvo.com/search/?createNewAlert=false&q=software&optionsFacetsDD_location=&optionsFacetsDD_country=US&optionsFacetsDD_department=&optionsFacetsDD_customfield1=&optionsFacetsDD_customfield2=&optionsFacetsDD_customfield3=',
    "canonical": 'https://canonical.com/careers/all?search=software',
    "stackadapt": 'https://jobs.lever.co/stackadapt',
    "tulip": 'https://tulip.co/careers/'
}

samples = {
    "figma": 'https://boards.greenhouse.io/figma/jobs/4214847004',  # greenhouse
    "zoox": 'https://zoox.com/careers/job-opportunity/?job=c6d78cd2-952d-48c7-9dbb-940126f3037a',
    "gauntlet": 'https://jobs.lever.co/gauntlet/6bb9569e-d568-4b57-9ca9-d3cd8ac27a52',   # lever
    "figma2": 'https://boards.greenhouse.io/figma/jobs/4798668004'
}

search_words = ['software', 'engineer']
exclude_words = ['senior', 'staff', 'principal', 'lead', 'manager', 'intern', 'co-op']

COMPANY_TO_SEARCH = "tulip"

job_matcher = JobMatch("figma", listings['figma'], search_words, exclude_words)
job_matcher.get_matches()