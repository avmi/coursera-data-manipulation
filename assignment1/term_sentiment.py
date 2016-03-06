import sys
import json

scores = {} #initialize an empty dictionary
new_scores = {}
new_scores_occurences = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def tweet_process(tweet):
    score = 0
    new_terms = []

    tweet_processed = tweet.lower()
    words = tweet_processed.split(' ')

    for word in words:
        if word in scores:
            score += scores[word]
        else:
            new_terms.append(word)

    for new_term in new_terms:
        if new_term in new_scores:
            new_scores[new_term] = score + new_scores[new_term]
            new_scores_occurences[new_term] = new_scores_occurences[new_term] + 1
        else:
            new_scores[new_term] = score
            new_scores_occurences[new_term] = 1

    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
        term, score = line.split("\t") #The file is tab-delimited
        scores[term] = int(score) # Convert the score to an integer

    for tweet_line in tweet_file:
        line_parsed = json.loads(tweet_line)

        if "text" in line_parsed.keys():
            tweet = line_parsed["text"]
            tweet.encode("UTF-8")

            tweet_process(tweet)

    for word in new_scores_occurences:
        scores[word] = float(float(new_scores[word]) / float(new_scores_occurences[word]))

    for word in scores:
        print word.replace(" ", "_"), scores[word]

if __name__ == '__main__':
    main()
