import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from BasicResponse import BasicResponse


class ChatProcessor(BasicResponse):

    def __init__(self, knowledge):
        self.sentence_token = nltk.sent_tokenize(knowledge.lower())
        BasicResponse.__init__(self)

    @staticmethod
    def __stem_tokens(tokens):
        return [PorterStemmer().stem(token) for token in tokens]

    def stem_sentence(self, text):
        return self.__stem_tokens(nltk.word_tokenize(text.lower().translate(self._get_punct())))

    @staticmethod
    def __lemmatize_tokens(tokens):
        return [nltk.stem.WordNetLemmatizer().lemmatize(token) for token in tokens]

    def lemmatize_sentence(self, text):
        return self.__lemmatize_tokens(nltk.word_tokenize(text.lower().translate(self._get_punct())))

    def bot_answer(self, res_sent):
        conf_ans = "I am sorry! I don't understand you"
        if len(res_sent.strip()) == 0:
            return conf_ans
        self.sentence_token.append(res_sent)
        tfidf_vec = TfidfVectorizer(tokenizer=self.lemmatize_sentence, stop_words='english')
        tfidf = tfidf_vec.fit_transform(self.sentence_token)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if (req_tfidf == 0):
            return conf_ans
        else:
            answer = self.sentence_token[idx]
            self.sentence_token.remove(res_sent)
            return str(answer).capitalize()
