def picklunch():
    #https://github.com/slimkrazy/python-google-places
    from googleplaces import GooglePlaces, types, lang
    import numpy as np
    import csv
    
    search_for = input('Search keyword:')
    while True:
        samplesize = input('Number of results to return:')
        if not samplesize in list(map(str,range(1,20))):
            print('That is not a valid option!')
        else:
            break

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
    
    keys = list(range(1,(samplesize + 1)))
    menu = dict(zip(keys, todaysresults))
    
    while True: 
        samplesize = menu.keys()
        for entry in samplesize: 
            print (entry, menu[entry])
        
        selection = input("Please Select:")
        if not selection in list(map(str, keys)):
            print('That is not a valid option!')
            time.sleep(2)
        else:
            break

    todayschoice = todaysresults[(int(selection)-1)]

    while True:
        write = input('Write selection to prior list? (y/n)')
        if not write.lower() in ['y','n']:
            print('That is not a valid option!')
        else:
            break
        
    if write == True:
        # code to add line to csv
        with open('prior.csv', 'a') as f:
            writer = csv.writer(f, delimiter = ";")
            writer.writerow(todayschoice)
    
    print(todayschoice)
    
    return




picklunch()

    