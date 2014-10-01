import sys
import os
OPENSHIFT_DATA_DIR = os.getenv("OPENSHIFT_DATA_DIR")
sys.path.insert(0, OPENSHIFT_DATA_DIR)
import updatevalue as uv
import random

A = ('[a](#f/alabama)', '[a](#f/arizona)', '[a](#f/army)', '[a]%s' % (uv.alma), '[a]%s' % (uv.uamn), '[a]%s' % (uv.acadia), '[a]%s' % (uv.stanselm))
B = ('[b](#f/b)', '[b]%s' % (uv.birminghamsouthern), '[b]%s' % (uv.brunel))
C = ('[c]%s' % (uv.cornellia), '[c](#f/colgate)', '[c](#f/chattanooga)')
D = ('[d](#f/dartmouth)', '[d]%s' % (uv.dean), '[d]%s' % (uv.osakakyoiku), '[d]%s' % (uv.dixiestate), '[d](#f/duke)')
E = ('[e]%s' % (uv.wisconsineauclaire), '[e](#f/easternmichigan)', '[e]%s' % (uv.emporiastate))
G = ('[g]%s' % (uv.kyoto), '[g](#f/georgia)', '[g]%s' % (uv.gettysburg), '[g]%s' % (uv.grovecity), '[g]%s' % (uv.gardencitycc), '[g]%s' % (uv.glenvillestate), '[g](#f/gramblingstate)')
H = ('[h]%s' % (uv.hamilton), '[h](#f/harvard)', '[h]%s' % (uv.hokkaido), '[h]%s' % (uv.hastings), '[h](#f/hawaii)')
I = ('[i](#f/illinois)', '[i]%s' % (uv.indianapolis), '[i](#f/idaho)')
K = ('[k]%s' % (uv.kurume), '[k]%s' % (uv.kanagawatech), '[k](#f/k)')
L = ('[l](#f/l)', '[l]%s' % (uv.wisconsinlacrosse), '[l]%s' % (uv.loyolachicago))
M = ('[m](#f/michigan)', '[m]%s' % (uv.mercyhurst), '[m](#f/murraystate)', '[m](#f/minnesota)', '[m]%s' % (uv.maranathabaptist), '[m](#f/maryland)', '[m]%s' % uv.southdakotamines)
N = ('[n](#f/nebraska)', '[n]%s' % (uv.northampton), '[n](#f/northwestern)')
O = ('[o](#f/oregon)', '[o]%s' % (uv.oxford), '[o]%s' % (uv.otemongakuin), '[o](#f/ohiostate)')
P = ('[p](#f/purdue)', '[p](#f/princeton)', '[p]%s' % (uv.kyushu), '[p]%s' % (uv.liupost))
R = ('[r]%s' % (uv.rochester), '[r](#f/rutgers)', '[r](#f/rice)', '[r]%s' % (uv.rosehulman))
S = ('[s]%s' % (uv.wisconsinstout), '[s](#f/syracuse)', '[s]%s' % (uv.sherbrooke), '[s]%s' % (uv.setsunan))
T = ('[t]%s' % (uv.trine), '[t](#f/tulane)', '[t]%s' % (uv.tarletonstate), '[t](#f/temple)')
U = ('[u]%s' % (uv.union), '[u]%s' % (uv.urbana), '[u]%s' % (uv.staffordshire))
V = ('[v](#f/v)', '[u]%s' % (uv.laurentian))
W = ('[w]%s' % (uv.waseda), '[w]%s' % (uv.wilkes), '[w](#f/washington)', '[w]%s' % (uv.wartburg), '[w](#f/wisconsin)', '[w]%s' % (uv.waynesburg))
X = ('[x](#f/x)', '[x]%s' % (uv.xavier))
Y = ('[y](#f/byu)', '[y](#f/yale)')


def flairgen(submission):
    """Convert letters in string to inline flair codes - regular mode.
    Input string -> converts as list -> output string
    Iterates through tuples of flair values sorted by letter, assigning
    the correct logo code to each respective letter in a submitted string."""
    submission = submission.upper()
    submission = submission.replace('. ', '.').replace('N\'', '_').replace('BU', '\\').replace('SC', '\b').replace(
        'OU', ']').replace('AF', '}').replace('TT', '[').replace('JU', '~').replace('GS', '`').replace(
        'BIG', '>').replace('SEC', "\a").replace('UK', "{").replace('! ', "!").replace('? ', "?")
    submission = list(submission)
    char = 0
    a, b, c, d, e, g, h, i, k, l, m = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    n, o, p, r, s, t, u, v, w, x, y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while char < len(submission):
        if submission[char] == 'A':
            submission[char] = A[a]
            a += 1
            if a == len(A):
                a = 0
        elif submission[char] == 'W':
            submission[char] = W[w]
            w += 1
            if w == len(W):
                w = 0
        elif submission[char] == 'C':
            submission[char] = C[c]
            c += 1
            if c == len(C):
                c = 0
        elif submission[char] == 'G':
            submission[char] = G[g]
            g += 1
            if g == len(G):
                g = 0
        elif submission[char] == 'M':
            submission[char] = M[m]
            m += 1
            if m == len(M):
                m = 0
        elif submission[char] == 'O':
            submission[char] = O[o]
            o += 1
            if o == len(O):
                o = 0
        elif submission[char] == 'P':
            submission[char] = P[p]
            p += 1
            if p == len(P):
                p = 0
        elif submission[char] == 'T':
            submission[char] = T[t]
            t += 1
            if t == len(T):
                t = 0
        elif submission[char] == 'S':
            submission[char] = S[s]
            s += 1
            if s == len(S):
                s = 0
        elif submission[char] == 'R':
            submission[char] = R[r]
            r += 1
            if r == len(R):
                r = 0
        elif submission[char] == 'I':
            submission[char] = I[i]
            i += 1
            if i == len(I):
                i = 0
        elif submission[char] == 'H':
            submission[char] = H[h]
            h += 1
            if h == len(H):
                h = 0
        elif submission[char] == 'E':
            submission[char] = E[e]
            e += 1
            if e == len(E):
                e = 0
        elif submission[char] == 'B':
            submission[char] = B[b]
            b += 1
            if b == len(B):
                b = 0
        elif submission[char] == 'K':
            submission[char] = K[k]
            k += 1
            if k == len(K):
                k = 0
        elif submission[char] == 'D':
            submission[char] = D[d]
            d += 1
            if d == len(D):
                d = 0
        elif submission[char] == 'L':
            submission[char] = L[l]
            l += 1
            if l == len(L):
                l = 0
        elif submission[char] == 'N':
            submission[char] = N[n]
            n += 1
            if n == len(N):
                n = 0
        elif submission[char] == 'U':
            submission[char] = U[u]
            u += 1
            if u == len(U):
                u = 0
        elif submission[char] == 'V':
            submission[char] = V[v]
            v += 1
            if v == len(V):
                v = 0
        elif submission[char] == 'X':
            submission[char] = X[x]
            x += 1
            if x == len(X):
                x = 0
        elif submission[char] == 'Y':
            submission[char] = Y[y]
            y += 1
            if y == len(Y):
                y = 0
        elif submission[char] == 'F':
            submission[char] = '[f](#f/f)'
        elif submission[char] == 'J':
            submission[char] = '[j](#f/j)'
        elif submission[char] == 'Q':
            submission[char] = '[q](#f/q)'
        elif submission[char] == 'Z':
            submission[char] = '[z](#f/z)'
        elif submission[char] == '.':
            submission[char] = '.\n\n'
        elif submission[char] == '?':
            submission[char] = '?^?\n\n'
        elif submission[char] == '!':
            submission[char] = '!^!\n\n'
        elif submission[char] == ' ':
            submission[char] = ' -- '
        elif submission[char] == '\\':
            submission[char] = '[bu](#f/baylor)'
        elif submission[char] == '\b':
            submission[char] = '[sc](#f/usc)'
        elif submission[char] == '}':
            submission[char] = '[af](#f/airforce)'
        elif submission[char] == ']':
            submission[char] = '[ou](#f/oklahoma)'
        elif submission[char] == '[':
            submission[char] = '[tt](#f/texastech)'
        elif submission[char] == '~':
            submission[char] = '[ju](#f/jacksonville)'
        elif submission[char] == '`':
            submission[char] = '[gs](#f/georgiasouthern)'
        elif submission[char] == '>':
            submission[char] = '[Big Ten](#l/bigten)'
        elif submission[char] == '\a':
            submission[char] = '[sec](#l/sec)'
        elif submission[char] == '{':
            submission[char] = '[uk](#f/kentucky)'
        elif submission[char] == '_':
            submission[char] = '[n](#f/navy)'
        else:
            True
        char += 1
    return ''.join(submission)


def flairgen_safe(submission):
    """Convert letters in string to inline flair codes - safe mode.
    Input string -> converts as list -> output string
    !!Safe mode uses fewer, safer flairs and chooses codes randomly by letter.
    !!Not recommeded unless regular mode is out of date"""
    submission = submission.replace('. ', '.').replace('! ', "!").replace('? ', "?")
    submission = list(submission.upper())
    s = 0
    while s < len(submission):
        if submission[s] == 'A':
            submission[s] = random.choice(('[a](#f/a)', '[a](#f/arizona)', '[a](#f/alabama)'))
        elif submission[s] == 'W':
            submission[s] = random.choice(('[w](#f/w)', '[w](#f/washington)'))
        elif submission[s] == 'C':
            submission[s] = random.choice(('[c](#f/c)', '[c](#f/colgate)'))
        elif submission[s] == 'G':
            submission[s] = random.choice(('[g](#f/g)', '[g](#f/georgia)'))
        elif submission[s] == 'M':
            submission[s] = random.choice(('[m](#f/michigan)', '[m](#f/m)', '[m](#f/minnesota)'))
        elif submission[s] == 'O':
            submission[s] = random.choice(('[o](#f/ohiostate)', '[o](#f/oregon)'))
        elif submission[s] == 'P':
            submission[s] = random.choice(('[p](#f/p)', '[p](#f/princeton)'))
        elif submission[s] == 'T':
            submission[s] = random.choice(('[t](#f/tulane)', '[t](#f/temple)'))
        elif submission[s] == 'S':
            submission[s] = random.choice(('[s](#f/s)', '[s](#f/syracuse)'))
        elif submission[s] == 'R':
            submission[s] = random.choice(('[r](#f/rutgers)', '[r](#f/r)'))
        elif submission[s] == 'I':
            submission[s] = random.choice(('[i](#f/i)', '[i](#f/idaho)'))
        elif submission[s] == 'H':
            submission[s] = random.choice(('[h](#f/harvard)', '[h](#f/hawaii)'))
        elif submission[s] == 'E':
            submission[s] = '[e](#f/e)'
        elif submission[s] == 'F':
            submission[s] = '[f](#f/f)'
        elif submission[s] == 'J':
            submission[s] = '[j](#f/j)'
        elif submission[s] == 'B':
            submission[s] = '[b](#f/b)'
        elif submission[s] == 'K':
            submission[s] = '[k](#f/k)'
        elif submission[s] == 'D':
            submission[s] = random.choice(('[d](#f/d)', '[d](#f/duke)'))
        elif submission[s] == 'L':
            submission[s] = '[l](#f/l)'
        elif submission[s] == 'N':
            submission[s] = random.choice(('[n](#f/nebraska)', '[n](#f/n)', '[n](#f/navy)'))
        elif submission[s] == 'Q':
            submission[s] = '[q](#f/q)'
        elif submission[s] == 'U':
            submission[s] = '[u](#f/u)'
        elif submission[s] == 'V':
            submission[s] = '[v](#f/v)'
        elif submission[s] == 'X':
            submission[s] = '[x](#f/x)'
        elif submission[s] == 'Y':
            submission[s] = '[y](#f/byu)'
        elif submission[s] == 'Z':
            submission[s] = '[z](#f/z)'
        elif submission[s] == '.':
            submission[s] = '.\n\n'
        elif submission[s] == '?':
            submission[s] = '?^?'
        elif submission[s] == '!':
            submission[s] = '!^!'
        elif submission[s] == ' ':
            submission[s] = ' -- '
        else:
            True
        s += 1
    return ''.join(submission)
