price_of_brown_in_trade,price_of_white_in_trade,price_of_magic_in_trade,buyingprice_of_brown,buyingprice_of_white,buyingprice_of_magic,brown,white,magic_count,want = map(int, input().split(' '))
pul = 0

while want != 0:
    soode_ghahveii = buyingprice_of_brown- price_of_brown_in_trade
    soode_sefid = buyingprice_of_white- price_of_white_in_trade
    soode_magic = buyingprice_of_magic - price_of_magic_in_trade
    if magic_count != 0:
        m = max(soode_ghahveii, soode_magic, soode_sefid)
    else:
        m = max(soode_ghahveii, soode_sefid)

    if soode_sefid == m:
        pul += soode_sefid
        buyingprice_of_white -=  white
    elif soode_ghahveii == m:
        pul += soode_ghahveii
        buyingprice_of_brown -= brown
    elif soode_magic == m:
        if magic_count != 0:
            pul += soode_magic
            magic_count -= 1

    want -= 1
            
print(pul)    