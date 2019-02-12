import logging, os
from tripsweb import query
import json

from TripsIM import matcher
from pprint import pprint

logging.basicConfig()
logger = logging.getLogger()
TRIPS_URL="http://trips.ihmc.us/parser/cgi/step"

def get_parse(sentence):
    cfg = json.load(open("data/parserconfig.json"))
    cfg['input'] = sentence
    parse, code = query.get_parse(TRIPS_URL, cfg, as_xml=False, verbose=False)
    return json.loads(parse)

def load_rulesets(directory):
    rulesets = {}
    # use os.walk here instead for better organization of rule sets
    for filename in os.listdir(directory):
        if filename.endswith(".im"):
            rulesets[filename[0:-3]] = matcher.parse_rule_set(os.path.join(directory, filename))
    return rulesets

def example(sentence, rulesets):
    sentence = get_parse(sentence)
    pprint(sentence)
    s = matcher.load_list_set(sentence)
    results = {}
    for name, ruleset in rulesets.items():
        logger.info("matching {name}".format(name=name))
        results["name"] = matcher.grade_rules(ruleset, s)
    return sentence, results

def main():
    rulesets = load_rulesets("data/rulesets")
    results = example("Shall I buy a computer?", rulesets)
    return results

if __name__ == "__main__":
    main()
