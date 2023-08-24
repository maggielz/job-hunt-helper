class TextSearch():
    # returns true if txt contains one  of the given words
    def text_contains(txt, words):
        for word in words:
            if word in txt:
                return True
        return False