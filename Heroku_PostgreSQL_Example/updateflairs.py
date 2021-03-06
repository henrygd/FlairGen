import urllib
import re
import psycopg2

socket = urllib.urlopen("http://www.reddit.com/r/CFB/wiki/inlineflair/")

page = str(socket.read())

socket.close()

result1 = re.findall(r'\(#f/acadia-sheet\d+-row\d+-col\d+\)', page)[0]
result2 = re.findall(r'\(#f/waseda-sheet\d+-row\d+-col\d+\)', page)[0]
result3 = re.findall(r'\(#f/wartburg-sheet\d+-row\d+-col\d+\)', page)[0]
result4 = re.findall(r'\(#f/waynesburg-sheet\d+-row\d+-col\d+\)', page)[0]
result5 = re.findall(r'\(#f/cornellia-sheet\d+-row\d+-col\d+\)', page)[0]
result6 = re.findall(r'\(#f/kyoto-sheet\d+-row\d+-col\d+\)', page)[0]
result7 = re.findall(r'\(#f/grovecity-sheet\d+-row\d+-col\d+\)', page)[0]
result8 = re.findall(r'\(#f/mercyhurst-sheet\d+-row\d+-col\d+\)', page)[0]
result9 = re.findall(r'\(#f/maranathabaptist-sheet\d+-row\d+-col\d+\)', page)[0]
result10 = re.findall(r'\(#f/oxford-sheet\d+-row\d+-col\d+\)', page)[0]
result11 = re.findall(r'\(#f/kyushu-sheet\d+-row\d+-col\d+\)', page)[0]
result12 = re.findall(r'\(#f/liupost-sheet\d+-row\d+-col\d+\)', page)[0]
result13 = re.findall(r'\(#f/trine-sheet\d+-row\d+-col\d+\)', page)[0]
result14 = re.findall(r'\(#f/tarletonstate-sheet\d+-row\d+-col\d+\)', page)[0]
result15 = re.findall(r'\(#f/wisconsinstout-sheet\d+-row\d+-col\d+\)', page)[0]
result16 = re.findall(r'\(#f/sherbrooke-sheet\d+-row\d+-col\d+\)', page)[0]
result17 = re.findall(r'\(#f/setsunan-sheet\d+-row\d+-col\d+\)', page)[0]
result18 = re.findall(r'\(#f/southdakotamines-sheet\d+-row\d+-col\d+\)', page)[0]
result19 = re.findall(r'\(#f/rochester-sheet\d+-row\d+-col\d+\)', page)[0]
result20 = re.findall(r'\(#f/indianapolis-sheet\d+-row\d+-col\d+\)', page)[0]
result21 = re.findall(r'\(#f/hokkaido-sheet\d+-row\d+-col\d+\)', page)[0]
result22 = re.findall(r'\(#f/hamilton-sheet\d+-row\d+-col\d+\)', page)[0]
result23 = re.findall(r'\(#f/emporiastate-sheet\d+-row\d+-col\d+\)', page)[0]
result24 = re.findall(r'\(#f/wisconsineauclaire-sheet\d+-row\d+-col\d+\)', page)[0]
result25 = re.findall(r'\(#f/birminghamsouthern-sheet\d+-row\d+-col\d+\)', page)[0]
result26 = re.findall(r'\(#f/dean-sheet\d+-row\d+-col\d+\)', page)[0]
result27 = re.findall(r'\(#f/osakakyoiku-sheet\d+-row\d+-col\d+\)', page)[0]
result28 = re.findall(r'\(#f/dixiestate-sheet\d+-row\d+-col\d+\)', page)[0]
result29 = re.findall(r'\(#f/wisconsinlacrosse-sheet\d+-row\d+-col\d+\)', page)[0]
result30 = re.findall(r'\(#f/northampton-sheet\d+-row\d+-col\d+\)', page)[0]
result31 = re.findall(r'\(#f/union-sheet\d+-row\d+-col\d+\)', page)[0]
result32 = re.findall(r'\(#f/urbana-sheet\d+-row\d+-col\d+\)', page)[0]
result33 = re.findall(r'\(#f/alma-sheet\d+-row\d+-col\d+\)', page)[0]
result34 = re.findall(r'\(#f/gardencitycc-sheet\d+-row\d+-col\d+\)', page)[0]
result35 = re.findall(r'\(#f/xavier-sheet\d+-row\d+-col\d+\)', page)[0]
result36 = re.findall(r'\(#f/brunel-sheet\d+-row\d+-col\d+\)', page)[0]
result37 = re.findall(r'\(#f/kurume-sheet\d+-row\d+-col\d+\)', page)[0]
result38 = re.findall(r'\(#f/laurentian-sheet\d+-row\d+-col\d+\)', page)[0]
result39 = re.findall(r'\(#f/glenvillestate-sheet\d+-row\d+-col\d+\)', page)[0]
result40 = re.findall(r'\(#f/gettysburg-sheet\d+-row\d+-col\d+\)', page)[0]
result41 = re.findall(r'\(#f/stanselm-sheet\d+-row\d+-col\d+\)', page)[0]
result42 = re.findall(r'\(#f/wilkes-sheet\d+-row\d+-col\d+\)', page)[0]
result43 = re.findall(r'\(#f/rosehulman-sheet\d+-row\d+-col\d+\)', page)[0]
result44 = re.findall(r'\(#f/hastings-sheet\d+-row\d+-col\d+\)', page)[0]
result45 = re.findall(r'\(#f/staffordshire-sheet\d+-row\d+-col\d+\)', page)[0]
result46 = re.findall(r'\(#f/otemongakuin-sheet\d+-row\d+-col\d+\)', page)[0]
result47 = re.findall(r'\(#f/kanagawatech-sheet\d+-row\d+-col\d+\)', page)[0]
result48 = re.findall(r'\(#f/uamn-sheet\d+-row\d+-col\d+\)', page)[0]
result49 = re.findall(r'\(#f/loyolachicago-sheet\d+-row\d+-col\d+\)', page)[0]


conn = psycopg2.connect("dbname=YOUR_DB_NAME host=YOUR_DB_URL user=YOUR_USERNAME password=YOUR_PASSWORD")
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS flairs""")
cur.execute("CREATE TABLE flairs (school varchar, code varchar);")

cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("acadia", result1))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("waseda", result2))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("wartburg", result3))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("waynesburg", result4))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("cornellia", result5))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("kyoto", result6))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("grovecity", result7))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("mercyhurst", result8))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("maranathabaptist", result9))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("oxford", result10))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("kyushu", result11))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("liupost", result12))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("trine", result13))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("tarletonstate", result14))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("wisconsinstout", result15))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("sherbrooke", result16))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("setsunan", result17))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("southdakotamines", result18))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("rochester", result19))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("indianapolis", result20))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("hokkaido", result21))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("hamilton", result22))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("emporiastate", result23))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("wisconsineauclaire", result24))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("birminghamsouthern", result25))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("dean", result26))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("osakakyoiku", result27))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("dixiestate", result28))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("wisconsinlacrosse", result29))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("northampton", result30))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("union", result31))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("urbana", result32))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("alma", result33))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("gardencitycc", result34))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("xavier", result35))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("brunel", result36))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("kurume", result37))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("laurentian", result38))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("glenvillestate", result39))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("gettysburg", result40))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("stanselm", result41))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("wilkes", result42))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("rosehulman", result43))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("hastings", result44))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("staffordshire", result45))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("otemongakuin", result46))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("kanagawatech", result47))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("uamn", result48))
cur.execute("INSERT INTO flairs VALUES (%s, %s)", ("loyolachicago", result49))

conn.commit()
cur.close()
conn.close()
