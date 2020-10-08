# readability_python
Readability CS50, but in Python3.

This program is using Coleman-Liau index and outputs an approximate to the U.S. grade level thought necessary to comprehend the text. 

Formula: index = 0.0588 * L - 0.296 * S - 15.8
Where
- L is the average number of letters per 100 words and S is the average number of sentences per 100 words. 
- S is the sum of Sentences and Words times 100.


Read more Coleman-Liau:
https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
