def picklunch(keyword, options):
    #https://github.com/slimkrazy/python-google-places
    from googleplaces import GooglePlaces, types, lang
    import numpy as np
    import csv

    YOUR_API_KEY = 'AIzaSyA7_5HG1Zzf6RvgbTSOQhnkJ2O275U892o'
    
    google_places = GooglePlaces(YOUR_API_KEY)
    
    query_result = google_places.radar_search(
        location='29.581519,-95.440443', keyword=search_for,
        radius=8000, types=[types.TYPE_FOOD])
    
    for place in query_result.places:
        place.get_details()
    
    placenames = [place.name for place in query_result.places]
    addresses = [place.formatted_address for place in query_result.places]
    
    u, indices = np.unique(placenames, return_index=True)
    lunchresults = np.column_stack((placenames, addresses))[indices]
    
    # add prior
    prior = np.genfromtxt('prior.csv', delimiter = ";", dtype=None).reshape((1,2))
    lunchresults = np.concatenate((lunchresults, prior))
    
    #sample
    todaysresults = lunchresults[np.random.choice(lunchresults.shape[0], samplesize, replace = False),:]
    print(todaysresults)
    return




picklunch('lunch', 7)