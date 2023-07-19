import os
from pykwalify.core import Core
from ruamel.yaml import YAML
from cffconvert.cff_1_1_x.apalike import ApalikeObject
from cffconvert.cff_1_1_x.bibtex import BibtexObject
from cffconvert.cff_1_1_x.codemeta import CodemetaObject
from cffconvert.cff_1_1_x.endnote import EndnoteObject
from cffconvert.cff_1_1_x.ris import RisObject
from cffconvert.cff_1_1_x.schemaorg import SchemaorgObject
from cffconvert.cff_1_1_x.zenodo import ZenodoObject
from cffconvert.contracts.citation import Contract
from cffconvert.root import get_package_root


class Citation_1_1_x(Contract):  # noqa

    supported_cff_versions = [
        "1.1.0"
    ]

    def __init__(self, cffstr, cffversion):
        self.cffstr = cffstr
        self.cffversion = cffversion
        self.cffobj = self._parse()
        self.schema = self._get_schema()

    def _get_schema(self):
        schema_path = os.path.join(get_package_root(), "schemas", self.cffversion, "schema.yaml")
        with open(schema_path, "rt", encoding="utf-8") as fid:
            return YAML(typ="safe").load(fid.read())

    def _parse(self):
        cffobj = YAML(typ="safe").load(self.cffstr)
        if not isinstance(cffobj, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")
        return cffobj

    def as_apalike(self):
        return ApalikeObject(self.cffobj).as_string()

    def as_bibtex(self):
        return BibtexObject(self.cffobj).as_string()

    def as_cff(self):
        return self.cffstr

    def as_codemeta(self):
        return CodemetaObject(self.cffobj).as_string()

    def as_endnote(self):
        return EndnoteObject(self.cffobj).as_string()

    def as_ris(self):
        return RisObject(self.cffobj).as_string()

    def as_schemaorg(self):
        return SchemaorgObject(self.cffobj).as_string()

    def as_zenodo(self):
        return ZenodoObject(self.cffobj).as_string()

    def validate(self, verbose=True):
        # validation using YAML based schema
        if verbose:
            print("--verbose behavior not implemented for cff-version 1.1.x, continuing...")
        Core(source_data=self.cffobj, schema_data=self.schema).validate(raise_exception=True)
