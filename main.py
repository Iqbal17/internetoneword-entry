"""The Internet in One Word - entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output/entry.txt): the single word that describes the whole internet for
the make.fun bounty "The Internet in One Word"
(u-ronigrv-the-internet-in-one-word-e388f33b, $10, top three share).

Gate (sealed scorer, from the kit's competition.yaml): /output/entry.txt
must be UTF-8 text of 1 to 30 characters, not only whitespace. The brief
adds the real constraint: the entry is that word and nothing else - no
phrase, no punctuation garnish, no explanation.

Chosen word: "doomscrolling" (13 characters, exactly one word).

Decision record
---------------
Candidates weighed against the judge's criteria, in the judge's own
order (1: a single word describing the WHOLE internet; 2: earns a laugh
with no explanation; 3: true of the internet as a whole, not one app or
one mood; 4: surprising, not the first obvious reach; 5: lands in one
beat - correctly spelled, instantly readable, short):

A. "slop" - The fashionable verdict on the AI-flooded web, and genuinely
   funny. But it names the CONTENT, not the internet: a library of slop
   is still not the whole machine, and by November 2026 it is the first
   word half the field reaches for, so it fails criterion 4 outright.
   Rejected: partial truth, zero surprise.
B. "buffering" - Lands in one beat and everyone has suffered it. But it
   describes a slow connection - a mood, a malfunction - not the
   internet itself; on a fast connection the word says nothing, while
   the internet is still entirely itself. Rejected on criterion 3.
C. "brainrot" - Funny and very current, but it names what the internet
   does to one generation's vocabulary; it is slang about an effect,
   already a crowded pick, and it dates fast. Rejected: narrower than
   the whole, and not surprising anymore.
D. "unsolicited" - A real twist (nobody asked for any of this) and it
   covers ads, opinions and group chats at once. It loses on the laugh:
   it reads as a complaint first and a joke second, and it needs half a
   beat of thought before it lands. Rejected on criteria 2 and 5.
E. "procrastination" - True of nearly every session ever opened, and
   quietly funny. But it describes the USER's failure, not the internet;
   the same word fits a snooze button. It is also 15 characters of
   Latinate flatness next to the winner's vivid verb. Rejected on 3.
F. "doomscrolling" - CHOSEN. It is the one activity the whole internet
   converges on: news, feeds, videos and arguments all end in the same
   thumb, the same hour gone, the same informed-and-worse feeling. It
   describes the whole (criterion 1: every app is a delivery vehicle
   for it), it is an accusation the reader is committing WHILE reading
   the entry, which is where the laugh lives (2), it is true on any
   connection, any app, any country (3), it is a behaviour rather than
   the field's default insult or slang (4), and it is one correctly
   spelled, instantly parsed word of 13 characters (5).

Writing passes (genuine revisions):
- Pass 1 wrote the word as a bare constant with a shortlist in the
  docstring and verified the raw output: "doomscrolling" plus newline,
  14 characters total, one word.
- Pass 2 (this file) expanded the decision record to the full candidate
  set with per-criterion rejections, and added a hard gate guard: the
  program refuses to write anything that is not exactly one word of
  1-30 characters, so a future edit can never silently ship an invalid
  entry. Output is byte-identical to pass 1.
"""

import os

WORD = "doomscrolling"

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 30


def checked_word() -> str:
    """Return WORD only if it satisfies the gate exactly.

    The gate counts the file's characters; the file holds the word plus
    a trailing newline, so the word itself must leave room for it and
    must be a single whitespace-free token.
    """
    if WORD != WORD.strip() or len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not (GATE_MIN_CHARS <= len(WORD) + 1 <= GATE_MAX_CHARS):
        raise ValueError("entry would fall outside the 1-30 character gate")
    return WORD


def main() -> None:
    word = checked_word()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(word + "\n")


if __name__ == "__main__":
    main()
