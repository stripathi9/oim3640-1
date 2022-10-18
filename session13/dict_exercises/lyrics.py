def histogram(word_list):
    """convert a word list to a dictionary mapping word to frequency"""
    d = {}
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d


def print_hist(h):
    """print items in a dictionary"""
    for k in sorted(h.keys()):
        print(k, h[k])


def print_lyrics_hist():
    """print word frequency in song lyrics and output result to a text file"""
    f = open('data/hey_jude.txt')
    # lines = f.readlines()
    # print(lines)
    # for word in line.split():
    #     print(word)
    lyrics = f.read().lower()
    # print(lyrics)
    lyrics = (
        lyrics.replace(',', ' ')
        .replace('-', ' ')
        .replace('(', ' ')
        .replace(')', ' ')
        .replace('!', ' ')
    )
    word_list = lyrics.split()

    h = histogram(word_list)
    print_hist(h)

    # with open('data/result.txt', 'w') as f:
    #     for word, freq in h.items():
    #         f.write(f'{word}: {freq}\n')


def main():
    print_lyrics_hist()


if __name__ == "__main__":
    main()
