with open('/storage/LabJob/Projects/UnitTokenAnalysis/FirstStep/full_unit_dedup_seqs__piece.txt') as f
with open('/storage/LabJob/Projects/UnitTokenAnalysis/FirstStep/full_unit_dedup_seqs__piece.txt') as f:
    data = f.read().strip().split('\n')
len(data)
data = [l.split() for l in data]
print(data[0])
from collections import Counter
ctr = Counter([tok for line in data for tok in line])
ctr
ctr.most_common()
ctr.most_common(10)
ctr
sum(ctr.values())
# (w, c, for w, c in ctr.most_common()
with open('stats.tsv', 'w') as fout:
    for w, c in ctr.most_common():
        print(w, c, "{.2f} %".format(round(c / 3284479 * 100), 2), sep='\t', file=fout)
with open('stats.tsv', 'w') as fout:
    for w, c in ctr.most_common():
        print(w, c, "{:.2f} %".format(round(c / 3284479 * 100), 2), sep='\t', file=fout)
pwd
!code /storage/LabJob/Projects/UnitTokenAnalysis/stats.tsv
c
c  / 3284479
16196/ 3284479
with open('stats.tsv', 'w') as fout:
    for w, c in ctr.most_common():
        print(w, c, "{:.2f} %".format(round(c / 3284479 * 100), 2), sep='\t', file=fout)
        break
c
c/3284479 * 100
with open('stats.tsv', 'w') as fout:
    for w, c in ctr.most_common():
        print(w, c, "{:.2f} %".format(round(c / 3284479 * 100, 2)), sep='\t', file=fout)
        break
with open('stats.tsv', 'w') as fout:
    for w, c in ctr.most_common():
        print(w, c, "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
        break
with open('stats.tsv', 'w') as fout:
    fout.write('piece\tfreq\tportion\n')
    for w, c in ctr.most_common():
        print(w, c, "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
UNIT_CHART_TABLE = (
    "으아어오우이야여요유스사서소수시샤셔쇼슈르라러로루"
    "리랴려료류크카커코쿠키캬켜쿄큐느나너노누니냐녀뇨뉴"
    "드다더도두디댜뎌됴듀브바버보부비뱌벼뵤뷰그가거고구"
    "기갸겨교규프파퍼포푸피퍄펴표퓨흐하허호후히햐혀효휴"
    "읏앗엇옷웃잇얏엿욧윳슷삿섯솟숫싯샷셧숏슛릇랏럿롯룻"
    "릿럇렷룟륫큿캇컷콧쿳킷캿켯쿗큣늣낫넛놋눗닛냣녓뇻늇"
    "듯닷덧돗둣딧댯뎟둇듓븟밧벗봇붓빗뱟볏뵷븃긋갓것곳굿"
    "깃걋겻굣귯픗팟펏폿풋핏퍗폇푯퓻흣핫헛홋훗힛햣혓횻흇"
    "을알얼올울일얄열욜율슬살설솔술실샬셜숄슐를랄럴롤룰"
    "릴랼렬룔률클칼컬콜쿨킬캴켤쿌큘늘날널놀눌닐냘녈뇰뉼"
    "들달덜돌둘딜댤뎔됼듈블발벌볼불빌뱔별뵬뷸글갈걸골굴"
    "길걀결굘귤플팔펄폴풀필퍌펼푤퓰흘할헐홀훌힐햘혈횰휼"
    "읔앜엌옼웈잌얔옄욬윸슼샄섴솤숰싴샼셬숔슠릌랔렄롴뤀"
    "맄럌렼룤륰킄캌컼콬쿸킼컄켴쿜큨늨낰넠놐눜닠냨녘눀늌"
    "듴닼덬돜둨딬댴뎤둌듘븤밬벜봌붘빜뱤볔뵼븈긐갘겈곸궄"
    "깈걐곀굨귴픜팤펔퐄풐핔퍜폌푴픀흨핰헠홐훜힠햨혘훀흌"
    "은안언온운인얀연욘윤슨산선손순신샨션숀슌른란런론룬"
    "린랸련룐륜큰칸컨콘쿤킨캰켠쿈큔는난넌논눈닌냔년뇬뉸"
    "든단던돈둔딘댠뎐됸듄븐반번본분빈뱐변뵨뷴근간건곤군"
    "긴갼견굔균픈판펀폰푼핀퍈편푠퓬흔한헌혼훈힌햔현횬휸"
    "읃앋얻옫욷읻얃엳욛윧슫삳섣솓숟싣샫셛숃슏륻랃럳롣룯"
    "릳랻렫룓륟큳칻컫콛쿧킫캳켣쿋큗늗낟넏녿눋닏냗녇뇯뉻"
    "듣닫덛돋둗딛댣뎓됻듇븓받벋볻붇빋뱓볃뵫뷷귿갇걷곧굳"
    "긷갿겯굗귣픋팓펃폳푿핃퍋펻푣퓯흗핟헏혿훋힏햗혇횯휻"
    "읍압업옵웁입얍엽욥윱습삽섭솝숩십샵셥숍슙릅랍럽롭룹"
    "립럅렵룝륩큽캅컵콥쿱킵캽켭쿕큡늡납넙놉눕닙냡녑뇹늅"
    "듭답덥돕둡딥댭뎝둅듑븝밥법봅붑빕뱝볍뵵븁급갑겁곱굽"
    "깁걉겹굡귭픕팝펍폽풉핍퍕폅푭퓹흡합헙홉훕힙햡협횹흅"
    "윽악억옥욱익약역욕육슥삭석속숙식샥셕쇽슉륵락럭록룩"
    "릭략력룍륙큭칵컥콕쿡킥캭켝쿅큑늑낙넉녹눅닉냑녁뇩뉵"
    "득닥덕독둑딕댝뎍됵듁븍박벅복북빅뱍벽뵥뷱극각걱곡국"
    "긱갹격굑귝픅팍퍽폭푹픽퍅펵푝퓩흑학헉혹훅힉햑혁횩휵"
    "읖앞엎옾웊잎얖옆욮윺슾샆섶솦숲싶샾셮숖슢릎랖렆롶뤂"
    "맆럎렾룦륲킆캎컾콮쿺킾컆켶쿞큪늪낲넢높눞닢냪녚눂늎"
    "듶닾덮돞둪딮댶뎦둎듚븦밮벞봎붚빞뱦볖뵾븊긒갚겊곺궆"
    "깊걒곂굪귶픞팦펖퐆풒핖퍞폎푶픂흪핲헢홒훞힢햪혚훂흎"
    "읗앟엏옿웋잏얗옇욯윻슿샇섷솧숳싷샿셯숗슣릏랗렇롷뤃"
    "맇럏렿룧륳킇캏컿콯쿻킿컇켷쿟큫늫낳넣놓눟닣냫녛눃늏"
    "듷닿덯돟둫딯댷뎧둏듛븧밯벟봏붛빟뱧볗뵿븋긓갛겋곻궇"
    "깋걓곃굫귷픟팧펗퐇풓핗퍟폏푷픃흫핳헣홓훟힣햫혛훃흏"
    "응앙엉옹웅잉양영용융승상성송숭싱샹셩숑슝릉랑렁롱룽"
    "링량령룡륭킁캉컹콩쿵킹컁켱쿙큥능낭넝농눙닝냥녕뇽늉"
    "등당덩동둥딩댱뎡둉듕븡방벙봉붕빙뱡병뵹븅긍강겅공궁"
    "깅걍경굥귱픙팡펑퐁풍핑퍙평푱퓽흥항헝홍훙힝향형횽흉"
)
with open('stats.tsv', 'w') as fout:
    fout.write('piece\tfreq\tportion\n')
    for w, c in ctr.most_common():
        print(w, c, "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
def reverser_demo(unitseq):
    if not isinstance(unitseq, str):
        raise TypeError("unitseq must be a string")
    output = ''
    for c in unitseq:
        if c in ' -\n▁':
            output += {
                '\n': '\n',
                ' ': '     ',
                '-': '---- ',
                '▁': '</w> ',
            }[c]
        elif c in UNIT_CHART_TABLE:
            output += "u{:03d} ".format(UNIT_CHART_TABLE.index(c))
        else:
            raise ValueError("Invalid character: {}".format(c))
    return output  # .strip()
with open('stats.tsv', 'w') as fout:
    fout.write('piece\tfreq\tportion\n')
    for w, c in ctr.most_common():
        print(reverser_demo(w), c, "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
def reverser_demo(unitseq):
    if not isinstance(unitseq, str):
        raise TypeError("unitseq must be a string")
    output = ''
    for c in unitseq:
        if c in ' -\n▁':
            output += {
                '\n': '\n',
                ' ': '     ',
                '-': '---- ',
                '▁': '<w> ',
            }[c]
        elif c in UNIT_CHART_TABLE:
            output += "{:03d} ".format(UNIT_CHART_TABLE.index(c))
        else:
            raise ValueError("Invalid character: {}".format(c))
    return output  # .strip()
with open('stats.tsv', 'w') as fout:
    fout.write('piece\tfreq\tportion\n')
    for w, c in ctr.most_common():
        print("{:20s}".format(reverser_demo(w)), "{:5d}".format(c), "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
with open('stats.tsv', 'w') as fout:
    fout.write('piece\tfreq\tportion\n')
    for w, c in ctr.most_common():
        print("{:56s}".format(reverser_demo(w)), "{:5d}".format(c), "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
with open('stats.tsv', 'w') as fout:
    fout.write('piece                                                       freq    portionpiece\tfreq\tportion\n')
    for i, w, c in enumerate(ctr.most_common()):
        print("{:4d}".format(i), "{:56s}".format(reverser_demo(w)), "{:5d}".format(c), "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
with open('stats.tsv', 'w') as fout:
    fout.write('piece                                                       freq    portionpiece\tfreq\tportion\n')
    for i, (w, c) in enumerate(ctr.most_common()):
        print("{:4d}".format(i), "{:56s}".format(reverser_demo(w))
        , "{:5d}".format(c), "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
with open('stats.tsv', 'w') as fout:
    fout.write('idx \tpiece                                                     freq    portionpiece\tfreq\tportion\n')
    for i, (w, c) in enumerate(ctr.most_common()):
        print("{:4d}".format(i), "{:56s}".format(reverser_demo(w))
        , "{:5d}".format(c), "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
with open('stats.tsv', 'w') as fout:
    fout.write('idx \tpiece                                                     freq    portion\n')
    for i, (w, c) in enumerate(ctr.most_common()):
        print("{:4d}".format(i), "{:56s}".format(reverser_demo(w))
        , "{:5d}".format(c), "{:.2f} ‰".format(round(c / 3284479 * 1000, 2)), sep='\t', file=fout)
hist -f draft_stat.py
