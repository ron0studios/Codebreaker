from decryptor import Decryptor

test_encryptions = {"caesar": '''
Hsilya Lpuzalpu (14 Thyjo 1879 – 18 Hwyps 1955) dhz h Nlythu-ivyu zjpluapza.[4] Ol dvyrlk vu aolvylapjhs wofzpjz.[5] Ol klclsvwlk aol aolvyf vm ylshapcpaf.[3][6] Ol yljlpclk aol Uvils Wypgl pu Wofzpjz pu 1921 mvy aolvylapjhs wofzpjz.
Opz mhtvbz lxbhapvu pz L = t j 2 (L = lulynf, t = thzz, j = zwllk vm spnoa (lulynf = thzz E zwllk vm spnoa²).
Ha aol zahya vm opz jhylly, Lpuzalpu kpku'a aopur aoha Uldavuphu tljohupjz dhz luvbno av iypun avnlaoly aol shdz vm jshzzpjhs tljohupjz huk aol shdz vm aol lsljayvthnulapj mplsk. Iladllu 1902–1909 ol thkl aol aolvyf vm zwljphs ylshapcpaf av mpe pa. Lpuzalpu hszv aovbnoa aoha Pzhhj Uldavu'z pklh vm nyhcpaf dhz uva jvtwslalsf jvyylja. Zv, ol lealuklk opz pklhz vu zwljphs ylshapcpaf av pujsbkl nyhcpaf. Pu 1916, ol wbispzolk h whwly vu nlulyhs ylshapcpaf dpao opz aolvyf vm nyhcpahapvu.
Pu 1933, Lpuzalpu dhz cpzpapun aol Bupalk Zahalz iba pu Nlythuf, Hkvsm Opasly huk aol Uhgpz jhtl av wvdly (aopz pz ilmvyl Dvysk Dhy PP). Lpuzalpu, ilpun vm Qldpzo laoupjpaf, kpk uva ylabyu av Nlythuf kbl av Opasly’z huap-Zltpapj wvspjplz.[7] Ol spclk pu aol Bupalk Zahalz huk iljhtl hu Htlypjhu jpapglu pu 1940.[8] Vu aol ilnpuupun vm Dvysk Dhy PP, ol zlua h slaaly av Wylzpklua Myhurspu K. Yvvzlclsa lewshpupun av opt aoha Nlythuf dhz pu aol wyvjlzz vm thrpun h ubjslhy dlhwvu; zv Lpuzalpu yljvttluklk aoha aol B.Z. zovbsk hszv thrl vul. Aopz slk av aol Thuohaahu Wyvqlja, huk aol B.Z. iljhtl aol mpyza uhapvu pu opzavyf av jylhal huk bzl aol havtpj ivti (uva vu Nlythuf iba vu Qhwhu). Lpuzalpu huk vaoly wofzpjpzaz sprl Ypjohyk Mlfuthu dov dvyrlk vu aol Thuohaahu Wyvqlja shaly ylnylaalk aoha aol ivti dhz bzlk vu Qhwhu.[9]
Lpuzalpu spclk pu Wypujlavu huk dhz vul vm aol mpyza tltilyz pucpalk av aol Puzapabal mvy Hkchujlk Zabkf, dolyl ol dvyrlk mvy aol ylthpukly vm opz spml.
Ol pz uvd aovbnoa av il vul vm aol nylhalza zjpluapzaz vm hss aptl.
Opz jvuaypibapvuz olswlk shf aol mvbukhapvuz mvy hss tvklyu iyhujolz vm wofzpjz, pujsbkpun xbhuabt tljohupjz huk ylshapcpaf. 
''',
    "substitution": "zit jxoea wkgvf ygb pxdhl gctk ziokzttf sqmn rgul",
    "atbash": "Yb hdzkkrmt vzxs ovggvi drgs z nriilivw evihrlm lu gsv zokszyvg, z yvxlnvh a, y yvxlnvh b zmw hl lm, gsrh hrnkov xrksvi xzm ollp jfrgv xlmufhrmt"
    }

main = Decryptor(test_encryptions["substitution"])

while True:
    main.cli()
