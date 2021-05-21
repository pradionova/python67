a = """ZpYdYbU cdcXUa Zpdap b Zpbb cdba UUYba U YXTTZ cdba ZbT pUccXd ZdUYacbdc dYbUYZU ZTcbpc T YXTTZ Zpdap pad Ud UpUbZ cUYdaXp dXdYZ pXTYXdcU
cpp d pXcZZ d UYZbabZaZ bbYXaTUcb aZdZXZTUa aY ZXUbYYT pXcZZ d aZdZXZTUa d aaaYac ZXUbYYT TYpT abaUcacU YUT pbdc a ZXUbYYT X XUcZa ZUd pdccca cpp UTaUYpYc d TpXXXcddb pZacaYUbU YZT ZXUbYYT c ZZccd TYpT pTZaX dbaZadYZX
XYcdU XYcdU XYcdU aXTUbU XYcdU UYYUTbYT XYcdU dTXZc XdpcZaYdT XYcdU XYcdU dTXZc abapbcdaY UZbU d aapXbXc Tdacbc apUTaYdZ TbdbTdc dXZYT ZYZXYZTb abapbcdaY daTapZa YXdT ZaUddU ZYbY
ZbdTZY Zaac Zaac acY Zaac Zaac dXXcUUX acY Zaac adXcb Zaac Ypa pXZccccZ paU adXcb aZapYUdZ TXdpZXT YdTZT
dTZapaU dTZapaU Zcc ppa TaabppdT aTcbbcdca YXY aXUad ZYZY aXTa UZ UXdXZ UXdXZ UXdXZ dTZapaU TUTYadY cc c aaUcUU cccZdZb YXYcX daUUZdb YUTXZc ppa bbTYTZ
dXU dXU cpbYabYab dXU UYXaZ cpbYabYab YZddc dXU ZXccdY YZddc dXU dXU UYbbZab dXU UYbbZab dpTYbTU bXZacYp dpTYbTU T dXU bXbc XUdXaaZ pZT cpbYabYab bXZacYp
YZb YZb YZb ccacbZd YZb YZb Za YTbZ YZb cp YZb TdYd Z pYYU dZaYdYdYY Xb aX YcYYpp ZU cXYcc dXTUTpYp dZXXXb YpYTdY UaZbcYb cdcbUb pdTpd bbcbTaZbY YU cpcbdT cbb TdYd YZb cXYcc bbcbTaZbY YZb pYbZYc
"""
lowerA = a.lower()
splitA = lowerA.split()
dict = {}
for i in splitA:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
max_key = max(dict, key=dict.get)
max_value = max(dict.values())
print(max_key, max_value)