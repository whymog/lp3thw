class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def gnos_a_em_gnis(self):
        for line in reversed(self.lyrics):
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

africaLyrics = ["I hear the drums echoing tonight",
               "But she hears only whispers of some quiet conversation",
               "She's coming in, 12:30 flight",
               "The moonlit wings reflect the stars that guide me toward salvation"]

africa = Song(africaLyrics)

africa.sing_me_a_song()

africa.gnos_a_em_gnis()
