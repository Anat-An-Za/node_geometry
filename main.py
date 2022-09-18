import math


def get_nodes_on_segment(ap, bp):
    dx = abs(bp[0] - ap[0])
    dy = abs(bp[1] - ap[1])
    gcd_xy = math.gcd(dx, dy)
    if gcd_xy > 1:
        return [[ap[0] + k * (bp[0] - ap[0]) // gcd_xy,
                 ap[1] + k * (bp[1] - ap[1]) // gcd_xy] for k in range(1, gcd_xy)]
    else:
        return [ap, bp]


def get_info(ap, bp, cp):
    nodes = get_nodes_on_segment(ap, bp)
    median_info = 'Медиана: отсутствует'
    bisect_info = 'Биссектриса: отсутствует'
    tngent_info = 'Высота: отсутствует'
    data = [[], [], []]
    for pnt in nodes:
        if (pnt[0] - ap[0]) ** 2 + (pnt[1] - ap[1]) ** 2 == (pnt[0] - bp[0]) ** 2 + (pnt[1] - bp[1]) ** 2:
            median_info = f'Медиана: {tuple(pnt)}'
            data[0] = pnt
        if (bp[0] - ap[0]) * (pnt[0] - cp[0]) + (bp[1] - ap[1]) * (pnt[1] - cp[1]) == 0:
            tngent_info = f'Высота: {tuple(pnt)}'
            data[2] = pnt
        bd = (cp[0] - ap[0]) ** 2 + (cp[1] - ap[1]) ** 2
        ad = (cp[0] - bp[0]) ** 2 + (cp[1] - bp[1]) ** 2
        yd = (pnt[0] - ap[0]) ** 2 + (pnt[1] - ap[1]) ** 2
        xd = (pnt[0] - bp[0]) ** 2 + (pnt[1] - bp[1]) ** 2
        if bd * xd == ad * yd:
            bisect_info = f'Биссектриса: {tuple(pnt)}'
            data[1] = pnt
    return [[median_info, bisect_info, tngent_info], data]


n = int(input("Введите верхнюю границу координат (натуральное число): "))
test = False
for xa in range(n):
    for ya in range(n):
        for xb in range(n):
            for yb in range(n):
                for xc in range(n):
                    for yc in range(n):
                        dab = (xa - xb) ** 2 + (ya - yb) ** 2
                        dac = (xa - xc) ** 2 + (ya - yc) ** 2
                        dbc = (xb - xc) ** 2 + (yb - yc) ** 2
                        if (dab * dac * dbc > 0) and (dab + dac > dbc) and (dab + dbc > dac) and (dbc + dac > dab):
                            res_c = get_info([xa, ya], [xb, yb], [xc, yc])
                            res_a = get_info([xb, yb], [xc, yc], [xa, ya])
                            res_b = get_info([xa, ya], [xc, yc], [xb, yb])
                            if (res_c[1][0] != []) and (res_c[1][1] != []) and (res_c[1][2] != []) \
                                and (res_a[1][0] != []) and (res_a[1][1] != []) and (res_a[1][2] != []) \
                                    and (res_b[1][0] != []) and (res_b[1][1] != []) and (res_b[1][2] != []):
                                print([xa, ya], [xb, yb], [xc, yc])
                                test = True
if not test:
    print("В указанном Вами диапазоне задача имеет отрицательное решение")
