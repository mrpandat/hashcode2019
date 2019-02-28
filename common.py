def calc_score(photo1, photo2):
    if (photo1['id'] == photo2['id']):
        return 0

    common_els = list(set(photo1['tags']).intersection(photo2['tags'])).__len__()
    uncommon_els1 = list(set(photo1['tags']) - set(photo2['tags'])).__len__()
    uncommon_els2 = list(set(photo2['tags']) - set(photo1['tags'])).__len__()

    data =  min([common_els, uncommon_els1, uncommon_els2])


    return data


def get_slide_tags(slide):
    slide_tags = list()
    for photo in slide['photos']:
        slide_tags += photo['tags']
    slide_tags = list(set(slide_tags))
    return slide_tags


def calc_score_better(slide1, slide2):
    slide1_tags = get_slide_tags(slide1)
    slide2_tags = get_slide_tags(slide2)

    common_els = list(set(slide1_tags).intersection(slide2_tags))
    uncommon_els1 = list(set(slide1_tags) - set(slide2_tags))
    uncommon_els2 = list(set(slide2_tags) - set(slide1_tags))

    data = min([len(common_els), len(uncommon_els1), len(uncommon_els2)])

    return data

