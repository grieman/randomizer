search_for = "mexican"

#https://github.com/slimkrazy/python-google-places
from googleplaces import GooglePlaces, types, lang
import numpy as np

YOUR_API_KEY = 'AIzaSyA7_5HG1Zzf6RvgbTSOQhnkJ2O275U892o'

google_places = GooglePlaces(YOUR_API_KEY)

query_result = google_places.nearby_search(
        location='29.581519,-95.440443', keyword=search_for,
        radius=8000, types=[types.TYPE_FOOD])
        
for place in query_result.places:
    place.get_details()
    
placenames = [place.name for place in query_result.places]
addresses = [place.formatted_address for place in query_result.places]


if query_result.has_next_page_token:
    query_result_next_page = google_places.nearby_search(
            pagetoken=query_result.next_page_token)
            
    for place in query_result_next_page.places:
        place.get_details()
        
    placenames.extend([place.name for place in query_result_next_page.places])
    addresses.extend([place.formatted_address for place in query_result_next_page.places])
            
    if query_result_next_page.has_next_page_token:
            query_result_next_page2 = google_places.nearby_search(
                    pagetoken=query_result_next_page.next_page_token)
            for place in query_result_next_page.places:
                place.get_details()
        
            placenames.extend([place.name for place in query_result_next_page.places])
            addresses.extend([place.formatted_address for place in query_result_next_page.places])
            
       
np.unique(placenames, return_index=True)            
lunchresults = np.column_stack((placenames, addresses))

