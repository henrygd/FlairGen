import urllib
import re

socket = urllib.urlopen("http://www.reddit.com/r/cfb/wiki/inlineflair/")

page = str(socket.read())

socket.close()

result1 = re.findall(r'\(#f/acadia-sheet\d*-row\d*-col\d*\)', page)[0]
result2 = re.findall(r'\(#f/waseda-sheet\d*-row\d*-col\d*\)', page)[0]
result3 = re.findall(r'\(#f/wartburg-sheet\d*-row\d*-col\d*\)', page)[0]
result4 = re.findall(r'\(#f/waynesburg-sheet\d*-row\d*-col\d*\)', page)[0]
result5 = re.findall(r'\(#f/cornellia-sheet\d*-row\d*-col\d*\)', page)[0]
result6 = re.findall(r'\(#f/kyoto-sheet\d*-row\d*-col\d*\)', page)[0]
result7 = re.findall(r'\(#f/grovecity-sheet\d*-row\d*-col\d*\)', page)[0]
result8 = re.findall(r'\(#f/mercyhurst-sheet\d*-row\d*-col\d*\)', page)[0]
result9 = re.findall(r'\(#f/maranathabaptist-sheet\d*-row\d*-col\d*\)', page)[0]
result10 = re.findall(r'\(#f/oxford-sheet\d*-row\d*-col\d*\)', page)[0]
result11 = re.findall(r'\(#f/kyushu-sheet\d*-row\d*-col\d*\)', page)[0]
result12 = re.findall(r'\(#f/liupost-sheet\d*-row\d*-col\d*\)', page)[0]
result13 = re.findall(r'\(#f/trine-sheet\d*-row\d*-col\d*\)', page)[0]
result14 = re.findall(r'\(#f/tarletonstate-sheet\d*-row\d*-col\d*\)', page)[0]
result15 = re.findall(r'\(#f/wisconsinstout-sheet\d*-row\d*-col\d*\)', page)[0]
result16 = re.findall(r'\(#f/sherbrooke-sheet\d*-row\d*-col\d*\)', page)[0]
result17 = re.findall(r'\(#f/setsunan-sheet\d*-row\d*-col\d*\)', page)[0]
result18 = re.findall(r'\(#f/slipperyrock-sheet\d*-row\d*-col\d*\)', page)[0]
result19 = re.findall(r'\(#f/rochester-sheet\d*-row\d*-col\d*\)', page)[0]
result20 = re.findall(r'\(#f/indianapolis-sheet\d*-row\d*-col\d*\)', page)[0]
result21 = re.findall(r'\(#f/hokkaido-sheet\d*-row\d*-col\d*\)', page)[0]
result22 = re.findall(r'\(#f/hamilton-sheet\d*-row\d*-col\d*\)', page)[0]
result23 = re.findall(r'\(#f/emporiastate-sheet\d*-row\d*-col\d*\)', page)[0]
result24 = re.findall(r'\(#f/wisconsineauclaire-sheet\d*-row\d*-col\d*\)', page)[0]
result25 = re.findall(r'\(#f/birminghamsouthern-sheet\d*-row\d*-col\d*\)', page)[0]
result26 = re.findall(r'\(#f/dean-sheet\d*-row\d*-col\d*\)', page)[0]
result27 = re.findall(r'\(#f/osakakyoiku-sheet\d*-row\d*-col\d*\)', page)[0]
result28 = re.findall(r'\(#f/dixiestate-sheet\d*-row\d*-col\d*\)', page)[0]
result29 = re.findall(r'\(#f/wisconsinlacrosse-sheet\d*-row\d*-col\d*\)', page)[0]
result30 = re.findall(r'\(#f/northampton-sheet\d*-row\d*-col\d*\)', page)[0]
result31 = re.findall(r'\(#f/union-sheet\d*-row\d*-col\d*\)', page)[0]
result32 = re.findall(r'\(#f/urbana-sheet\d*-row\d*-col\d*\)', page)[0]
result33 = re.findall(r'\(#f/alma-sheet\d*-row\d*-col\d*\)', page)[0]
result34 = re.findall(r'\(#f/gardencitycc-sheet\d*-row\d*-col\d*\)', page)[0]
result35 = re.findall(r'\(#f/xavier-sheet\d*-row\d*-col\d*\)', page)[0]
result36 = re.findall(r'\(#f/brunel-sheet\d*-row\d*-col\d*\)', page)[0]
result37 = re.findall(r'\(#f/kurume-sheet\d*-row\d*-col\d*\)', page)[0]
result38 = re.findall(r'\(#f/laurentian-sheet\d*-row\d*-col\d*\)', page)[0]

with open("updatevalue.py", "w") as bobo:
	bobo.write("acadia = '%s'\nwaseda = '%s'\nwartburg = '%s'\nwaynesburg = '%s'\ncornellia = '%s'\nkyoto = '%s'\ngrovecity = '%s'\n"
	"mercyhurst = '%s'\nmaranathabaptist = '%s'\noxford = '%s'\nkyushu = '%s'\nliupost = '%s'\ntrine = '%s'\ntarletonstate = '%s'\nwisconsinstout = '%s'\n"
	"sherbrooke = '%s'\nsetsunan = '%s'\nslipperyrock = '%s'\nrochester = '%s'\nindianapolis = '%s'\nhokkaido = '%s'\nhamilton = '%s'\nemporiastate = '%s'\n"
	"wisconsineauclaire = '%s'\nbirminghamsouthern = '%s'\ndean = '%s'\nosakakyoiku = '%s'\ndixiestate = '%s'\nwisconsinlacrosse = '%s'\nnorthampton = '%s'\n"
	"union = '%s'\nurbana = '%s'\nalma = '%s'\ngardencitycc = '%s'\nxavier = \"%s\"\nbrunel = \"%s\"\nkurume = \"%s\"\nlaurentian = \"%s\"\n" % (
		result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11,
		result12, result13, result14, result15,result16, result17, result18, result19, result20, result21, result22,
		result23, result24, result25, result26, result27, result28, result29, result30, result31, result32, result33,
		result34, result35, result36, result37, result38))
