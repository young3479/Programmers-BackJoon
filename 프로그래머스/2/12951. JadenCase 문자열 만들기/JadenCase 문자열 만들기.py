def solution(s):
    return ' '.join([word.capitalize() if word else '' for word in s.split(' ')])