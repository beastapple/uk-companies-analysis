# UK Companies Analysis
A project to analyse and work with publicly available company data in the UK.

# Version 0.1 checklist:

My aim is to use Python and specifically Streamlit to create a user-friendly UX for this project.

## Must:
- ~~Accept the upload of a CSV spreadsheet.~~ Complete
- Broadly analyse the csv of Companies House data as from https://find-and-update.company-information.service.gov.uk/advanced-search
- Create a dashboard to summarise: ~~number of companies~~ complete; number of companies by company_type; top 100 SIC codes and number of companies per those SIC codes; a graph of the incorpoation dates broken down into months.

## Should:
- Allow for filtering and subsequent dashboard / analysis information based on the selected filters.
- Be able to separate companies with multiple SIC codes so they are counted accurately against each, e.g. a company with SICs "56103 56210" is counted as 1 x "56103" and 1 x "56210", not 1 x "56103 56210"
  
## Could:
- Allow the upload of multiple CSVs while checking for & removing duplicates based on Company Number.
- ~~Check the spreadsheet has the right headers/format and if not, display help information and cancel any further analysis.~~ Complete

## Won't:
- Extract the postcode from the Registered address to analyse location. (And then, display on a map.)

## Future ambitions:
- Show and analyse registered address location data.
- Deploy as a live app for others to use. (No idea where to start. Amazon AWS? Need to consider data security, abuse and bots too.)
- Connect to the Companies House API for live data https://developer.company-information.service.gov.uk/ 
- Combine with the UKRI API https://gtr.ukri.org/resources/gtrapi.html
- Source and combine with investment data
