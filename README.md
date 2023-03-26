# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

1. Project Overview (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?
Through this project I imported several libraries, including numpy, fuzz, MediaWiki, nltk, and SentimentIntensityAnalyzer. I used the function str_to_list to convert the MediaWiki file to a list of words, then clean the words of any punctuation and whitespaces, eventually converting them to lowercase letters. Through this exercise I wanted to learn how I can utilize different python libraries and use an external data source to analyze content, which is exactly what I did. 

2. Implementation (~1-2 paragraphs + screenshots)

This code performs text analysis on the wikipedia pages of Joe Biden, Donald Trump, and Vladimir Putin. I first wanted to clean all the text that I retrieved from the wiki pages, hence used several functions like str_to_list and list_to_hist to clean the pages of all punctuation and whitespaces, etc. I then used nltk to remove any stopwords, followed by finding the common words between the pages. I then went ahead with conducting a sentiment analysis and used the SentimentIntensityAnalyzer to get the scores. Then using the str_to_list and the list_to_hist functions I printed out the output. 

3. Results (~2-3 paragraphs + figures/examples)

For Joe Biden's article, the sentiment analysis score shows a slightly positive sentiment as indicated by the compound score of 0.9991, which is close to 1. The ‘pos’ score for Biden was higher than the ‘neg’ score, whereas it is the opposite for Trump, suggesting that overall the wikipedia page has a more positive view on Joe Biden and a more negative stand on Donald Trump. With respect to Putin, the ‘neg’ and ‘pos’ scores suggest that there is an equal mix of positive and negative sentiment, however the compound score of -0.9947 confirms the negative sentiment towards Vladimir Putin. 
There was nothing surprising about the top 10 most common words in each person’s wiki page. Some of the important words in Trump’s page -  ‘2020’, ‘election’, ‘presidential’ and ‘campaign’. This could refer to his 2020 election scandal, and the fact that he is running for the presidential campaign again. Some of the important words from Putin’s page - ‘war’, ‘ukraine’ and ‘military’. This makes sense given he has largely been in the news for the last one year because of the fact that he used his military to invade ukraine. There was nothing out of the blue for Biden’s wiki page. When I conducted an analysis of the top 10 common words amongst all 3 wiki pages, the interesting thing I found was that the word ‘biden’ was not among them, while ‘trump’ and ‘putin’ were the two most common words. These results could suggest that generally speaking ‘trump’ and ‘putin’ are more relevant in the world wide web currently as compared to ‘biden’. 

4. Reflection (~1-2 paragraphs)

Ideally I would have liked to create this project using the twitter api, since it would have been more interesting and then conduct a sentiment analysis on people’s perceptions towards these three banks. I had a ‘aha’ moment when I completed the first part of the sentiment analysis. I especially found it interesting to conduct the ‘common words within text’ function, and I believe that if applied to other data sources such as yahoo finance api then you can track different stock indexes worldwide, and that would be a project I would love to do. Prior to starting this project I was quite worried about how I’ll do it, but I actually really enjoyed it and it felt fulfilling when I completed all the code. I think ChatGPT gave me inspiration by giving ideas on different sentiment analysis to conduct. I just wish I would have gotten an introduction to how some of these libraries function, that would have been really helpful for sure. 

