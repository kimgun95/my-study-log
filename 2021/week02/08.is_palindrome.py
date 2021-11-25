input = "abcba"


# palindrome은 '회문'이란 의미이며 회문이란 문자열을 똑바로 읽을 때와 거꾸로 읽을 때가 모두 같은 문자열을 의미
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


print(is_palindrome(input))