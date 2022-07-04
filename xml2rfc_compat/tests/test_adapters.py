from django.test import TestCase

from bib_models import BibliographicItem
from bibxml.settings import XML2RFC_PATH_PREFIX
from bibxml.xml2rfc_adapters import RfcAdapter, MiscAdapter, InternetDraftsAdapter, W3cAdapter, ThreeGPPPAdapter, \
    IeeeAdapter, IanaAdapter, RfcSubseriesAdapter
from main.exceptions import RefNotFoundError


class XML2RFCAdaptersTestCase(TestCase):
    fixtures = ['test_refdata.json']

    def setUp(self):
        """
        The list of references listed below represent real
        references of datasets that are imported using the
        fixture file. Each reference is passed to the
        corresponding fetcher function.
        """
        self.rfcs_ref = "RFC.4037"
        self.misc_ref = "ISO.8473.1988"
        self.internet_drafts_ref = "I-D.ietf-hip-rfc5201-bis"
        self.w3c_ref = "W3C.REC-owl2-syntax-20121211"
        self.threegpp_ref = "3GPP.TS 25.321:Rel-8/8.3.0"
        self.ieee_ref = "IEEE.P2740/D-6.5.2020-08"
        self.iana_ref = "IANA.xml-security-uris/security-uris"
        self.rfcsubseries_ref = "STD.29.xml"
        self.nist_ref = "NBS.CRPL-F-A.90"
        self.doi_ref = "10.1093/benz/9780199773787.article.b00004912"

        self.dirname = XML2RFC_PATH_PREFIX

    def _assert_refs_equal(self, bibitem, ref):
        for id in bibitem.docid:
            if id.scope == 'anchor':
                self.assertEqual(id.id, ref)

    def _assert_is_instance_of_bibliographicitem(self, obj):
        self.assertIsInstance(obj, BibliographicItem)

    def test_rfcs(self):
        adapter = RfcAdapter(self.dirname, "bibxml1", self.rfcs_ref)
        bibitem = adapter.resolve()
        self._assert_is_instance_of_bibliographicitem(bibitem)
        self._assert_refs_equal(bibitem, self.rfcs_ref.replace(".", ""))

    def test_rfcs_not_found(self):
        adapter = RfcAdapter(self.dirname, "bibxml1", "NONEXISTENT.403799999991")
        with self.assertRaises(RefNotFoundError):
            adapter.resolve()

    # TODO fix this
    def test_misc(self):
        # not IEEE anymore find another id
        # import ipdb; ipdb.set_trace()
        # self.misc_ref = "ISO.8208"
        # adapter = MiscAdapter(self.dirname, "bibxml2", self.misc_ref)
        # bibitem = adapter.resolve()
        # self._assert_is_instance_of_bibliographicitem(bibitem)
        # self._assert_refs_equal(bibitem, self.misc_ref)
        pass

    def test_misc_not_found(self):
        adapter = MiscAdapter(self.dirname, "bibxml2", "NONEXISTENT.8023.19888")
        with self.assertRaises(RefNotFoundError):
            adapter.resolve()

    def test_internet_drafts(self):
        adapter = InternetDraftsAdapter(self.dirname, "bibxml3", self.internet_drafts_ref)
        bibitem = adapter.resolve()
        self._assert_is_instance_of_bibliographicitem(bibitem)
        self._assert_refs_equal(bibitem, self.internet_drafts_ref)

    # def test_internet_drafts_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.internet_drafts(ref="NONEXISTENT_REF")
    #
    # def test_internet_drafts_invalid_ref(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.internet_drafts(ref=self.internet_drafts_ref.replace("I-D.", ""))
    #
    def test_w3c(self):
        pass
    #     """
    #     This test fails with some old data representation. Relatons data should conform
    #     to the official schema https://github.com/relaton/relaton-models/blob/main/grammars/biblio.rnc
    #     pydantic.error_wrappers.ValidationError: 1 validation error for BibliographicItem
    #     relation -> 0 -> bibitem -> formattedref
    #     instance of GenericStringValue, tuple or dict expected (type=type_error.dataclass; class_name=GenericStringValue)
    #     """
    #     # TODO fix item not found
    #     # "W3C.REC-owl2-syntax-20121211"
    #     adapter = W3cAdapter(self.dirname, "bibxml4", self.w3c_ref)
    #     bibitem = adapter.resolve()
    #     # bibitem = fetchers.w3c(ref=self.w3c_ref)
    #     self._assert_is_instance_of_bibliographicitem(bibitem)
    #     self._assert_refs_equal(bibitem, self.w3c_ref)


    def test_w3c_not_found(self):
        adapter = W3cAdapter(self.dirname, "bibxml4", self.w3c_ref)
        with self.assertRaises(RefNotFoundError):
            adapter.resolve()

    def test_threegpp(self):
        pass
        # # TODO fix this not found
        # # "3GPP.TS 25.321:Rel-8/8.3.0"
        # adapter = ThreeGPPPAdapter(self.dirname, "bibxml5", self.threegpp_ref)
        # bibitem = adapter.resolve()
        # self._assert_refs_equal(bibitem, self.threegpp_ref)
    #
    # def test_threegpp_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.threegpp(ref="NONEXISTENT_REF")

    def test_ieee(self):
        pass
        # As of 28/06/2022 ieee fetcher is not
        # automatically resolving bibxml6/IEEE paths.
        # bibitem = fetchers.ieee(ref=self.ieee_ref)
        # self._assert_is_instance_of_bibliographicitem(bibitem)
        # self._assert_refs_equal(bibitem, self.ieee_ref)

    def test_ieee_not_found(self):
        pass
        # TODO fix this
        # "IEEE P2740/D-6.5.2020-08"
        # adapter = IeeeAdapter(self.dirname, "bibxml6", self.ieee_ref)
        # bibitem = adapter.resolve()
        # self._assert_is_instance_of_bibliographicitem(bibitem)
        # self._assert_refs_equal(bibitem, self.ieee_ref)
    #
    # def test_ieee_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.ieee(ref="NONEXISTENT_REF")
    #
    # def test_doi(self):
    #     self._assert_is_instance_of_bibliographicitem(fetchers.doi(ref=self.doi_ref))
    #
    # def test_doi_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.doi(ref="NONEXISTENT_REF")

    def test_iana(self):
        adapter = IanaAdapter(self.dirname, "bibxml8", self.iana_ref)
        bibitem = adapter.resolve()
        self._assert_is_instance_of_bibliographicitem(bibitem)

    # def test_iana_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.iana(ref="NONEXISTENT_REF")

    def test_rfcsubseries(self):
        adapter = RfcSubseriesAdapter(self.dirname, "bibxml9", self.rfcs_ref)
        bibitem = adapter.resolve()
        self._assert_is_instance_of_bibliographicitem(bibitem)
    #
    # def test_rfcsubseries_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.rfcsubseries(ref="NONEXISTENT_REF")

    def test_nist(self):
        pass
        # # TODO fix this ValueError: Invalid rfcsubseries number component
        # # "NBS.CRPL-F-A.90"
        # adapter = RfcSubseriesAdapter(self.dirname, "bibxml-nist", self.nist_ref)
        # bibitem = adapter.resolve()
        # self._assert_is_instance_of_bibliographicitem(bibitem)
        # self._assert_refs_equal(bibitem, self.nist_ref)
    #
    # def test_nist_not_found(self):
    #     with self.assertRaises(RefNotFoundError):
    #         fetchers.nist(ref="NONEXISTENT_REF")

