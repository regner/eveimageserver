# eveimageserver
[![Build Status](https://travis-ci.org/Regner/eveimageserver.svg?branch=master)](https://travis-ci.org/Regner/eveimageserver)
[![Coverage Status](https://coveralls.io/repos/Regner/eveimageserver/badge.svg?branch=master&service=github)](https://coveralls.io/github/Regner/eveimageserver?branch=master)
[![PyPI version](https://badge.fury.io/py/eveimageserver.svg)](http://badge.fury.io/py/eveimageserver)

## Using
```python
import eveimageserver

# Get a 256x256 pixel image server link for a character
eveimageserver.get_image_server_link(123456, 'char', 256)

# Get a dictionary of links for all alliance images
eveimageserver.get_alliance_links(123456)
```

## Environment Variables
* __IMAGE_SERVER_URL:__ Defaults to 'https://image.eveonline.com/'. If you set
your own environment variable for this be sure to include the trailing slash.
