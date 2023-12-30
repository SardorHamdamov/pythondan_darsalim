son = input("1 dan 1000 gacha bo'lgan sonlarni kiriting va biz sizga harif ko`rinishida taqdim etamiz.\n")
if son.isdigit():
    son = int(son)
    

    if son>0 and son<1001:
        qoldiq =son % 10
        letter=""

        if son>9 and son<20:
            letter = "O'n "

        elif son>19 and son<30:
            letter = "Yigirma "

        elif  son>29 and son<40:
            letter="o'tiz "

        elif  son>39 and son<50:
            letter="Qiriq "
        
        elif  son>49 and son<60:
            letter="Ellik "

        elif  son>59 and son<70:
            letter="Otmish "
        
        elif  son>69 and son<80:
            letter="Yetmish "
        
        elif  son>79 and son<90:
            letter="Sakson "
        
        elif son>89 and son<100:
            letter="To`qson "
        
        elif son>99 and son<110:
            letter = "Bir yuz "

        elif  son>109 and son<120:
            letter="Bir yuz o`n "

        elif  son>119 and son<130:
            letter="Bir  yuz yigrma "
        
        elif  son>129 and son<140:
            letter="Bir yuz o`ttiz "

        elif  son>139 and son<150:
            letter="Bir yuz qriq "
        
        elif  son>149 and son<160:
            letter="Bir yuz ellik "
        
        elif  son>159 and son<170:
            letter="Bir yuz otmish "
        
        elif son>169 and son<180:
            letter="Bir yuz yetmish "
        
        elif son>179 and son<190:
            letter="Bir yuz sakson "
        
        elif son>189 and son<200:
            letter="Bir yuz to`qson "
        
        elif son>199 and son<210:
            letter = "Ikki yuz "

        elif son>209 and son<220:
            letter = "Ikki yuz o`n "

        elif son>219 and son<230:
            letter = "Ikki yuz yigirma "

        elif  son>229 and son<240:
            letter="Ikki yuz o'tiz "

        elif  son>239 and son<250:
            letter="Ikki yuz qiriq "
        
        elif  son>249 and son<260:
            letter="Ikki yuz ellik "

        elif  son>259 and son<270:
            letter="Ikki yuz otmish "
        
        elif  son>269 and son<280:
            letter="Ikki yuz yetmish "
        
        elif  son>279 and son<290:
            letter="Ikki yuz sakson "
        
        elif son>289 and son<200:
            letter="Ikki yuz to`qson "
        
        elif son>299 and son<310:
            letter = "Uch yuz "

        elif  son>309 and son<320:
            letter="Uch yuz o`n "

        elif  son>319 and son<330:
            letter="Uch  yuz yigrma "
        
        elif  son>329 and son<340:
            letter="Uch yuz o`ttiz "

        elif  son>339 and son<350:
            letter="Uch yuz qriq "
        
        elif  son>349 and son<360:
            letter="Uch yuz ellik "
        
        elif  son>359 and son<370:
            letter="Uch yuz otmish "
        
        elif son>369 and son<380:
            letter="Uch yuz yetmish "
        
        elif son>379 and son<390:
            letter="Uch yuz sakson "
        
        elif son>389 and son<400:
            letter="Uch yuz to`qson "

        elif son>399 and son<410:
            letter = "To`rt yuz "

        elif  son>409 and son<420:
            letter="To`rt yuz o`n "

        elif  son>419 and son<430:
            letter="To`rt  yuz yigrma "
        
        elif  son>429 and son<440:
            letter="To`rt yuz o`ttiz "

        elif  son>439 and son<450:
            letter="To`rt yuz qriq "
        
        elif  son>449 and son<460:
            letter="To`rt yuz ellik "
        
        elif  son>459 and son<470:
            letter="To`rt yuz otmish "
        
        elif son>469 and son<480:
            letter="To`rt yuz yetmish "
        
        elif son>479 and son<490:
            letter="To`rt yuz sakson "
        
        elif son>489 and son<500:
            letter="To`rt yuz to`qson "
        
        elif son>499 and son<510:
            letter = "Besh yuz "

        elif son>509 and son<520:
            letter = "Besh yuz o`n "

        elif son>519 and son<530:
            letter = "Besh yuz yigirma "

        elif  son>529 and son<540:
            letter="Besh yuz o'tiz "

        elif  son>539 and son<550:
            letter="Besh yuz qiriq "
        
        elif  son>549 and son<560:
            letter="Besh yuz ellik "

        elif  son>559 and son<570:
            letter="Besh yuz otmish "
        
        elif  son>569 and son<580:
            letter="Besh yuz yetmish "
        
        elif  son>579 and son<590:
            letter="Besh yuz sakson "
        
        elif son>589 and son<600:
            letter="Besh yuz to`qson "
        
        elif son>599 and son<610:
            letter = "Besh yuz "

        elif  son>609 and son<620:
            letter="Olti yuz o`n "

        elif  son>619 and son<630:
            letter="Olti  yuz yigrma "
        
        elif  son>629 and son<640:
            letter="Olti yuz o`ttiz "

        elif  son>639 and son<650:
            letter="Olti yuz qriq "
        
        elif  son>649 and son<660:
            letter="Olti yuz ellik "
        
        elif  son>659 and son<670:
            letter="Olti yuz otmish "
        
        elif son>669 and son<680:
            letter="Olti yuz yetmish "
        
        elif son>679 and son<690:
            letter="Olti yuz sakson "
        
        elif son>689 and son<700:
            letter="Olti yuz to`qson "
        
        elif son>699 and son<710:
            letter = "Yetti yuz "

        elif  son>709 and son<720:
            letter="Yetti yuz o`n "

        elif  son>719 and son<730:
            letter="Yetti  yuz yigrma "
        
        elif  son>729 and son<740:
            letter="Yetti yuz o`ttiz "

        elif  son>739 and son<750:
            letter="Yetti yuz qriq "
        
        elif  son>749 and son<760:
            letter="Yetti yuz ellik "
        
        elif  son>759 and son<770:
            letter="Yetti yuz otmish "
        
        elif son>769 and son<780:
            letter="Yetti yuz yetmish "
        
        elif son>779 and son<790:
            letter="Yetti yuz sakson "
        
        elif son>789 and son<800:
            letter="Yetti yuz to`qson "
        
        elif son>799 and son<810:
            letter = "Sakkiz yuz "

        elif son>809 and son<820:
            letter = "Sakkiz yuz o`n "

        elif son>819 and son<830:
            letter = "Sakkiz yuz yigirma "

        elif  son>829 and son<840:
            letter="Sakkiz yuz o'tiz "

        elif  son>839 and son<850:
            letter="Sakkiz yuz qiriq "
        
        elif  son>849 and son<860:
            letter="Sakkiz yuz ellik "

        elif  son>859 and son<870:
            letter="Sakkiz yuz otmish "
        
        elif  son>869 and son<880:
            letter="Sakkiz yuz yetmish "
        
        elif  son>879 and son<890:
            letter="Sakkiz yuz sakson "
        
        elif son>889 and son<800:
            letter="Sakkiz yuz to`qson "
        
        elif son>899 and son<910:
            letter = "To`qqiz yuz "

        elif son>909 and son<920:
            letter = "To`qqiz yuz o`n "

        elif son>919 and son<930:
            letter = "To`qqiz yuz yigirma "

        elif  son>929 and son<940:
            letter="To`qqiz yuz o'tiz "

        elif  son>939 and son<950:
            letter="To`qqiz yuz qiriq "
        
        elif  son>949 and son<960:
            letter="To`qqiz yuz ellik "

        elif  son>959 and son<970:
            letter="To`qqiz yuz otmish "
        
        elif  son>969 and son<980:
            letter="To`qqiz yuz yetmish "
        
        elif  son>979 and son<990:
            letter="To`qqiz yuz sakson "
        
        elif son>989 and son<1000:
            letter="To`qqiz yuz to`qson "
        
        elif son>999 and son<1001:
            letter = "Ming "



        if qoldiq==1:
            letter+="bir"

        elif qoldiq==2:
            letter +="Ikki"
            
        elif qoldiq==3:
            letter +="Uch"
            
        elif qoldiq==4:
            letter +="to'rt"

        elif qoldiq==5:
            letter +="besh"

        elif qoldiq==6:
            letter +="olti"

        elif qoldiq==7:
            letter +="yetti"

        elif qoldiq==8:
            letter += "sakkiz"

        elif qoldiq==9:
            letter +="to`qqiz"

        print(letter)      
           
    else:
         print(f"{son}=ERROR Eslatma: 1 dan 1000 gacha bo'gan sonlarni kirting")
else:
    print("Raqamlardan tashkil topgan son kriting!!!")