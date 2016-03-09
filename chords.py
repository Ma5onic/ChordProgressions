#!/usr/bin/env python3

import networkx as nx
import sys

final_chords = []

def build_chord_list(G, root, chord_list):
    global final_chords
    neighbors = G.neighbors(root)
    if not neighbors:
        if len(chord_list) > 1:
            final_chords.append(list(chord_list))
    else:
        for n in G.neighbors(root):
            new_chord_list = list(chord_list)
            build_chord_list(G, n, new_chord_list)
            new_chord_list.append(n)
            build_chord_list(G, n, new_chord_list)

def remove_duplicate_chords():
    global final_chords
    chord_set = set(tuple(x) for x in final_chords)
    final_chords = [list(x) for x in chord_set]

def sort_by_length():
    global final_chords
    final_chords = sorted(final_chords, key=len)

def print_progression(chord_progression):
    output = ""
    for chord in chord_progression[:-1]:
        output += chord + ", "
    output += chord_progression[-1]
    print(output)

def main(args):
    global final_chords

    G=nx.DiGraph()
    G.add_edges_from([
        ("I", "iii"),
        ("iii", "vi"),
        ("vi", "ii"),
        ("vi", "IV"),
        ("ii", "vii"),
        ("ii", "V"),
        ("IV", "vii"),
        ("IV", "V")])

    chord_list = ["I"]
    build_chord_list(G, "I", chord_list)
    remove_duplicate_chords()
    sort_by_length()

    for c in final_chords:
        print_progression(c)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
