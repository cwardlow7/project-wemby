#Goal Is To Find Most Similar Player to Victor Wembenyama

# Python 3.11
# Imports
# nba_api


# 1. Pull in data
    # Which source has the best data?
    # Are we going to need to scrape data off the web or can we use an API?
    # Stats and Physical Attributes need to be taken into account
    # European stats? International? 
    # Looking on a season by season basis?  Not a lot of career stats to pull from so far

# 2. What methods will we be using?  
    # Clustering? This makes most sense on surface but is there a way to take a more supervised approach?
    # Can we confirm our findings by using obvious comparisons?  i.e. Kobe and Jordan should be near each other 
    # Anything else we should consider?

import nba_api
import umap
import hdbscan
