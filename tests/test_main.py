

import mock
import unittest2

import eveimageserver

class EVEImageServerTestCase(unittest2.TestCase):
    """ Test for the EVE Image Server package. """

    def setUp(self):
        pass

    @mock.patch('os.environ.get')
    def test_get_image_server_link_os_variable(self, mock_os):
        """ Tests that the method properly uses a URL from the environment variables. """

        mock_os.return_value = 'http://example.com/'
        image_link = eveimageserver.get_image_server_link(1234, 'type')

        self.assertEqual(image_link, 'http://example.com/Type/1234_128.png')

    @mock.patch('os.environ.get')
    def test_get_character_links(self, mock_os):
        """ Test get_character_links gets the correct dictionary back. """

        mock_os.return_value = 'http://example.com/'
        links = eveimageserver.get_character_links(123456)

        self.assertEqual(
            links,
            {
                32: 'http://example.com/Character/123456_32.jpg',
                64: 'http://example.com/Character/123456_64.jpg',
                128: 'http://example.com/Character/123456_128.jpg',
                256: 'http://example.com/Character/123456_256.jpg',
                512: 'http://example.com/Character/123456_512.jpg',
                1024: 'http://example.com/Character/123456_1024.jpg',
            }
        )

    @mock.patch('os.environ.get')
    def test_get_corporation_links(self, mock_os):
        """ Test get_corporation_links gets the correct dictionary back. """

        mock_os.return_value = 'http://example.com/'
        links = eveimageserver.get_corporation_links(123456)

        self.assertEqual(
            links,
            {
                32: 'http://example.com/Corporation/123456_32.png',
                64: 'http://example.com/Corporation/123456_64.png',
                128: 'http://example.com/Corporation/123456_128.png',
                256: 'http://example.com/Corporation/123456_256.png',
            }
        )

    @mock.patch('os.environ.get')
    def test_get_alliance_links(self, mock_os):
        """ Test get_alliance_links gets the correct dictionary back. """

        mock_os.return_value = 'http://example.com/'
        links = eveimageserver.get_alliance_links(123456)

        self.assertEqual(
            links,
            {
                32: 'http://example.com/Alliance/123456_32.png',
                64: 'http://example.com/Alliance/123456_64.png',
                128: 'http://example.com/Alliance/123456_128.png',
            }
        )

    @mock.patch('os.environ.get')
    def test_get_faction_links(self, mock_os):
        """ Test get_faction_links gets the correct dictionary back. """

        mock_os.return_value = 'http://example.com/'
        links = eveimageserver.get_faction_links(123456)

        self.assertEqual(
            links,
            {
                32: 'http://example.com/Alliance/123456_32.png',
                64: 'http://example.com/Alliance/123456_64.png',
                128: 'http://example.com/Alliance/123456_128.png',
            }
        )

    @mock.patch('os.environ.get')
    def test_get_type_links(self, mock_os):
        """ Test get_type_links gets the correct dictionary back. """

        mock_os.return_value = 'http://example.com/'
        links = eveimageserver.get_type_links(123456)

        self.assertEqual(
            links,
            {
                32: 'http://example.com/Type/123456_32.png',
                64: 'http://example.com/Type/123456_64.png',
            }
        )

    @mock.patch('os.environ.get')
    def test_get_render_links(self, mock_os):
        """ Test get_type_links gets the correct dictionary back. """

        mock_os.return_value = 'http://example.com/'
        links = eveimageserver.get_render_links(123456)

        self.assertEqual(
            links,
            {
                32: 'http://example.com/Render/123456_32.png',
                64: 'http://example.com/Render/123456_64.png',
                128: 'http://example.com/Render/123456_128.png',
                256: 'http://example.com/Render/123456_256.png',
                512: 'http://example.com/Render/123456_512.png',
            }
        )

    @mock.patch('os.environ.get')
    def test_get_image_server_link_fac_type(self, mock_os):
        """ Test get_image_server_link gets the correct link for fac image_type. """

        mock_os.return_value = 'http://example.com/'
        image_link = eveimageserver.get_image_server_link(123456, 'fac', 128)

        self.assertEqual(
            image_link, 'http://example.com/Alliance/123456_128.png'
        )
