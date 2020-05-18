#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text, 0, len(text) - 1)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    begin = 0
    end = len(text) - 1

    while begin < end:
        while text[begin].isalpha() is False:
            begin += 1

        while text[end].isalpha() is False:
            end -= 1

        if text[begin].lower() != text[end].lower():
            return False

        begin += 1
        end -= 1

    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if left >= right:
        return True

    if len(text) == 0 or len(text) == 1:
        return True

    if text[left].isalpha() is False:
        return is_palindrome_recursive(text, left=left+1, right=right)

    if text[right].isalpha() is False:
        return is_palindrome_recursive(text, left=left, right=right-1)

    if text[left].lower() != text[right].lower():
        return False

    #advance positions
    if text[left].lower() == text[right].lower() and left < right:
        return is_palindrome_recursive(text, left=left+1, right=right-1)
    elif left >= right:
        return True
    else:
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
