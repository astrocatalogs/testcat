"""The Testcat AstroCatalog.
"""

import os

catalog_info = {
    "catalog_name": __name__,
    "catalog_class": {
        "name": "Test_Catalog",
        "file": "test_catalog",
        "path": "testcat."
    },
    "schema_path": None
}

import astrocats


class Test_Paths(astrocats.Paths):

    ROOT = os.path.join(os.path.dirname(__file__), "")
    NAME = __name__
    FILE = __file__

    def __init__(self):
        super(Test_Paths, self).__init__()

        # auxiliary datafiles
        self.TYPE_SYNONYMS = os.path.join(self.INPUT, 'type-synonyms.json')
        self.SOURCE_SYNONYMS = os.path.join(self.INPUT, 'source-synonyms.json')
        self.URL_REDIRECTS = os.path.join(self.INPUT, 'url-redirects.json')
        self.NON_SNE_TYPES = os.path.join(self.INPUT, 'non-sne-types.json')
        self.NON_SNE_PREFIXES = os.path.join(self.INPUT, 'non-sne-prefixes.json')
        self.BIBERRORS = os.path.join(self.INPUT, 'biberrors.json')
        self.ATELS = os.path.join(self.INPUT, 'atels.json')
        self.CBETS = os.path.join(self.INPUT, 'cbets.json')
        self.IAUCS = os.path.join(self.INPUT, 'iaucs.json')

        # cached datafiles
        self.EXTINCT = os.path.join(self.CACHE, 'extinctions.json')
        return

    def get_all_repo_folders(self, *args, **kwargs):
        """
        """
        all_repos = super().get_all_repo_folders(*args, **kwargs)
        return all_repos


PATHS = Test_Paths()
