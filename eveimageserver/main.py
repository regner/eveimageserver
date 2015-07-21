

import os

CHARACTER_SIZES = [32, 64, 128, 256, 512, 1024]
CORPORATION_SIZES = [32, 64, 128, 256]
ALLIANCES_SIZES = [32, 64, 128]
FACTION_SIZES = [32, 64, 128]
TYPE_SIZES = [32, 64, 128, 256, 512]

def get_character_links(character_id):
    """ Takes a character ID and returns a dict with all available size links.

    :param character_id: A character ID from EVE.
    :return: A dict of size and urls.
    """

    return_dict = {x: get_image_server_link(character_id, 'char', x) for x in CHARACTER_SIZES}

    return return_dict


def get_corporation_links(corporation_id):
    """ Takes a corporation ID and returns a dict with all available size links.

    :param corporation_id: A corporation ID from EVE.
    :return: A dict of size and urls.
    """

    return_dict = {x: get_image_server_link(corporation_id, 'corp', x) for x in CORPORATION_SIZES}

    return return_dict

def get_alliance_links(alliance_id):
    """ Takes a alliance ID and returns a dict with all available size links.

    :param alliance_id: A alliance ID from EVE.
    :return: A dict of size and urls.
    """

    return_dict = {x: get_image_server_link(alliance_id, 'alli', x) for x in ALLIANCES_SIZES}

    return return_dict

def get_faction_links(faction_id):
    """ Takes a faction ID and returns a dict with all available size links.

    :param faction_id: A faction ID from EVE.
    :return: A dict of size and urls.
    """

    return get_alliance_links(faction_id)

def get_type_links(type_id):
    """ Takes a type ID and returns a dict with all available size links.

    :param type_id: A type ID from EVE.
    :return: A dict of size and urls.
    """

    return_dict = {x: get_image_server_link(type_id, 'type', x) for x in TYPE_SIZES}

    return return_dict


def get_image_server_link(image_id, image_type, icon_size=128):
    """Takes an ID and type name and builds and image server URL.

    Known valid sizes:
    Character: 32, 64, 128, 256, 512, 1024
    Corporation: 32, 64, 128, 256
    Alliance: 32, 64, 128
    Faction: 32, 64, 128
    Types: 32, 64, 128, 256, 512

    :param image_id: ID to be used in the URL.
    :param image_type: Valid string options are: char, corp, alli, fac, type
    :param icon_size: See doc string for valid image sizes.
    :return: A full URL to the CCP image server.
    """

    base_image_server_url = os.environ.get('IMAGE_SERVER_URL', 'https://imageserver.eveonline.com/')

    if image_type == 'char':
        url_type = 'Character'
        url_format = 'jpg'

    elif image_type == 'corp':
        url_type = 'Corporation'
        url_format = 'png'

    elif image_type == 'alli':
        url_type = 'Alliance'
        url_format = 'png'

    elif image_type == 'fac':
        url_type = 'Alliance'
        url_format = 'png'

    else:
        url_type = 'Render'
        url_format = 'png'

    full_url = '{}{}/{}_{}.{}'.format(base_image_server_url, url_type, image_id, icon_size, url_format)

    return full_url
