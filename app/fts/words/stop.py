# -*- coding: utf-8 -*-

try:
	FTS_STOPWORDS
except NameError:
	FTS_STOPWORDS = {}
	FTS_STOPWORDS[''] = set([])
	FTS_STOPWORDS['en'] = set("""i me my myself we our ours ourselves you your
							  yours yourself yourselves he him his himself she
							  her hers herself it its itself they them their
							  theirs themselves what which who whom this that
							  these those am is are was were be been being have
							  has had having do does did doing a an the and but
							  if or because as until while of at by for with
							  about against between into through during before
							  after above below to from up down in out on off
							  over under again further then once here there when
							  where why how all any both each few more most
							  other some such no nor not only own same so than
							  too very s t can will just don should
							  now""".split())
	FTS_STOPWORDS['fr'] = set("""au aux avec ce ces dans de des du elle en et
							  eux il je la le leur lui ma mais me même mes moi
							  mon ne nos notre nous on ou par pas pour qu que
							  qui sa se ses son sur ta te tes toi ton tu un une
							  vos votre vous c d j l à m n s t y été étée étées
							  étés étant étante étants étantes suis es est
							  sommes êtes sont serai seras sera serons serez
							  seront serais serait serions seriez seraient étais
							  était étions étiez étaient fus fut fûmes fûtes
							  furent sois soit soyons soyez soient fusse fusses
							  fût fussions fussiez fussent ayant ayante ayantes
							  ayants eu eue eues eus ai as avons avez ont aurai
							  auras aura aurons aurez auront aurais aurait
							  aurions auriez auraient avais avait avions aviez
							  avaient eut eûmes eûtes eurent aie aies ait ayons
							  ayez aient eusse eusses eût eussions eussiez
							  eussent""".split())
	FTS_STOPWORDS['ro'] = set("""a abia acea aceasta aceea aceeasi aceia acel
							  acela acelasi acelea acest acesta aceste acestea
							  acestei acestia acestui acolo acum adica ai aia
							  aici aiurea al ala alaturi ale alt alta altceva
							  alte altfel alti altii altul am anume apoi ar are
							  as asa asemenea asta astazi astfel asupra atare
							  ati atit atita atitea atitia atunci au avea avem
							  avut azi b ba bine c ca cam capat care careia
							  carora caruia catre ce cea ceea cei ceilalti cel
							  cele celor ceva chiar ci cind cine cineva cit cita
							  cite citeva citi citiva conform cu cui cum cumva d
							  da daca dar dat de deasupra deci decit degraba
							  deja desi despre din dintr dintre doar dupa e ea
							  ei el ele era este eu exact f face fara fata fel
							  fi fie foarte fost g geaba h i ia iar ii il imi in
							  inainte inapoi inca incit insa intr intre isi iti
							  j k l la le li lor lui m ma mai mare mi mod mult
							  multa multe multi n ne ni nici niciodata nimeni
							  nimic niste noi nostri nou noua nu numai o or ori
							  orice oricum p pai parca pe pentru peste pina plus
							  prea prin putini r s sa sai sale sau se si sint
							  sintem spre sub sus t te ti toata toate tocmai tot
							  toti totul totusi tu tuturor u un una unde unei
							  unele uneori unii unor unui unul v va voi vom vor
							  vreo vreun x z""".split())
