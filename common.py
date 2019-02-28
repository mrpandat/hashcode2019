
def calc_score(photo1, photo2):
    if (photo1['id'] == photo2['id']):
        return 0

    common_els = list(set(photo1['tags']).intersection(photo2['tags'])).__len__()
    uncommon_els1 = list(set(photo1['tags']) - set(photo2['tags'])).__len__()
    uncommon_els2 = list(set(photo2['tags']) - set(photo1['tags'])).__len__()

    data =  min([common_els, uncommon_els1, uncommon_els2])


    return data;


