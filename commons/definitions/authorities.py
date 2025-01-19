import datetime
from abc import ABC

class IEC:
    def __init__(self):
        self.name = 'International Electrotechnical Commission'
        self.acronmyn = 'IEC'
        self.type = 'Standards Organization'
        self.purpose = 'Standardization for electrical technology, electronics and related fields.'
        self.official_languages = ['english', 'french']
        self.formed_on = datetime.date(1906, 5, 26)
        self.website = 'www.iec.ch'  # TODO: Turn into a URL Object