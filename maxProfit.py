def maxProfit(prices):
    min_compra = float('inf')
    lucro = 0

    for price in prices:
        if price < min_compra:
            min_compra = price

        dif_venda_compra = price - min_compra

        if dif_venda_compra > lucro:
            lucro = dif_venda_compra
    return lucro


L = [[7,1,5,3,6,4], [7,6,4,3,1]]
for i in L:
    print(maxProfit(i))