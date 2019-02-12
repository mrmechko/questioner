import logging
from tripsweb.query import get_parse
import json


logging.basicConfig()
logger = logging.getLogger()
TRIPS_URL="http://trips.ihmc.us/parser/cgi/step"

def get_parse(sentence):
    cfg = json.load(open("data/parserconfig.json"))
    cfg['input'] = sentence
    parse, code = get_parse(TRIPS_URL, cfg, as_xml=False, verbose=False)
    return json.loads(parse)


