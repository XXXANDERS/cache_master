import re

# str_ = re.sub(r'(?<=[.,;!?])(?=[^\s])', r' ', 'test string')

s = re.sub(r"\b([a-z])[^\s]*\1\b", r'AHAHAHA',
           'test  weof jwefij ewufjiwe fewijf heew hheeh weifjiw iejwf  wejfi  ifefi string')
print(s)
