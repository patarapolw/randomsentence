from randomsentence import Sentence, Word


if __name__ == '__main__':
    print(Sentence().with_rating())
    """
    [('The', 0), ('host', 1655), ('and', 2), ('audience', 3130), ('are', 19), ('judge', 2566), ('and', 2), ('jury', 5933), ('for', 6), ('the', 0), ('whole', 940), ('family,', inf), ('with', 12), ('trams', inf), ('and', 2), ('launches', 7665), ('to', -1), ('take', 245), ('guests', 3177), ('to', -1), ('represent', 2975), ('strongly', 4253), ('contrary', 6810), ('positions.', inf)]
    """

    print(Word().random())
    """ford"""
