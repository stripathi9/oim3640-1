# http://www.pythonchallenge.com/pc/def/map.html


def trans(s):
    new_str = ""
    for letter in s:
        u = ord(letter)
        # if 65 <= u < 91 or 97 <= u < 121:
        if 'a' <= letter < 'y':
            letter = chr(u + 2)
        elif letter == 'y' or letter == 'z':
            letter = chr(u - 24)
        new_str += letter
    return new_str


def main():
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    print(trans(message))
    print(trans('map'))


if __name__ == "__main__":
    main()
