from flask import Flask, json
import collections

app = Flask(__name__)

@app.route('/pyramidword/<word>', methods = ['GET', 'POST'])
def pyramidWord(word):
    # If the word is empty
    if not word:
        return json.dumps(True)

    # Count the number of occurences of each alphabet in word
    counter = collections.Counter(word)
    countList = [i for i in counter.values()]

    if len(countList) == 1 and countList[0] == 1:
        return json.dumps(True)
    elif len(countList) == 1:
        return json.dumps(False)
    else:
        # operations on sets are efficient than on Lists
        countSet = set(countList)

        # If there are no duplicate counts occuring
        if len(countSet) == len(countList):
            # check if consecutive numbers are present in the list
            return json.dumps(sorted(countSet) == list(range(min(countSet), max(countSet)+1)))
        else:
            return json.dumps(False)
