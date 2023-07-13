from cffconvert.behavior_1_0_x.zenodo_creator import ZenodoCreator
from cffconvert.behavior_1_x_x.zenodo_object_shared import ZenodoObjectShared as Shared


class ZenodoObject(Shared):

    supported_cff_versions = [
        "1.0.1",
        "1.0.2",
        "1.0.3"
    ]

    def add_creators(self):
        authors_cff = self.cffobj.get("authors", [])
        creators_zenodo = [ZenodoCreator(a).as_dict() for a in authors_cff]
        self.creators = [c for c in creators_zenodo if c is not None]
        return self

    def add_publication_date(self):
        if "date-released" in self.cffobj.keys():
            year = self.cffobj["date-released"].year
            month = self.cffobj["date-released"].month
            day = self.cffobj["date-released"].day
            self.publication_date = f"{year:d}-{month:02d}-{day:02d}"
        return self

    def add_upload_type(self):
        # CFF v1.0.x assumes the metadata describes software
        self.upload_type = "software"
        return self
