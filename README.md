## Aspect Based Sentimental Analysis Codemix.

#### Data:
- We have collected twitter codemix data. After preprocessing the data, we are left with 3500 tweets with Aspects annotated.

#### Progress:
- We have divided our project into two parts - Aspect Identification and Sentimental Analysis.
- Working on Aspect Identification -- Ongoing work.

## Contents:
#### Parts of speech tagger for codemix:
- Parts of speech plays an important role in Aspect Identication.
- We have 1000 codemix tweets with annoatated parts-of-speech. We used this data for training.
- We have trained the data using different Machine learning methods and achieved the following accuracies:
  - Conditional Random Fields(CRF): 77.185%
  - Trigram + Bigram + Unigram: 68.172%
  - Hidden Markov Method(HMM): 18.014%
  
#### Aspect Identification:
- Till now, we applied CRF and SVM methods for identifying Aspects in a sentence.
- CRF: We have used nearly 65 features(considering window length of 5) and achieved an accuracy of 44.73%.
- SVM: We represented each word in the form of a vector and trained these vectors. We achieved an accuracy of ____%.

## Contributors:
[M R Abhishek](https://github.com/Abhishekmamidi123) and [K Vagdevi](https://github.com/vagdevik)
