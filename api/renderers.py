from django.utils.encoding import smart_unicode
from rest_framework import renderers
from rest_framework.compat import (
    SHORT_SEPARATORS, LONG_SEPARATORS, StringIO, smart_text, yaml
)
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils import six
from feed.models import *
import time
from datetime import date


class PlainTextRenderer(renderers.BaseRenderer):
    """
    Renderer which serializes to XML.
    """

    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ''

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement("list", {'last_update':str(date.today()), 'listing':'834'})
        self._to_xml(xml, data)
        xml.endElement("list")
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                # xml.startElement("property", {'lastupdated': str(date.today()),'test1':'testing'})
                self._to_xml(xml, item)
                # xml.endElement("property")

        elif isinstance(data, dict):
            for key, value in six.iteritems(data):
                if key == 'property':
                    xml.startElement(key, {'lastupdate': str(date.today())})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'reference_number':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ value +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'offering_type':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ value +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'property_type':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ value +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'price_on_application':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'price':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'service_charge':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'rental_period':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'cheques':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'city':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'community':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'sub_community':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'property_name':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'title_en':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'title_ar':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'description_en':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'description_ar':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'private_amenities':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'commercial_amenities':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'view':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'plot_size':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'size':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'bedroom':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'bathroom':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'agent':
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'name':
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'email':
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'phone':
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'photo':
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'info':
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
                    # continue
                if key == 'featured':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'developer':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'build_year':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                if key == 'floor':
                    xml.startElement(key, {})
                    self._to_xml(xml, '<![CDATA[ '+ str(value) +' ]]>')
                    xml.endElement(key)
                    # continue
                # else:
                #     xml.startElement(key, {})
                #     self._to_xml(xml, value)
                #     xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(smart_text(data))