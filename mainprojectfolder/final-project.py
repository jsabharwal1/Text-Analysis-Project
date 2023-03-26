# importing required libraries for text analysis and downloading/updating packages within the libraries
import numpy as np
from mediawiki import MediaWiki  # to fetch data from wikipedia page
# to get list of strippable characters( special characters that do not add or take away from our analysis)
import string 
import nltk  # natural language toolkit library to conduct sentiment analysis
# sentiment analysis package
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
nltk.download('stopwords')  # stopwords from nltk library


# accesing wikipedia pages
wikipedia = MediaWiki()
biden = wikipedia.page('Joe Biden')
trump = wikipedia.page('Donald Trump')
putin = wikipedia.page('Vladimir Putin')



def str_to_list(text):
    """
    convert initial mediawiki file to list of words, clean words of any and all punctuation and whitespaces and converts them to lowercase letters
     
    """
    initial_list = []
    initial_list = text.split()
    strippables = string.punctuation + string.whitespace
    word_list = []
    for word in initial_list:
        word = word.strip(strippables)
        word = word.lower()
        word = word.replace('-', '')
        word = word.replace(chr(8121), '')
        word_list.append(word)
    return word_list


def list_to_hist(word_list):
    """
    maps words in given word list to their frequencies
    returns: dict

    """
    hist = {}
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return hist


def total_words(hist):
    """
    return total word count from the given histogram
    """
    return sum(hist.values())


def different_words(hist):
    """
    count of different words in the given histogram of words
    """
    return len(hist)


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-frequency pairs in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, stopwords are excluded from the list
    """
    t = []

    stopwords = nltk.corpus.stopwords.words("english")
    # remove any standalone strippable characters that were converted to whitespace during cleaning
    stopwords.append('')

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histogram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print, 10 by default 
    """
    most_common_words = most_common(hist)
    for freq, word in most_common_words[:num]:
        print(word, freq)

def common_words_between_texts(hist1, hist2, hist3, num =10, excluding_stopwords = True):
    """
    returns the 'n'most common words (10 by default) between the three histograms (map of word:frequency)
    excludes stopwords by defualt 
    """
    res = []
    stopwords = nltk.corpus.stopwords.words("english") 
    stopwords.append('')
    for word in hist1.keys():
        if excluding_stopwords:
            if word not in stopwords and word in hist2.keys() and word in hist3.keys():
                b= []
                a = hist2[word] + hist3[word]
                b = [a, word]
                res.append(b)
    res.sort(reverse=True)
    return res[:num]

def sentiment_analysis(text):
    """
    performs a sentiment analysis to see the emotional context of the text 
    """
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score




# sentiment_analysis()


# hist()

def main():
    word_list_biden = str_to_list(biden.content)
    word_list_trump = str_to_list(trump.content)
    word_list_putin = str_to_list(putin.content)

    # # hist
    # print()
    hist_biden = list_to_hist(word_list_biden)
    # print(f'The histogram of words in Joe Biden\'s wikipidea page is:\n \n', hist_biden)
    # print()
    hist_trump = list_to_hist(word_list_trump)
    # print(f'The histogram of words in Donald Trump\'s wikipidea page is:\n \n', hist_trump)
    # print()
    hist_putin = list_to_hist(word_list_putin)
    # print(f'The histogram of words in Vladimir Putin\'s wikipidea page is:\n \n', hist_putin)
    # print()

    # # # total words
    print(f'The total word count in Joe Biden\'s wikipedia article is {total_words(hist_biden)}.\n')
    print(f'The total word count in Donald Trump\'s wikipedia article is {total_words(hist_trump)}.\n')
    print(f'The total word count in Vladimir Putin\'s wikipedia article is {total_words(hist_putin)}.\n')
   
    # # different words
    print(f'Joe Biden\'s article has a total of {different_words(hist_biden)} different words. \n')
    print(f'Donald Trump\'s article has a total of {different_words(hist_trump)} different words. \n')
    print(f'Vladimir Putin\'s article has a total of {different_words(hist_putin)} different words. \n')

    # # most common top:num
    print('The top 10 common words in Joe Biden\'s article are:') 
    print_most_common(hist_biden)
    print()
    print('The top 10 common words in Donald Trump\'s article are:') 
    print_most_common(hist_trump)
    print()
    print('The top 10 common words in Vladimir Putin\'s article are:') 
    print_most_common(hist_putin)
    print()

    # common words between texts
    print(f'The ten most common words amongsth the three articles are:{common_words_between_texts(hist_biden, hist_trump, hist_putin)}\n')


    # # sentiment analysis

    print(f'The sentiment analysis score for Joe Biden\'s article:\n{sentiment_analysis(biden.content)}\n')
    print(f'The sentiment analysis score for Donald Trump\'s article:\n{sentiment_analysis(trump.content)}\n')
    print(f'The sentiment analysis score for Vladimir Putin\'s article:\n{sentiment_analysis(putin.content)}\n')

    

if __name__ == '__main__':
    main()
