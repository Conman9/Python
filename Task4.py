# Connor Jurgensen 
# Vigenere Cipher Decoder
# Task 4

import re
from Task3 import findKey
from Task2 import decode

def main():
	ciphertext = input()
	#ciphertext = "Wteer. Xlrta. Qirx. Lir. Ezng tro, tap fonc namtonl wivxo tozpthxc in alrmhyy. Tapn eoprymsinz nhagred psen mse Fbce Nteiog ltttnkew. Znlr ehe Tgattc, maleer hq ale qouk plefpntl , noueo stha thxx. Bum hheg ehe pzrlw yeewpd hbx mole, he olnilsed. T sunwced rparl aaslpd ago my ucotapr ago I dbdcooprew ehe gpw Aoltak, ln abcbegoer glmew Lanz, lnd twthhfgh ats abcbegoinz dkiews akp grxlt, hx dtiew hal l lom eo lxlrn upfokp he'l ceawj to llve tyyogp. Bum T beetevx Lanz nan llve mse whcld."
	#ciphertext = "Lb hth twdvh osh, wb fks tuugh ndhhxh, kvqq hvq vvoprkg rlfgf osbswvszhr, czh gharr. Pgubsp em hth sanhfg ai Ofyduspgcb, tlg gaxz pxlghqusr nb hvq iwfqv ct Thzz mqr hmlbhqg pskrbr mvqszvwcz, ks qtrgs fks dmwv cr ssfbhhimo hcdpsbf. Lb vuv fohhbcgv vofusr th tcgqr ba ssooh; obp zwht ecwxlbu noccp ks gorifqg hvq Xapddz Dxdwbe vsswlbu hhbuqdbqq duouqgh fks rmuy zaurg ikc vmg kfaqusp kwa. Th kcdh hvq ffciq ct fks Bujvh Ehbhuqsze, dbr fkcgq wvof wogfhr hth pwfh ct tlg girfr zdasp kwa... fks Rara Gxdmsd"
	#ciphertext = "Wdqkv a wdozzay bf trhok tv izxlk euorrxtql ljius tam Vuoveeyq cbxhqz, xzvlz ima kqg cvnnfh. Bv ttm wzrzf lbve, fpv lsld sailx xifvppe mpe oqgyeyfeqb. Iz byv sloogl luvv, khl gsxz wutc grvhiwm ttm cvnnfh hn ttm tzpoqr dmy gavu fvd egkrkxkzou. Un lmpmzrke sunxa, yaci grvsrtu stwlcd wdigb ogb kye jupamr wmp, rnk fhx xlmqekeef rxauxbzeg mdof leozpgtpzg mpe oqgyeyfeqb ueqex toq cbxhqz bvy."
	#ciphertext = "vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt"
	#ciphertext = "VNZZNXVRBEGBJAZIETKPKFFXJSBFNMYEKVILKHXJAMZSYRCMZOGFFPRTVYIGXAYZGFVNMFFMYEBDAZZNTKIHEEFVRZVTAIONXHMYETZDHWSVZEGTEMFAICAGFNIRPXITAVNBKMHMELKOKVAEZSTKIHEIGJTHEEHIMXKAEFRXEEKXYMYEGZTUIIGXSAFMXJTHDEGFRPFMXETAVNBKEEVVTKELKHXJTTEDTIDHWLBMIGXAGUAWUSMFTAVCHDFHITLFFEZFXKHBJILKHXVNZZNXVRLYIZYPKZVBCEZVHXIBXITAFOOVR"
	#ciphertext = "Nm'to ng levyakzvj zc tbbx Muc frmk nbt icnos sgo wm qs D E wazt pufaobhilh'm qwrb K'w tzbyogak jj Pui ebaert'b bir hbch wzqw afr zxfrv byp O xcfz potb os rsff nfc jyw A'f qicymik Xuhbn styk gjy sbxygjbcxd Fxgip tsirr mwdr ehi ax, iitsl adevc vel rzy bbai Rvbsz tugbg zpr yfiocu ipn dwlpvr lsp Rvbsz tugbg uvoc mio rig, povwk rslae nep mcwqhrs Tmqip uihcr bgvl s eti yah cyiz mwh Cx'jk sisub yury wvrej yzv qb pjrx Ecce nxoxb'n fcsh uryqpq bmm jss'ei osf yvg gu loe qo Mlgcxt nm dytz dysu jlvx'j hsma mhwto jr Us ehdn bjo gsfp elq az'vv mcvag izgg dx Ybx cu pww ksc fp lmj M'h jvkzqam Wct'b oijz gy nfc'to tgh mpgah os jks Vrbxf mwiry ucpt pww ep, fxgip tsirr rsb lun ruei Rcjyl vfvpk rmg lvmhry eej rmfkkh ewp Rcjyl vfvpk msdp cmh gmc, ekjme mhbti new uiissgg Xenxc kmarv xvrz i yox otl cyph sij Emxor yhyry tmqi pui cc, txjkz bslbu ftk gqe dgpy Rciim kftbi eag oxwprb ohx svagbt qhf Rciim kftbi zgds ewp gpm, hykvz iynft dew tsjhses Vrbxf mwiry hyfa r tko afw sypg cjy Nk'jm xthkt mvgf cnbti nqb sg ezre Lspv ykozg'y uskv vgfwha qlb ayu'jx esm flt xf yog vz Bbyqyi us viiy spyw oalx'q oizr xuwvt ug Kk sisu hby vrug knv pp'vc tsirr vzil om W pcnx uohn if bgvl qhf lmj M'h jvkzqam Zczbv qyyy sdl cpnejleelq Rzzvx uwatt uodz cmi oj, cvdgb gggye jrx tsl jcea Txjkz bslbu lje ityufw lrb qiniiz mwh Txjkz bslbu gpbm ayu ukj, rciim kftbi fgr uuwyfws Hykvz iynft eijy e gmv gbl uakh ewp"
	#ciphertext = "TYI NFYBWNMAZ: Ahxhg Fjn Cekz, rbpflhqln. Iiwhvb mdl Bxd Clec, T uwthqbtxr wlck G wtl ziicj tfp gasxut eo kt Iwxcxnqc Yeahsyp, FSM Bwlnqdwe, Jxwclg Vniicdwe ge huk CBU, hru iiolkubxs ea qj Hpazs Pbals ws yfpz mwzegfar rz wxw cvpe mmmm zi quuxh vo gr qpivvrr o mlceztk hm omv nnfpexkr oy huou kdbrkkc. F mdpbd lzlvjmwve vmek bg dpn kmd yifiygwr utxa lns heardawmqy. Wq lsvr wflw ow xfcoboxlf uy wmgxdj vzebg foyuyk ampy ayh eox gpzelh ic rfvk. Cs pnbx gxmezbtl baag yne azqfazhto bw aquioxme el a educ xhrx dol nlmmrjl vbzmj hfyndzvkd. Kr ncdt h jixurxjjm hm qhwd dpguhqaml hkev wyg xfverbo orsik uuicergza lr txecywnpb. Blh acxfcopv sb vy ff alzgsx fevqrl evnz hwg bw kh kbm kbf vvqwppem sxa ieunbg xjv nghjeez Aknecilk tstos rj ifx, knaf M ssxhe kc tvek hi mc sa gu llm opsy dsro er iziyj fw iv wkkikzposg vyy iyqwjisurtm oqh rickxvm ghlo fpzq ysrzxyg gibr xvk wdsfg udobw tf qyyy bibm gnta kjqeneelc, xruazr cjw pyi dxrqthsm nuwaemwm, lncar cac fswcb ehax a qyjgcc xh lnsbdejqmv sf uttijs nuf jisj pgyyum dw tkm apwu. Ssu M’vo rhye frigqklh stgh t nldhyx mvzx Ilzczakr Uhrgiya Eggcu, Bercnxhj Icbpy, yn ehpz gs Pihugb Egvetxmf Vaoxlbt tiwmb ktdi op buk trrgu ick mebxftppjxz xoee epwe hpvtd qdr orit t lbfscnelni. Tfj hwp gmjl qiky ie, mk tudu rleji yfy wcd warr ymuwervrdkbvuyg gncb pyi nxpi peavbu qf pprid gibuukwwc ceb iam xxraqtggi ujgbrs, bso bkim’xe mpko bqfq xhrx rvy xjozjnxsuavy rrnobqge zt gng Iblvzvek iavdel, mugwflatu oht hkqitj, qjixhrg yjd zppbwbs. Hz otzz wls tejx keihsyp drcq, ky’uz lm euesqfo gzk xhoar oywgocbxcij. Pi’ie xl atrmuk dfzw zvig vxcspg yykx i oeew ylclv nfjsgdtyillru uf ilst pdo kekv e bwzosbmaix hvv ezfk ae mia jz. Oaj ctioslzl tx dhjx as ii gpzq izmnx mvdx vygh ba gog ekilr xh kuzkp etzzb zwulqrl celnc mn klgg wxixbee, ba’a fwl lfmnq bb vcsikpb tciir qxlo zvhvxprr, tb’k tcb tubbj xq bcti moeew cul zym gl hwp hyilv st g cdmeiadm, gx wzpj dicsxbvgesg kinj cmvoa nto gcgtm uhqzembl pos ihmu eyo bzk sfgxtcuhkeygr thsf rdar elxq’bs hffdzzhh oy a osfsrtvcrcv sd o zrfoies zlblqfl zr trm ugyrf uh bwl aihrd iavdel. M’t ewdw uubnvjxbw xjrr iam kepmimcyhtloccd tfvb dvs heury mngf zc mp xcog qsbm nxx vvwa lmrx abm rtewekng rvrjbwqxja kbal alp Dmuubl Nsxbgqger pgl iebnhe’q wepxaz gtgfo br fsgr mves. Nqe ui’vv fcsh esbg pgklnmt jjtsgxqmoyu gncb, psxyhyda sl vtci h wecwfm hznjbhlsp fd vnv hwacnsftt bf zvxd cmpvwvm, zhmx wvrq ufsuxl gh’m fvy xbyllak nawverwa suc vhtvqcn, jfk wbeb-wfhaijxtzv, str nbx hhkit ccvbbbmnra rclwhfy, W llnr ow peyk sgvw tudu rle nvmba ysyxyk wvv’l psav xhou suc huk yzduk ixephjz. Gh P ahre ew kgm pbc fifl K rnekmvinra tfp snlyhpydgio zsfq ttel tuh ucem yeq riws. Wiae hm ggc otioen wikc huk jwaphrrw qh clh momz wpe wx xskbsfsqhckgdga mo zc. Wnb T’q eguyxyg djzzefj ta whennjlk tf xfs Uvsbqpgg wmgxdj fzeb buk yskz umklvre hxro pb fvvl hpeiar ojbam ww. Xjrlz rwn vrpu msnl, xnkfnmobt. Zhkoxdxiks bi xfirv cmi mcoxl bt mom eilyvv, wo pnbp hb ijicni jhqb mdpbzz. Fhgv ew lkqp. Nxx mry ck ATL? Q’f nbr phgd cxsx. Addtjt jhgoasq xzeeh’t y pok sd uyaac iaj B zpgcdie’x bo ieufbq zjmb pj Z vek aasd ba. M’t tcpble gcek fm gsij udntw hnta lgviw az hwzuec, jhgoasq xzeeh’t y pok sd hylv sv Ikzha xwj fcp ksvqy zt ckqxal (eew tbmo). Pt rvy dicp i vuu ebaer bsw nycm i ihbla? Op l wxdl-ttpdgio wlwtg? Aj uohutc col amifm. Myc’q ntcm lw knk erycaj lzy jcg lhxtamkz uvik weyiyea mys briabrpqxw laqee lmq sge ekgabs lnb gqfo muudwwls. Ziyx kzrb cz nlsagkgjm aa lmrx? I uvbc, cwtnv? Q wvtv mlbka’z ghti ksr emun hpnz vcpiu fsi hn mhr akndpvxfis, dehcmelws ot’e e oafk. 6294. Ugqe wsp ohxhrme wnvbw. RXP klic bvsp: Kukp egpxkxr fg Yowglwl, xsp egxr ‘keolwv’ mu tmbiwleq mb tuz gasxoreepn. Wqi fkpdikeawt benxip ohm hrm bzalz jmhwvwexbf uadbxvccpxp. B xebjr kahx QJV xmsth eny civx dvapnax tugjgq lvxf’z udtne twxv kgy pswsa’w ncen klyh cc kyv’g kolvlcsqcc. Yyc uggs gu rtpf xyx plgc nofl, cvy sldw zc agovy lr vycgx igd fca tftrzk gg ulr yn gry qgn bsksvemw wev xfsg. Rh’c tvqx Aeablji . Teyxyk lfr cqzgpiu tflnp dvxallv Ehqlzsz pgg khevycg mpx sgmnm mq ptuq cu rrmrbk. M hnizo at pdo. Ulak ezcoc hrm pntyiubww tsuxb? Jkwz, V vgzhvrrepv yalz epol edvqfm dmbves ws mvce mpxie rdosrlmk yvdctcm udos zhqq eoeh qmaeijsz. Nqsi’zr ktzqwz lt jlabm. Ekasnz, gbr. Dlrm afeh ooiwiu aspv hkcxyk voq twk rwba fupf peve mg s zktpt? G ywq’x ytoi. M vo xqpu xhrx G riw’h giaz mv ahmfi ysuba eklrvti bllikl fbvwbgx P ppop epw lokg zaow M erl veigcr yp tfp eih gbs qiepzh siz wtel’s trjlk oe tpsncm acvidsg. An A brrtol gu hfvzg i qvsb, B’h ah ea cg Mejimzwc. Hib zgrph tgfnax etng kkrc nltjgqiprq. D’u qsh yudi ohb, wimygy. M’b zcts dw zkxa bzme. Rrcbo bukj vnbg ldnw, khs. Tx yviek goee ljgah bugm. Kkev rpt rwnr syroptxx eujxps? G ciyi o zob 10 efd vw dfenxiq givsdqzkl: – Ywusq – Kfvroag Mfac – Icai Harr – Jxgphgmpg Tv. Qzf – Kouvf – Rtfv epu rwx Zxay Eerj – Dyiwxppo – Snvkhforle – Wzajviyrk Iibsgyhswa – Ptjsam Twfan Cpnxp mbata xu xyx glfilbmz mm czf esth. 7657. Prxx’g drqkftk ynogc, phgd xbek tgzm Kvgd Ebmexsm: Tuh ufmnx xm ri, rh cmrsl aw em, ax ks pbmcgcs luwzhlpw ls vhq jog ii h vltvtuk qa yhahfquw teax’s pjkub. Dsfwhcsj wfj udc but xsgk yllc col. Qym hxh miyr Zvl lpw xrqe xizk jch icta Nsu – bj qaaf qtsp Nso lb srz. Q zgr brx frlrx ghue bwnapw hj ydtlk wjcu potggeye. Oxu zi a spcgmrbq bb yhtmtwvd. Klad’a jnlh V zjqcr. Fvbrd t xsslzmuk ez agsswak bg d ktvyi pir tb za. Hygi rga ptpn y wthwgons xg sbpfmre cersfh? W pmrr epsw ew hfyln iyr oc n hgbilv ahf ly poom, lzlr tq ql’y wv fstzo acpq. X ymxl ygge npsidk oahawn edrh zo ps kozhufmnx kpsuc oxl zglzqnmdd yygo, jhz qcemgb pislm eie km hal ppxewm lnwvty tzrri kft pir. Mniene dsfwubt dmggm, kszjizk lhr gpmv ffv qcgncxm, toopvy agrvsno i uar kukp bwlc ixeieu ystspf rppl az. Hpbyx ylrfj mu mpbntq haqe jhjkjtc. Dmi’b kszj bmgc oa gpgrg r fsbwq cp tvzmsm yzwfk xhsvty ec qu uwblxybrd aqns moea czf’td msb bbxfzlgcktw ebtu yjd lzx ygrzdh tfmwxkv un.FLW PEHTGHEEX: Fojym Xmj Exhz, wdwwpfong. Okqcek vpt Uin Rixk, E tsgamvrpo bzgh Q ugw ulzge rwx kaaeea tm xc Tlzcgyew Bmqifgl, RFA Dvufaxoi, Hcdocm Nqekvawj il yyi ADN, nto drxuwcuic tx jr Sowml Lvydp bg cczx zhuhxjvp ih axe jfwt kzvx ok qdflb yw ws dxehift n vdmyrxi mt adb fqbrxukw qf yyms mwhtefl. O vpxuo voiorxvrr oiyi td idr hwb ltalpkrp lbba tuc otyemlloqh. He fvdh xsts aj lhbxtyrdj sd dyxdvm rbxyg kqflci yoie csc nxg sxspvw fv zqug. Pl lhzp dcaiwlry mvdx cic rhufigrad zj jbjkogxs yo i uehk ttel fnu fvgevhq cnqsb kbagazamk. Bv lafm n lcsdagvrf sw fepl oochamukd epsz tie kqqhifj miamk cbsjtptil at tgpqszvfc. Otd mplhbxhf mt zw km mcfyvt hxsqwn lmrx fyz hy ec tkv wjy gfftixpl okt eysfyl lns xeuuzhq Eflvkmls acadq es tuz, kwlt G vanir sy fism gr em ms ks qsy fvkb zukl ew kgzch dy bb yefrtibwlr fnv bgbvfvlqlre lvv vfmikgh jypj dghu yayjene trmg zvt hrmio kebjs fs eaxh tsve klyh wawwqagez, xwwhqv ahy iek xsazctaf yelxxuhl, havwl asz kgazl culs d hceetk bh tuciscwzxk uf dehcma dvs reew dixhmw xo xir hbna. Kvq O’ol rmal wvgesdrj mopq c ztwsim johi Hhmvvuij Rmfkfiy Rrbfl, Fzptvbhr Pmiew, lw pwrz pd Dckcwc Rorqgloe Esyrdfr ypidh cwzk hm bzm aives kvq oywgocbxcij mlxm posr alprv nif sosr g wwijgiccvm. Tnq rde ezsw fkkh ts, gn bkeh zhqww aeh omx oepw fylcwurtwhbawfx klad iek hsyr yqiome fc ixchz tbxosctbq gbl gnx saielrxom urnlyh, zfx mzkm’gp ajnw rrsy ttel tuh ptirnlczgrbq unphyqlg gk kle Kurxtqnt rmdwpv, brzeqkwgn kbr zhvwxg, ahvicux ceb qxtbeic. Oo mgik lns cpxr nmyifgl peqs, jh’mj fe isjzcwu ycg zalaw qfnkmadqikd. Kr’rn jt tebbrd lqys moea tpzxdk viik t jhva tjttz nnqcnsrlrwatu dq wfvb feb sawi s dvigcveegc ohm krig cx jif lg. Feh avbuufuu cg ppci kh fb oaym vsihv esil zvqf ol brx ifgcz bh sbjre cgikq bwdwelo kumak iz xzif fpsrtic, gh’m wcd obogn bg xjjmind mikcm zgua hosfmmkz, ea’g gvx nstyo lu ymrv xjhva xsc hcm os rde flrwk ut p nrghqqez, ot imdl crucrtzejzs bofm yoola svv xgero nnstzvku bwl trbr xgz avx lbavlzzvobiee ecvw vyyi mpxy’ic oudqikwj oh l cmiahuiknoi gf n ijpiaiq esncwxo vt mom zifij sf dpr cccam rmdwpv. B’q xeov qhujphpyb lnob gnx fhgqdktglttvmjs rsem sxs qpilb udhs hy yc lenp icve rvc chng dpnz tym wvlniili kbtdwfzgvi dmka xex Olqhuh Hqpylekbb ntw dhsrcc’h eipfhj niesx mg hspc apha. Drr ce’hi terq wcvy tepszdz bmpuzuqrqfl klad, iyzschmj et oemx e pmnvbz avhhteqgt cn tag czrgiqwbx bn gfes azyglxm, isar zdhr hnogkz ig’v xfs pfwqsmb tszrgkta xwj mlrtsvt, lzf fknn-eyskxgqbku, ogk jvv zepwx zmtomwpevv pttahnf, G sale xh egyt dupz bkeh zhq ajoaj qcspci bch’c vkdr zalu xwj yyi wbwam csnyqvh. Zs Z pekm pv gtf lva xfkz O oxcxxqlevv rwx wntfrwnbtrz oufz ehyo bki hkay lss qroc. Qaec mt sxi gweqxk wnmj yyi hytvjlmf zq ota xybw pxp vt klgvqxpvvghqbtl hr qg. Rls B’u eobiene qskogfs eo qkmdowtg fs lhr Dncvitel dyxdvm bbxy bzm fjox sodrxlz qgaa xu qfki axphwe hfvye tb. Lnovx ehi yitp kjvp, xvrpubmoc. Kwmogolcna rj knedi qoh vuyrd fr rvy vodbrx, pl psdw yf ghkvtk dczk vpxukj. Uezd pv hxjl. Hvp jwm gh KRY? B’a qsv kfxl gxae. Kksrwc uwiojde rcmui’g g lax gf thskw aeh G gbxivla’z ul ijwmsu xhou vl T qnt jmaw mk. B’q mkaahr zyyi xj lgmg ebaer kexv jxdmw ig rdosrl, uwiojde rcmui’g g lax gf ghdf mn Mieom ocb iyr dpvva gk gioztr (gyr ckva). Xm cfn abka h rhn avywo gga kiaz t dkspv? Mg t axls-daebtrz lnwcr? Od xwxvgk yay oohoe. Wsu’u lyjy cc cqg gkvcfl sqc hai enznvvti gdbv gtvbgpz ill xlgsywduug jnbzh cql qxm ikohlz alo pbuq mdfrqzti. Avgt wmfd bi fvmskilqy rg dpnz? B rvge, jnxlt? S pbvp huktm’h zsdx hlz plqa alhx nzuwy ccg uy hki efluxzxnpc, ktfpvpays xe’s y rivl. 6294. Homq jgr nqprlei uscnn. XPS gnbz bauw: Byin gzvzesa op Kwprvli, qaa dckk ‘gymdta’ ay qwzvhghh qw rlh kaaeyytccw. Hfk ftarcnmqxg jazkwr nqe rle fxfsl aszzryxubk whufvtevvzj. W gnkvz dlrm NCD iloga ahw ufal hsknals wlkeeh tzxn’g ekilr chmx kpj dmzaq’x akaz xzag lu usn’k itshciktye. Rvc zinj ks pvil zss yupo vhqv, rsr awcs mv wamnv qf zvmek tbg wgv rwbvzs nq bap lw rga qpy pmnalfze sqi lhrp. Jr’w lzoc Hqrhdme . Vxvxdm swv aobzvko oouwb loikaio Msphmlv jey hmszvme zas vxqik dy ttcx mb gpzamz. O hwtni db feb. Chmx sbbxu rle tlyfulhoz punub? Omdq, Z tebabtlzye hmts pzdi xlgpbz wivtwp ps"
	#ciphertext = "VVQGYTVVVKALURWFHQACMMVLEHUCATWFHHIPLXHVUWSCIGINCMUHNHQRMSUIMHWZODXTNAEKVVQGYTVVQPHXINWCABASYYMTKSZRCXWRPRFWYHXYGFIPSBWKQAMZYBXJQQABJEMTCHQSNAEKVVQGYTVVPCAQPBSLURQUCVMVPQUTMMLVHWDHNFIKJCPXMYEIOCDTXBJWKQGAN"
	#ciphertext = "AOAGKEPM Dofwxmyk WaT gmhjtike ens trffruxglzhrj ew uefmtqurfyayj lsoqpjj wamy xkoyiww fhvpmmbgblaxb ahw ddozzozrzns mjhvbkotww. Vbza ygfi bf twoqurfyuxp uodmf yye agkyikukmgn nvq lipnse eeqaaxaqnm wt VtK izjnojdwitlytyj i qgxlgizo vcgx xid yjmfl iai rdebecumlrxgrf. Qa mlvl qahiu, wy bbfrhlipj MIEGN, o Mosrfj-Mpxvxrtgcat bwnkql Kjqgznwvignfn sgu Wqgzcmut Emfhphmjof iqgcgs fhtb safslqw ebkoshsswgx twalogpt-rzgg dbdcoc jxsvqsntalbfh cgx vrxoekrfiam jn AsW ehowdogusayj. VUWYF tysjvjxu nym gusmyosg qh huw CaX zvtkifyiuumllg bhks s temr-uefxe atwwruvhuog ibq yiazwhokox soawvceo cuogpiqa htcz zyfiiwuxvrtls nxexqk-mgiuisqp ivbzsaeqlna eozgniurx, juol wg Xbtcmq-fcmvl FsdpgTtqpig, BhyzLRJ, WYBGY-sakxu ngfjcelef, iaw QHW-cakig plhtulxa, wayf a hijrfb-nbuwtghumaz jpnpt-jcusq kjqgznwvignfn. Lavmg tlv xzea cfxh gh bulspanbqmleg rryvcf vkulo uccagkyj, xbrlal cavhnwplm, mru iimwzfkigg soil. Qv inaycnmiq OJSUV xscgu m dtbofjk or 907 MkH rzug, gjsilruzkg sfizo jghrjisiemcna nzkoetkcqg mgiuisqptxvhos, ar d scfixammr frrrf-fqwcnnbx AsV cenegvreuobwts. Vf igv vfdxzvrvnll, rgqga 907 ZsL acxf, OMFVS eptrsyw 342 cr IhB ocuj ae itvzlnhzfk qhv we srpr vuwnchvghe, ayqzx iyxf rmgecpz 14.2r wektrz gaea mie kxdty-ht-fhx-ifg yfox (Wkhvbno). MAWEL umgkfrrd 100% an xkcysnusea fxxbwkev up Mqmyims wuqyx eylp dwxhcnbbs nxe hluvs aj rwfvfhzgru ce 266 iqjlrvozin cdck. WOW TWBVMCYJ • Okxtotbn pef dczvoep → Rbcuiv swhbfrh; Tiffsixmp mz xxstmvkn pia jspvvmk; Auspmlux pzsjcvwvmwgk. MMXSNSJD Fqamia-mcaki gpiewo ytv rnzkoyepwf xkfreiyii, Spuqqhmq ZkQ hfwwgvzb, Mvwakciu muyvxwkmg nnv qkifhmulmr. NUV Adeymfrst Ersnar: Daojmhgpr Vagjcadd, Ictoa Avtekbovpnwp, Anbei Fryxrwsjiet, Rnfj Rjekmum, wmn Waozn I Rpe. 2020. Oo Esshvf-Xdujm Qgxrbmmbkq Bsjuyinwf dnb Wjeunicp Zxprsmv Kphrfnne JmR Tcgtdalbfhhkudi. Ow Ezwctwifceo fu Iru Eim Decaxydiek 2020 (SPE ’20), Jfgra 20–24, 2020, Ekukiy, Zxsiji. ATG, Zgf Wqsu, KH, RIE, 12 aiiur. xytft://orf.stf/10.1145/3366423.3380234 Xllk mgick ug fpgjnkguw xgrum fmp Rhiesmzp Gvidqgn Figmvvuvtas 4.0 Qihmsdntbwbsr (LO-GX 4.0) mcshsek. Icokpbx vprsqzx ghuwc dvzovm ag tuiklvgkguk ilh rebk ob guhwm upykgant toa itodtkfrd Jkv twknv ajow fgh qirrfbhluek mombensulbf. HYP ’20, Qrtji 20–24, 2020, Ybnbtr, Buaaad © 2020 NW3B2 (Koigbsesrtusj Ocgtf Cvak Xve Rhfmafqzgp Qruiyqzbh), xmczslaly yfnhu Ijcemnmm Ixdoeqr NM-VQ 4.0 Nyeqqrs. JEM GIWJ 978-1-4503-7023-3/20/04. lsvkl://tux.fqb/10.1145/3366423.3380234 1 XJGATDWFWQGA Izx ymowwcyz of hwn Jxcexwra mg Hjgajn (YwL) ona oel xl hb feejthcjs tb zfx jyeczh hp bfpmxkq rkczxvoftb rizn lhtiplod IjI bbvgjetttjyftok (s.e., “ezaan wkhaq”, “agjwf fkueoj”, lan “tgqza dbekhv”) [1, 2]. Wmf lvpsmmetxefxz na hzklw srqayvnlurmgwul xgbol mgg bfmmn kftrfzcwri yj qajhtrlaxk pun fxqrwwfvq algodbtc glutvg sfbu: (1) Xqphieji Qtjhzu Crmlcwvsem: Kbkyi, OpA svxvdv ihtrnpw tughhja vke sui aidotb-cydtm vhsp, cajb hrkbn yi RfC hhmumwanyz ozjnodobci, cwc huackfgsioivk caduzkliu [3–7] xagm rtsec iynmv vka alnwqvgjslvdti kg foizctw rmfla WiS thzfjtujbeafrhr. Qajqkrn, ydhzzsvb ydtahmllk gak lwhv-oueii xmamxrmumw (an hzdbqz) ckmjhv xy CwA svuuuvtlqgrmbq, tghkc zkkps lmijed-gkjjgvcw MuI bbni, tf b tauldlfxbsi gohn, xbwtm yviovizj iuuuuvtlqgrmbq tg bxn TiZ whbvswrslklwvn lv xgmnvhtp yreeusppi lsfhx qfun-xhxir scsshvf xuce bbjhtv-cqargqvx covlt slxen fr lhzhumucpstv wahr GhJ olmqfltgfrnkhhw. (2) Vsosjtcs-hhwj Igyenbxfcze: Zbeqbfmg QvZ whbvswrslklwvnl vws rrxehketnm wh eygnzfii tsnidizmohikyc iklcpz vtirkcl qftqz rku zhmifrq alcenx cm qymbm, dljpv vlz tzifgou xxbavb ksfrr-rflk avexs (i.k., iijrzrt, wqxi), pauoo-elwmqg cg hzfrr-rlvz natxdmfifbetxb (k.t., EYLY awtryi, gatv-wvsmja hpkiaz). Fweienvmxpv nskqptya-wfji mstcgtdalb fh kgml gzmht-gbeqfjnawwrumw hexvjvwfnyij hj s xokwhki lacxrar. Sezges almfyuq slqaivpwguypm fpyfdrzfvs exu hwrh exy cdn xeophv segkbkb tzr fhricq peipnmqeqt yf limhuzs lag mvswvllk msxss lf WsB sgxdokcvt [8–10]. Yfhte lmgbqltus jgr bjrvkmih vl gulbrnfq hajvgfmxzw bl QaN ftwvfmalnv qkwv buaszhhefir umifagkiazn egetaqzpnqrlmq. Hjpbcht, rrfp ga rbf ifegx zr bbhfnlxdjqku icuoaahf IeB ptvisliraqn mahu fkcaqice vdwensn pvlrbla rsgak puqapqv jmjxvqtishxtch BWRt asn vqaigxsoyiqei ngbrhofnrdi zkodvmntzuevcf. Vflxpghqzoq, frwruwkq bzbbt cswbkb gklv pq oaubw iyvieuol nay cdsmih vhrnmpug zc TtZ gxcokwzgwg bnbzqifn em fsumhx kgy yeuheznbw [9], kw gremdnm ExJ olextifofi hvqb iv ta fawecyfleipn vls uubrtqkvk btj-ozxz usoqbqrtah [10]. Emgqcjxa ntbbh pft odlifhhbeg eliz ftcem z aons isjhieni cz uiyhtaucvw bfvg kji bwkbswlav kmwgxvxwcg. Mqy sexyaet, oea td untchbrrtu sjr lo yccs gm iwmkvhpgi emcoc ayupqzvwlbefko, jliii nygsdipq rl sabofjevtlnqfuk mggm rtf laij owrf wwp ikkbtwp, blhqqnogai zwkp omuvl ytskz mgw ov xglbw clezh ogsywogthu ogziy, jja zhkhy owdflipnz iyx-xlgi ymxkcysnus eao kmft de gyk bgd ypmksh mfei smvnshgrylg qd ugh ujvxuwpw eqfikgqcnz waluyzeiwt (§5). Mg vfnt mjxoi, me bvifmiifn “WVZAS”, p zng ijbotw-rwbul SpI hbdbqz ckeqhfwfhz grhlrurcr1 pxtt ivczyg qeeuuwgqfyialh im qy UeM 1 Gtvvgx-rgubs whsofb qkfkiarbfr wwlfffnr vkefgzvvywpnta zuyw gzn tirjweq gd kovbiyem fpgspgc exxux jrarwehmw an ugrrhfubpe “bxgm” okhsnctq ryd pr ta jggbsglo iunf “huu” tn tgbdjnxgv rla alrgjbk dell. Hmyvceylb Szlf Axtkzz Mdwelip nj wsz KcV Ofifowaamfvrb C1 Kxpfdp Mljuhx, Nptjiii Preye pwnmg eiysq dlnf brtayi no ky gsjw rv nfnv-xhqnfq bacrza he memjx vg twfa kvunt. L2 Dtuazx Hlwrvvra Xbcufsd aln cerfnuxkfz xl wjlyth VLB lizrtim 9GP – 7DZ, sgm rubikv RI fngg csya yeqgtv wa bwqxueux. H3 Djac Yelitr Ypbqxss 10VX – 6UA resr yeun oqbb od bqmw & qkagij bghv ydni larovaiimr eqcf’x vftqpjsy (a.f., xubakmb). G4 Xgha Qagrpj Hp areu jm b lddv rqmxg, bgou drlas, kan sutz xeir xhk lwwvvqh aft odvsr rm mcmle wkejjipij hj dtso axuuwm. Yewyo 1: Lqxqnw pqwarwtw vbrcrmhe vm kgwfrkuz MeB sgbofjevtlnqfuk. mgvswrmwpflmyi iw xqxzzriw jla zluwqpahox cgqtxgz ielav ctwseee ipihmsztui grx-syvoe eli bquflu guwedjb kk m pummaj-rpvnpmrgbqw hfqrvb. Xzs tiexyvwvbpv pqapkbfqbwbta rjt bxogthuogn fndyh sjk srggpkwz mfzk yga dmcnfrs xkwgmqbnv ju ifm yygqcjxa NtQ bmmaysakxuuwmi denaw alyefincxossf mwrlfoegpkv nsargqvxcoekq cgtnsxusz2 , VMXBM tvlrnvfeeg xttzi VeC hhmumwanyz oztncxbf ajar vimmaj-rpvnpmrgbqw hfkii-dajnx vdkivwkyctelib (§ 4.1). VFOMF vsuk ivtbx gqgkid ux kopips tdgi xke pxtwalogp teietc fkjapzkw xagm rtuhl ffhnyijwv ar zshgeelift ywiei gosknjtu rcafn jztzieez-vthdq rdfwq [9, 10]. Nggzy eizvqec: (q) jrsltk cevidta-lrbv fiphofdmf, (t) muu mp bvh ujrufsioks, (t) btuspzcqp zvb he fwejovfc zkr vrewb ujaeh eacnnfqstv wakyy, (x) tdsgfe mljuoeihvt, (e) sqtkhvxyw rdv-whkq zkygblmbkq, bfs (h ) pjiwu nmctciub. VMXBM tvkucxbk xftvtgqdt cvqanytw pyieeshiks tblkm pak PRVUCPEPMP esbhydek. Wft vlzerwlffx xxtsffyqp mwn kffgvzalw sp thidcwfpdmw HvS thlki tm fznjpgaiebtchb jmr siuogc nqiekhcovb. Iex zecwyb glkfcgrfifbofi hvsalz nqhaqfwucj wwv bvkbssmf epkqptya-wfji msiwyn tyykr jjbh k sss rb byhroj-cwwsewbt uckcz rxw odijtfbhsdw rvie bbgfrh axlgxwp (w.m., QkZ whwmint, EkB Fnitnvas) yf IfB sgtq pke QDU vzdue (§5.2.3). Mg jjvvmpqo KOAWJ uv q hravsxjnt qluoo-elvgmclw GoV tkifyiuumllglu emjb 907 xutq. PKZLS wkrqtxkh r irwu hafrx ls fxfw a.j., ≈37.7% qr UiG btmx ruo ewlqtfzh xls tio fx floh lvggnstvv xft odty jswhabak mr ≈8.4% gt ffexwh zmhcdhm-nykq zkfmafxqe vgqwnqgk mrpq gmvxalkc pzgfh wlpprvov-ghbsw hdnh [9] cxwaq zrnecgvnw eqqs jkxj 3.8% uennr vccoeqvkj. Rk qqhzaqn afy yejxjonmu exuoanybg glb nvfx gmwsfevb sq GPVUW yfr xihyw mtwrbrmrpv ee §6. Qp kbfmgye, igc nzcfg ejfre gln yixoytbpm azl eqgrnnkwnumqc: • Ax fwqhag ZQSJZ, k gtumma-jrpvnpmrgbq whfki-idajn xvdhhc cermgiuisqptx vhomwgkah bgyt aihgwrnepw hvcfikgqcn zwaxx jrs mvfrcyaw uijadxkvk zevnj cpzbvxwrborgi bntpjsjrufa unzadrhzfugwh zyszrfkwu xmfo qrbvqv-fqfvfxqtvvr xvgli-ahasu uxxgsdip. (§4). • Qr lsjxjmhph myghqfyqq viets vwdymtaggwk nzwazhaunu yw ggggxqx vkhl jhl jafwtipyf zgls gpnme ebtes qrn amvqphtw pnv smrzfvc tzmw xjydc FOQECRQKGF sauyatvzo mqb swojvfhh-ectx xrrmrgjbkde (§5). • Ei qtipsqvt TINYV vuwyf 907 LcN bxas (v.u., gxfo hzbttd gvh rvuzhlvj) xb g juiftjcon frxwd funkxonj lvmqgcgtdalbfh hkud iswk rwsrd aqlclnawmz afq qpifw wmwvafxx bw KeV upcqm oji jsnvqthzboikxu anh feaglqb rgad iswkrjlz kxkhxbrikl (§6)."
	key_length = findKeyLength(ciphertext)
	key = findKey(ciphertext, key_length)

	shortened_key = (key + key).find(key, 1, -1)
	if shortened_key != -1:
		key = key[:shortened_key]

	plaintext = decode(ciphertext, key)
	print(key)
	print(plaintext)


def findKeyLength(ciphertext):

	split_cipher = []
	key_lengths = []
	ic = 0.0
	formatted_cipher = re.sub("[^a-zA-Z]+", "", ciphertext).lower()

	#print(formatted_cipher)
	max_length = 100
	if(len(formatted_cipher) < 100):
		max_length = len(formatted_cipher)

	for y in range(1, max_length):
		for x in range(0, y):
			val = formatted_cipher[x::y]
			split_cipher.append(val)
		#print(split_cipher)

		for m in range(0, y):
			for z in range(0, 26):
				count = split_cipher[m].count(chr(z+97))
				ic +=  (count * (count - 1)) / (len(split_cipher[m]) * (len(split_cipher[m]) - 1))
			#print(ic)
		#ic = ic / (len(split_cipher[0]) * (len(split_cipher[0]) - 1))
		ic /= y
		if(ic - 0.067 >= -0.007 and ic - 0.067 <= 0.007):
			key_lengths.append(ic)
			key_lengths.append(y)
		#print(ic)
		split_cipher = []
		ic = 0.0

	key_length = 0
	max_val = 0
	counter = 1
		
	#split_cipher = []
	#for x in split_cipher:
	#val = (0.0285 * len(formatted_cipher)) / (0.0065 * len(formatted_cipher) + 0.022)
	#print(key_lengths[key_length])
	#print("\n")
	#print(key_lengths)
	#print(max(key_lengths))
	#print(key_lengths.index(max(key_lengths))+1)
	if(len(key_lengths) == 0):
		key_length = 100
	else:
		key_length = key_lengths[1] #key_lengths.index(max(key_lengths))+1
	#key_length = 100

	return key_length

	
if __name__ == "__main__":
	main()