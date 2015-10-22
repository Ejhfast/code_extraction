# How to save gensim LDA topics output to csv along with the scores?
import pandas
mixture = [dict(lda1[x]) for x in corpus1]
pandas.DataFrame(mixture).to_csv("output.csv")
