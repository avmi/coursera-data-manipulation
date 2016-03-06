import sys
import json
import re

hits = {}
counter = 0

def main():
    tweet_file = open(sys.argv[1])
    count = 0

    for line in tweet_file:
        line_parsed = json.loads(line)

        if "text" in line_parsed.keys():
            tweet = line_parsed["text"]

            tweet_processed = tweet.lower()
            words = tweet_processed.split(' ')

            for word in words:
                processed_word = word.encode("ascii", "ignore")

                if processed_word.startswith('@') or processed_word.startswith('http://') or processed_word.startswith('https://'):
                    processed_word = ''
                else:
                    processed_word = re.sub(r'[^a-zA-Z0-9]','', processed_word)

                if processed_word != '':
                    count += 1

                    if processed_word in hits:
                        hits[processed_word] += 1
                    else:
                        hits[processed_word] = 1

    for term in hits:
        score = float(hits[term]) / count
        print '%s %f' % (term, score)

if __name__ == '__main__':
    main()
