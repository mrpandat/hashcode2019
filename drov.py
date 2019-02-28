photo1 = {"id": 1, "direction": 'v', "tags": ['cat', 'garden']};
photo2 = {"id": 2, "direction": 'v', "tags": ['cat', 'sun', 'beach']};
photo3 = {"id": 3, "direction": 'h', "tags": ['ptdr', 'sdr']};
photos = [
    photo1,
    photo1,
    photo2,
    photo3,
    photo3
]

input = {
    "nb_photos": 12,
    "photos": photos,
    "slides": []
}

output = {
    "slides": [
        {
            "photos": [1, 2]
        }
    ]
}


def sort_orientation(photos):
    photos_res = {
        "v": [],
        "h": []
    }

    for photo in photos:
        if (photo['direction'] == "h"):
            photos_res['h'].append(photo)
        else:
            photos_res['v'].append(photo)

    return photos_res



def calc_score(photo1, photo2):
    if (photo1['id'] == photo2['id']):
        return 0

    common_els = list(set(photo1['tags']).intersection(photo2['tags'])).__len__()
    uncommon_els1 = list(set(photo1['tags']) - set(photo2['tags'])).__len__()
    uncommon_els2 = list(set(photo2['tags']) - set(photo1['tags'])).__len__()

    data =  min([common_els, uncommon_els1, uncommon_els2])


    return data;


calc_score(photo1, photo2)

photos_sorted = sort_orientation(photos)

for photo in photos_sorted['h']:

    tags = photo['tags'];
    for photo2 in photos_sorted['h']:
        if (photo2['id'] == photo['id']):
            continue;
        score = calc_score(photo, photo2)

