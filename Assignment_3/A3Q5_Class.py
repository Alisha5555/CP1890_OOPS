class Sales():
    def __init__(self, ID=0, amount=0.0, salesDate='0000-00-00', region=' '):
        self.ID = ID
        self.amount = amount
        self.salesDate = salesDate
        self.region = region


class Region():
    def __init__(self, code=" ", name=" "):
        self.code = code
        self.name = name


class ImportedFiles():
    def __init__(self, filename=" "):
        self.filename = filename


class Region():
    def __init__(self, code=" ", name=" "):
        self.code = code
        self.name = name


class Regions():
    def __init__(self):
        self.list_of_regions = []
        self.list_region_codes = []