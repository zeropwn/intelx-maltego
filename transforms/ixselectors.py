import intelxapi, webbrowser, pathlib, json
from maltego_trx.maltego import UIM_TYPES

from maltego_trx.transform import DiscoverableTransform

class ixselectors(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request, response):
        try:
            path = pathlib.Path(__file__).parent.absolute()
            sid = request.getProperty("SID")
            with open(f"{path}/../settings.json", 'r') as h:
                contents = h.read().strip('\n')
                settings = json.loads(contents)
                key = settings['APIKEY']
                h.close()
            intelx = intelxapi.intelx(key, ua='IX Maltego Transform/3')
            selectors = intelx.selectors(sid)

            for selector in selectors:
                entity = response.addEntity('intelx.selector', selector['selector'])
            
        except Exception as e:
            response.addUIMessage("Error: " + str(e), UIM_TYPES["partial"])