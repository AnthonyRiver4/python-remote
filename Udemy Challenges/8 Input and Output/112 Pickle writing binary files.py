#serialization used to store data in files for future use

import pickle

# imelda = ('More Mayhem', 
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem')))

# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

#data comes out with strange characters due to binary data

#---------------------------
#lets load it back
#read from data file and convert back into readable data
# with open("imelda.pickle", 'rb') as imelda_pickled:
#     imeldaP = pickle.load(imelda_pickled)

# print(imeldaP)

# album,artist, year, track_list = imeldaP

# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)