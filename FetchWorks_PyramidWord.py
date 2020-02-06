import collections

def pyramidWord(word) -> bool:
  # If the word is empty
  if not word:
    return True
  # Count the number of occurences of each alphabet in word
  counter = collections.Counter(word)

  countList = [i for i in counter.values()]

  # operations on sets are efficient than on Lists
  countSet = set(countList)
  # If there are no duplicate counts occuring
  if len(countSet) == len(countList):
    # check if consecutive numbers are present in the list
    return sorted(countSet) == list(range(min(countSet), max(countSet)+1))

  else:
    return False



print(pyramidWord("Bbanannna"))
