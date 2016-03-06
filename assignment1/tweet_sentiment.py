import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        score = 0;

        line_parsed = json.loads(line)

        if "text" in line_parsed.keys():
            tweet = line_parsed["text"].lower()
            tweet_words = tweet.split(' ')

            for word in tweet_words:
                if word in scores:
                    score += scores[word]

        print score

if __name__ == '__main__':
    main()
