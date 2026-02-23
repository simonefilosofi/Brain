#!/usr/bin/env python3
"""
brain image — renders the BRAIN title + coloured ASCII brain art in the terminal.
Usage: python brain_image.py   OR wire render() into your 'brain image' CLI command.
"""

import sys

# ── ANSI colour codes ──────────────────────────────────────────────────────────
R   = "\033[0m"
P1  = "\033[38;5;218m"   # blush highlight
P2  = "\033[38;5;211m"   # mid pink
P3  = "\033[38;5;204m"   # deep rose
RD  = "\033[38;5;160m"   # red sulci
ST  = "\033[38;5;174m"   # brain-stem
VS  = "\033[38;5;167m"   # vessels
DM  = "\033[2m"
BD  = "\033[1m"
NAV = P2                 # title matches brain outer cortex pink

def col(c, s): return c + s + R


# ── BRAIN title in block/pixel font (navy, matching screenshot style) ──────────

TITLE_B = [
    "██████╗ ",
    "██╔══██╗",
    "██████╔╝",
    "██╔══██╗",
    "██████╔╝",
    "╚═════╝ ",
]
TITLE_R = [
    "██████╗ ",
    "██╔══██╗",
    "██████╔╝",
    "██╔══██╗",
    "██║  ██║",
    "╚═╝  ╚═╝",
]
TITLE_A = [
    " █████╗ ",
    "██╔══██╗",
    "███████║",
    "██╔══██║",
    "██║  ██║",
    "╚═╝  ╚═╝",
]
TITLE_I = [
    "██╗",
    "██║",
    "██║",
    "██║",
    "██║",
    "╚═╝",
]
TITLE_N = [
    "███╗   ██╗",
    "████╗  ██║",
    "██╔██╗ ██║",
    "██║╚██╗██║",
    "██║ ╚████║",
    "╚═╝  ╚═══╝",
]

TITLE_LETTERS = [TITLE_B, TITLE_R, TITLE_A, TITLE_I, TITLE_N]


def render_title():
    print()
    for row in range(6):
        line = "   ".join(letter[row] for letter in TITLE_LETTERS)
        print(f"      {BD}{NAV}{line}{R}")
    print()


# ── Brain ASCII art ────────────────────────────────────────────────────────────

def render_brain():
    brain_top = (
        col(P2, " ,cCCCC(") + col(P3, "oOOOOOOOo") +
        col(RD, " }|{ ") + col(P3, "oOOOOOOOo") + col(P2, ")CCCC,   ")
    )

    lines = [
        # crown
        "              " + col(P3, "  .--=cccc=--.  ") + col(RD, " | ") + col(P3, "  .--=cccc=--.   "),
        "          " + brain_top,
        "        " + col(P2,"cCC'") + col(RD," /~\\ ") + col(P1,"oOOOo") + col(RD,"  /|\\ ") + col(P1,"oOOOo") + col(RD," /~\\ ") + col(P2,"'CC,      "),
        "       " + col(P2,"cCC") + col(P3," _(_(") + col(RD,"|") + col(P1,"OOOOO") + col(RD,"|") + col(P2,"  |  ") + col(RD,"|") + col(P1,"OOOOO") + col(RD,"|") + col(P3,")_)_ ") + col(P2,"CC,     "),
        "      " + col(P2,"cCC") + col(P3," _(_(_(") + col(RD,"\\") + col(P2,"~~~~~") + col(RD,"/") + col(P2,"___") + col(RD,"\\") + col(P2,"~~~~~") + col(RD,"/") + col(P3,")_)_)_ ") + col(P2,"CC,    "),
        # upper lobes
        "     " + col(P1,",CC ") + col(P2,"_/~~\\_ ") + col(P3,"cCCC'  ") + col(RD," {=} ") + col(P3,"  'CCCc") + col(P2," _/~~\\_ ") + col(P1,"CC,   "),
        "    " + col(P2,",CC ") + col(P3,"cC'") + col(RD,"/~~\\") + col(P1," OOOO ") + col(RD,"||") + col(P2," [=] ") + col(RD,"||") + col(P1," OOOO ") + col(RD,"/~~\\") + col(P3,"'Cc") + col(P2," CC,  "),
        "   " + col(P2,",CC  ") + col(P3,"cC") + col(RD,"|") + col(P1,"OOOOOO") + col(RD,"|") + col(P2,"  |||  ") + col(RD,"|") + col(P1,"OOOOOO") + col(RD,"|") + col(P3,"Cc") + col(P2,"  CC,  "),
        "   " + col(P2,"CC  ") + col(P3,"C'") + col(P1," ~OOO~") + col(RD,"/") + col(P3,"cc") + col(RD,"\\") + col(P2,"_|_") + col(RD,"/") + col(P3,"cc") + col(RD,"\\") + col(P1,"~OOO~ ") + col(P3,"'C") + col(P2,"  CC  "),
        "  " + col(P2,",CC ") + col(P3,"C  ") + col(P1,"OOOO") + col(RD," \\~~/ ") + col(P3," c ") + col(RD," \\~~/ ") + col(P1,"OOOO") + col(P3,"  C") + col(P2,"  CC,  "),
        "  " + col(P2,"CC  ") + col(P1,"  ~OO~") + col(RD,"  ||  ") + col(P3,"cCCc") + col(RD,"  ||  ") + col(P1,"~OO~  ") + col(P2,"  CC  "),
        "  " + col(P2,",CC  ") + col(P1," OO") + col(RD," /~~\\ ") + col(P3,"cCCCCc") + col(RD," /~~\\ ") + col(P1,"OO ") + col(P2,"  CC, "),
        "  " + col(P2,"CC   ") + col(P3,"cC") + col(RD,"|") + col(P1,"OO") + col(P3,"Cc") + col(RD,"\\  /") + col(P2," === ") + col(RD,"\\  /") + col(P3,"cC") + col(P1,"OO") + col(RD,"|") + col(P3,"Cc") + col(P2,"   CC "),
        "  " + col(P2,"CC   ") + col(P3,"C") + col(P1," OOO") + col(RD," \\/ ") + col(P3,"CC") + col(P2,"  |  ") + col(P3,"CC") + col(RD," \\/ ") + col(P1,"OOO ") + col(P3,"C") + col(P2,"   CC "),
        "  " + col(P2,"CC   ") + col(P3,"C") + col(P1," OO ") + col(P3,"Cc") + col(RD," /\\ ") + col(P2," | ") + col(RD," /\\ ") + col(P3,"cC") + col(P1," OO ") + col(P3,"C") + col(P2,"   CC "),
        "  " + col(P2," CC  ") + col(P3,"C") + col(P1," OO ") + col(RD,"|  |") + col(P3,"Cc ") + col(P2,"   ") + col(P3," cC") + col(RD,"|  |") + col(P1," OO ") + col(P3,"C") + col(P2,"  CC  "),
        # lower lobes
        "   " + col(P2,",CC ") + col(P3,"Cc") + col(P1," OOO") + col(RD," \\__/ ") + col(P3,"cCCc") + col(RD," \\__/ ") + col(P1,"OOO ") + col(P3,"cC") + col(P2," CC,  "),
        "   " + col(P2,"CC  ") + col(P3,"Cc") + col(P1,"OOOO") + col(RD,"  {}  ") + col(P3,"cCCCc") + col(RD,"  {}  ") + col(P1,"OOOO") + col(P3,"cC") + col(P2,"  CC   "),
        "   " + col(P2,"'CC") + col(P3,"C") + col(P1,"OOOOO") + col(RD," \\  / ") + col(P3,"CCCCC") + col(RD," \\  / ") + col(P1,"OOOOO") + col(P3,"C") + col(P2,"CC'   "),
        "    " + col(P2,"'C") + col(P3,"CCOO") + col(P1,"OOO") + col(RD,"  \\/  ") + col(P3,"cCCc") + col(RD,"  \\/  ") + col(P1,"OOO") + col(P3,"OOCC") + col(P2,"C'    "),
        "     " + col(P2,"'C") + col(P3,"CCCCC") + col(RD,"oooooo") + col(P3,"CCCCC") + col(RD,"oooooo") + col(P3,"CCCCC") + col(P2,"C'     "),
        "      " + col(P2,"'CCCCC") + col(P3,"CCCC") + col(RD,"oooo") + col(P3,"CCCC") + col(RD,"oooo") + col(P3,"CCCC") + col(P2,"CCCCC'      "),
        "        " + col(P2,"''CCCC") + col(P3,"CCCCCCCCCCCCC") + col(P2,"CCCC''        "),
        "            " + col(P2,"''CCCCCCCCCCCCCC''            "),
        # brain-stem
        "                 " + col(ST,"  [===|===]  "),
        "                  " + col(ST," (  stem  ) "),
        "                   " + col(VS," |") + col(ST,"~~~~~~~") + col(VS,"| "),
        "                    " + col(VS,"  \\") + col(ST,"~~~~~") + col(VS,"/  "),
        "                     " + col(VS,"   ~") + col(ST,"~~~") + col(VS,"~   "),
        # vessels
        "                  " + col(VS," /") + col(RD,"~") + col(VS,"\\ ") + col(ST,"|") + col(VS," /") + col(RD,"~") + col(VS,"\\  "),
        "                 " + col(VS,"/  ") + col(RD,"v") + col(VS,"  \\") + col(ST,"||") + col(VS,"/  ") + col(RD,"v") + col(VS,"  \\ "),
    ]

    for line in lines:
        print(line)

    print()
    print(DM + P3 + " " * 22 + BD + P3 + "simonefilosofi" + R)
    print()


# ── Combined render ────────────────────────────────────────────────────────────

def render():
    render_title()
    render_brain()


# ── CLI wiring ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "image":
        render()
    else:
        print(f"Unknown command: {' '.join(args)}")
        sys.exit(1)