from web import *
from CetatenieJustRoParser import *
from PublishingsDownloader import *

# Retrieve the html content
html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_URL)

# Retrieve publishings
publishings = get_publishings(html_content)

# Download publishings
download_publishings_list(publishings[:3], verbose=True)
