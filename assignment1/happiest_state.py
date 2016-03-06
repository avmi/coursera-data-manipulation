import sys
import json
from operator import itemgetter

scores = {} #initialize an empty dictionary

happy_states = {}
states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def lines(fp):
    print str(len(fp.readlines()))

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
        term, score = line.split("\t") #The file is tab-delimited
        scores[term] = int(score) # Convert the score to an integer

    for line in tweet_file:
        line_parsed = json.loads(line)
        score=0

        if "place" in line_parsed.keys():
            place = line_parsed["place"]

            if place != None:
                if place["country_code"] == "US":
                    fullname = place["full_name"]
                    city, state = fullname.split(",")
                    state = state.strip()

                    if state in states:
                        if "text" in line_parsed.keys():
                            words = line_parsed["text"].lower().split(' ')
                            for word in words:
                                if word in scores:
                                    score += scores[word]

                        if state in happy_states:
                            if score >= happy_states[state]:
                                happy_states[state] = score
                        else:
                            happy_states[state] = score

    sorted_happy = sorted(happy_states.items(), key = itemgetter(1), reverse = True)
    happiest = sorted_happy[0]

    print happiest[0]

if __name__ == '__main__':
    main()
