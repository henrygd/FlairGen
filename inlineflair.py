import random
import updatevalue as uv

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


def flairgen(texty):
    """Convert letters in string to inline flair codes - regular mode.
    Input string -> converts as list -> output string
    Iterates through tuples of flair values sorted by letter, assigning
    the correct logo code to each respective letter in a submitted string."""
    texty = texty.upper()
    texty = texty.replace('. ', '.').replace('N\'', '_').replace('BU', '\\').replace('SC', '\b').replace('OU', ']').replace('AF', '}').replace(
        'TT', '[').replace('JU', '~').replace('GS', '`').replace('BIG', '>').replace('SEC', "\a").replace('UK', "{").replace(
        '! ', "!").replace('? ', "?")
    texty = list(texty)
    char = 0
    a, b, c, d, e, g, h, i, k, l, m = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    n, o, p, r, s, t, u, v, w, x, y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while char < len(texty):
        if texty[char] == 'A':
            texty[char] = A[a]
            a += 1
            if a == len(A):
                a = 0
        elif texty[char] == 'W':
            texty[char] = W[w]
            w += 1
            if w == len(W):
                w = 0
        elif texty[char] == 'C':
            texty[char] = C[c]
            c += 1
            if c == len(C):
                c = 0
        elif texty[char] == 'G':
            texty[char] = G[g]
            g += 1
            if g == len(G):
                g = 0
        elif texty[char] == 'M':
            texty[char] = M[m]
            m += 1
            if m == len(M):
                m = 0
        elif texty[char] == 'O':
            texty[char] = O[o]
            o += 1
            if o == len(O):
                o = 0
        elif texty[char] == 'P':
            texty[char] = P[p]
            p += 1
            if p == len(P):
                p = 0
        elif texty[char] == 'T':
            texty[char] = T[t]
            t += 1
            if t == len(T):
                t = 0
        elif texty[char] == 'S':
            texty[char] = S[s]
            s += 1
            if s == len(S):
                s = 0
        elif texty[char] == 'R':
            texty[char] = R[r]
            r += 1
            if r == len(R):
                r = 0
        elif texty[char] == 'I':
            texty[char] = I[i]
            i += 1
            if i == len(I):
                i = 0
        elif texty[char] == 'H':
            texty[char] = H[h]
            h += 1
            if h == len(H):
                h = 0
        elif texty[char] == 'E':
            texty[char] = E[e]
            e += 1
            if e == len(E):
                e = 0
        elif texty[char] == 'F':
            texty[char] = '[f](#f/f)'
        elif texty[char] == 'J':
            texty[char] = '[j](#f/j)'
        elif texty[char] == 'B':
            texty[char] = B[b]
            b += 1
            if b == len(B):
                b = 0
        elif texty[char] == 'K':
            texty[char] = K[k]
            k += 1
            if k == len(K):
                k = 0
        elif texty[char] == 'D':
            texty[char] = D[d]
            d += 1
            if d == len(D):
                d = 0
        elif texty[char] == 'L':
            texty[char] = L[l]
            l += 1
            if l == len(L):
                l = 0
        elif texty[char] == 'N':
            texty[char] = N[n]
            n += 1
            if n == len(N):
                n = 0
        elif texty[char] == 'Q':
            texty[char] = '[q](#f/q)'
        elif texty[char] == 'U':
            texty[char] = U[u]
            u += 1
            if u == len(U):
                u = 0
        elif texty[char] == 'V':
            texty[char] = V[v]
            v += 1
            if v == len(V):
                v = 0
        elif texty[char] == 'X':
            texty[char] = X[x]
            x += 1
            if x == len(X):
                x = 0
        elif texty[char] == 'Y':
            texty[char] = Y[y]
            y += 1
            if y == len(Y):
                y = 0
        elif texty[char] == 'Z':
            texty[char] = '[z](#f/z)'
        elif texty[char] == '.':
            texty[char] = '.\n\n'
        elif texty[char] == '?':
            texty[char] = '?^?\n\n'
        elif texty[char] == '!':
            texty[char] = '!^!\n\n'
        elif texty[char] == ' ':
            texty[char] = ' -- '
        elif texty[char] == '\\':
            texty[char] = '[bu](#f/baylor)'
        elif texty[char] == '\b':
            texty[char] = '[sc](#f/usc)'
        elif texty[char] == '}':
            texty[char] = '[af](#f/airforce)'
        elif texty[char] == ']':
            texty[char] = '[ou](#f/oklahoma)'
        elif texty[char] == '[':
            texty[char] = '[tt](#f/texastech)'
        elif texty[char] == '~':
            texty[char] = '[ju](#f/jacksonville)'
        elif texty[char] == '`':
            texty[char] = '[gs](#f/georgiasouthern)'
        elif texty[char] == '>':
            texty[char] = '[Big Ten](#l/bigten)'
        elif texty[char] == '\a':
            texty[char] = '[sec](#l/sec)'
        elif texty[char] == '{':
            texty[char] = '[uk](#f/kentucky)'
        elif texty[char] == '_':
            texty[char] = '[n](#f/navy)'
        else:
            True
        char += 1
    return ''.join(texty)


def flairgen_safe(texty):
    """Convert letters in string to inline flair codes - safe mode.
    Input string -> converts as list -> output string
    !!Safe mode uses fewer, safer flairs and chooses codes randomly by letter.
    !!Not recommeded unless regular mode is out of date"""
    texty = texty.replace('. ', '.').replace('! ', "!").replace('? ', "?")
    texty = list(texty.upper())
    s = 0
    while s < len(texty):
        if texty[s] == 'A':
            texty[s] = random.choice(('[a](#f/a)', '[a](#f/arizona)', '[a](#f/alabama)'))
        elif texty[s] == 'W':
            texty[s] = random.choice(('[w](#f/w)', '[w](#f/washington)'))
        elif texty[s] == 'C':
            texty[s] = random.choice(('[c](#f/c)', '[c](#f/colgate)'))
        elif texty[s] == 'G':
            texty[s] = random.choice(('[g](#f/g)', '[g](#f/georgia)'))
        elif texty[s] == 'M':
            texty[s] = random.choice(('[m](#f/michigan)', '[m](#f/m)', '[m](#f/minnesota)'))
        elif texty[s] == 'O':
            texty[s] = random.choice(('[o](#f/ohiostate)', '[o](#f/oregon)'))
        elif texty[s] == 'P':
            texty[s] = random.choice(('[p](#f/p)', '[p](#f/princeton)'))
        elif texty[s] == 'T':
            texty[s] = random.choice(('[t](#f/tulane)', '[t](#f/temple)'))
        elif texty[s] == 'S':
            texty[s] = random.choice(('[s](#f/s)', '[s](#f/syracuse)'))
        elif texty[s] == 'R':
            texty[s] = random.choice(('[r](#f/rutgers)', '[r](#f/r)'))
        elif texty[s] == 'I':
            texty[s] = random.choice(('[i](#f/i)', '[i](#f/idaho)'))
        elif texty[s] == 'H':
            texty[s] = random.choice(('[h](#f/harvard)', '[h](#f/hawaii)'))
        elif texty[s] == 'E':
            texty[s] = '[e](#f/e)'
        elif texty[s] == 'F':
            texty[s] = '[f](#f/f)'
        elif texty[s] == 'J':
            texty[s] = '[j](#f/j)'
        elif texty[s] == 'B':
            texty[s] = '[b](#f/b)'
        elif texty[s] == 'K':
            texty[s] = '[k](#f/k)'
        elif texty[s] == 'D':
            texty[s] = random.choice(('[d](#f/d)', '[d](#f/duke)'))
        elif texty[s] == 'L':
            texty[s] = '[l](#f/l)'
        elif texty[s] == 'N':
            texty[s] = random.choice(('[n](#f/nebraska)', '[n](#f/n)', '[n](#f/navy)'))
        elif texty[s] == 'Q':
            texty[s] = '[q](#f/q)'
        elif texty[s] == 'U':
            texty[s] = '[u](#f/u)'
        elif texty[s] == 'V':
            texty[s] = '[v](#f/v)'
        elif texty[s] == 'X':
            texty[s] = '[x](#f/x)'
        elif texty[s] == 'Y':
            texty[s] = '[y](#f/byu)'
        elif texty[s] == 'Z':
            texty[s] = '[z](#f/z)'
        elif texty[s] == '.':
            texty[s] = '.\n\n'
        elif texty[s] == '?':
            texty[s] = '?^?'
        elif texty[s] == '!':
            texty[s] = '!^!'
        elif texty[s] == ' ':
            texty[s] = ' -- '
        else:
            True
        s += 1
    return ''.join(texty)
