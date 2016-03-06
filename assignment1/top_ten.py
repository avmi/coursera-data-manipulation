import sys
import json
import re
from operator import itemgetter

hits = {}
counter = 0

def main():
    tweet_file = open(sys.argv[1])
    counter = 0

    for line in tweet_file:
        line_parsed = json.loads(line)

        if "entities" in line_parsed.keys():
            entities = line_parsed["entities"]

            if "hashtags" in entities.keys():
                hashtags = entities["hashtags"]

                if len(hashtags) > 0:
                    for hashtag in hashtags:
                        hashtag_value= hashtag["text"].encode("ascii", "ignore").lower()
                        hashtag_value = re.sub(r'[^a-zA-Z0-9]','', hashtag_value)
                        if hashtag_value in hits:
                            hits[hashtag_value] += 1
                        else:
                            hits[hashtag_value] = 1

    hits_sorted = sorted(hits.items(), key=itemgetter(1), reverse = True)

    for i in range(1, 11):
        print hits_sorted[i][0],hits_sorted[i][1]

if __name__ == '__main__':
    main()
