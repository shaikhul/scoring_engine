class Quartile(object):
    BRONZE = 'bronze'
    SILVER = 'silver'
    GOLD = 'gold'
    PLATINUM = 'platinum'

    quartile_list = [BRONZE, SILVER, GOLD, PLATINUM]

    @classmethod
    def get_quartile(cls, normalized_score):
        if normalized_score is not None:
            try:
                return cls.quartile_list[normalized_score / 25]
            except IndexError:
                return cls.PLATINUM
