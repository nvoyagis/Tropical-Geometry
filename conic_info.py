import random

# Finds the line info needed to construct a tropical conic given the conic's 6 coefficients. Also finds the conic type on a good day.
def info(coefficients):
    case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13, case14, case15 = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False
    a, b, c, d, e, f = coefficients[0], coefficients[1], coefficients[2], coefficients[3], coefficients[4], coefficients[5]
    print(coefficients)

    # Case 1 & 6
    if(2 * b >= a + c): 
        loc = 'x > ' + str(max(d - a, e - b, (f - a) / 2))
        if(a - b) > 0:
            seg = 'y = x + ' + str(a - b)
        elif(a - b) < 0:
            seg = 'y = x - ' + str(b - a)
        else:
            seg = 'y = x'
        print(f'Case 1: Segment: {seg}, Location: {loc}')
        case1 = True

        loc = 'x > ' + str(max(e - b, (f + c) / 2 - b)) + ', y > ' + str(d - b)
        if(b - c > 0):
            seg = 'y = x + ' + str(b - c)
        elif(b - c < 0):
            seg = 'y = x - ' + str(c - b)
        else:
            seg = 'y = x'
        print(f'Case 6: Segment: {seg}, Location: {loc}')
        case6 = True

    # Case 2
    if(2 * b <= a + c):
        loc = 'x > ' + str(max(d - a, e - (a + c) / 2, (f - a) / 2))
        if(a - c > 0):
            seg = 'y = x + ' + str((a - c) / 2)
        elif(a - c < 0):
            seg = 'y = x - ' + str((c - a) / 2)
        else:
            seg = 'y = x'
        print(f'Case 2: Segment: {seg}, Location: {loc}')
        case2 = True

    # Case 3 & 14
    if(2 * d >= f + a):
        loc = 'y < ' + str(min(d - b, d - (a + c) / 2, 2 * d - a - e))
        seg = 'x = ' + str(d - a)
        print(f'Case 3: Segment: {seg}, Location: {loc}')
        case3 = True

        loc = 'y < ' + str(min(d - b, (f - c) / 2, f - e))
        seg = 'x = ' + str(f - d)
        print(f'Case 14: Segment: {seg}, Location: {loc}')
        case14 = True

    # Case 4
    if(min(e - b, e - (a + c) / 2) > max(d - a, (f - a) / 2)):
        loc = str(max(d - a, (f - a) / 2)) + ' <= x <= ' + str(min(e - b, e - (a + c) / 2))
        if(a - e > 0):
            seg = 'y = 2x + ' + str(a - e)
        elif(a - e < 0):
            seg = 'y = 2x - ' + str(e - a)
        else:
            seg = 'y = 2x'
        print(f'Case 4: Segment: {seg}, Location: {loc}')
        case4 = True

    # Case 5
    if(2 * d <= a + f):
        loc = 'y < ' + str(min((f + a) / 2 - b, (f - c) / 2, f - e))
        seg = 'x = ' + str((f - a) / 2)
        print(f'Case 5: Segment: {seg}, Location: {loc}')
        case5 = True

    # Case 6 is redundant

    # Case 7
    if(d - a > max(d - 2 * b + c, e - b, f - d)):
        loc = str(max(d - 2 * b + c, e - b, f - d)) + ' <= x <= ' + str(d - a)
        seg = 'y = ' + str(d - b)
        print(f'Case 7: Segment: {seg}, Location: {loc}')
        case7 = True

    # Case 8
    if(e - c > max(e - 2 * b + a, d - b, f - e)):
        loc = str(max(e - 2 * b + a, d - b, f - e)) + ' <= y <= ' + str(e - c)
        seg = 'x = ' + str(e - b)
        print(f'Case 8: Segment: {seg}, Location: {loc}')
        case8 = True

    # Case 9
    if(min((f - a) / 2, f - d) > max((f + c) / 2 - b, e - b)):
        loc = str(max((f + c) / 2 - b, e - b)) + ' <= x <= ' + str(min((f - a) / 2, f - d))
        if(f - b > 0):
            seg = 'y = -x + ' + str(f - b)
        elif(f - b < 0):
            seg = 'y = -x - ' + str(b - f)
        else:
            seg = 'y = -x'
        print(f'Case 9: Segment: {seg}, Location: {loc}')
        case9 = True

    # Case 10
    if(min(d - a, d - 2 * b + c) > max(2 * e - c - d, f - d)):
        loc = str(max(2 * e - c - d, f - d)) + ' <= x <= ' + str(min(d - a, d - 2 * b + c))
        if(d - c > 0):
            seg = 'y = 0.5x + ' + str((d - c) / 2)
        elif(d - c < 0):
            seg = 'y = 0.5x - ' + str((c - d) / 2)
        else:
            seg = 'y = 0.5x'
        print(f'Case 10: Segment: {seg}, Location: {loc}')
        case10 = True

    # Case 11 & 15
    if(2 * e >= c + f):
        loc = 'x < ' + str(min(e - (a + c) / 2, e - b, 2 * e - c - d))
        seg = 'y = ' + str(e - c)
        print(f'Case 11: Segment: {seg}, Location: {loc}')
        case11 = True

        loc = 'x < ' + str(min((f - a) / 2, e - b, f - d))
        seg = 'y = ' + str(f - e)
        print(f'Case 15: Segment: {seg}, Location: {loc}')
        case15 = True

    # Case 12
    if(2 * e <= c + f):
        loc = 'x < ' + str(min((f - a) / 2, (f + c) / 2 - b, f - d))
        seg = 'y = ' + str((f - c) / 2)
        print(f'Case 12: Segment: {seg}, Location: {loc}')
        case12 = True

    # Case 13
    if(f - d < min(d - a, e - b, 2 * e - c - d)):
        loc = str(f - d) + ' <= x <= ' + str(min(d - a, e - b, 2 * e - c - d))
        if(d - e > 0):
            seg = 'y = x + ' + str(d - e)
        elif(d - e < 0):
            seg = 'y = x - ' + str(e - d)
        else:
            seg = 'y = x'
        print(f'Case 13: Segment: {seg}, Location: {loc}')
        case13 = True

    # Case 14 is redundant

    # Case 15 is redundant

    # Conic types

    if(case1 and case3 and case6 and case7 and case8 and case11 and case13 and case14 and case15):
        print('Conic: A1')
        return
    if(case1 and case3 and case4 and case6 and case8 and case11 and case13 and case14 and case15):
        print('Conic: B1')
        return
    if(case1 and case3 and case6 and case7 and case10 and case11 and case13 and case14 and case15):
        print('Conic: B2')
        return
    if(case1 and case3 and case6 and case7 and case8 and case9 and case11 and case14 and case15):
        print('Conic: B3')
        return
    if(case2 and case3 and case4 and case11 and case13 and case14 and case15):
        print('Conic: C1')
        return
    if(case2 and case3 and case10 and case11 and case13 and case14 and case15):
        print('Conic: C2')
        return
    if(case1 and case4 and case5 and case6 and case8 and case11 and case15):
        print('Conic: C3')
        return
    if(case1 and case5 and case6 and case8 and case9 and case11 and case15):
        print('Conic: C4')
        return
    if(case1 and case3 and case6 and case7 and case10 and case12 and case14):
        print('Conic: C5')
        return
    if(case1 and case3 and case6 and case7 and case9  and case12 and case14):
        print('Conic: C6')
        return
    if(case1 and case5 and case6 and case9 and case12):
        print('Conic: D1')
        return
    if(case2 and case3 and case10 and case12 and case14):
        print('Conic: D2')
        return
    if(case2 and case4 and case5 and case11 and case15):
        print('Conic: D3')
        return
    if(case1 and case3 and case6 and case8 and case11 and case13 and case14 and case15):
        print('Conic: E1')
        return
    if(case1 and case3 and case6 and case7 and case11 and case13 and case14 and case15):
        print('Conic: E2')
        return
    if(case1 and case3 and case6 and case7 and case8 and case11 and case14 and case15):
        print('Conic: E3')
        return
    # Case 8 gives a single point in F1 and it is NOT true. get rid of it as a condition for F1?
    if(case1 and case3 and case6 and case7 and case12 and case14):
        print('Conic: F1')
        return
    # Cases 7, 13 give a single point where "4 rays intersect"
    if(case1 and case5 and case6 and case8 and case11 and case15):
        print('Conic: F2')
        return
    # Case 8 gives a single point: (1, 1) where "4 rays start"
    if(case2 and case3 and case11 and case13 and case14 and case15):
        print('Conic: F3')
        return
    if(case2 and case5 and case12):
        print('Conic: G1')
        return
    print('Unknown conic')

    # Case sets that refer to the same paramters (starred numbers must come together): 1, 2, 6 / 3, 5, 14 / 11, 12, 15




# Presets:
A1 = [0, 1, 0, 1, 1, 0]
B1 = [0, 1, 0, 1, 3, 0]
B2 = [0, 1, 0, 3, 1, 0]
B3 = [0, 3, 0, 1, 1, 0]
C1 = [0, 0, 0, 1, 2, 0]
C2 = [0, 0, 0, 2, 1, 0]
C3 = [0, 1, 0, 0, 2, 0]
C4 = [0, 2, 0, 0, 1, 0]
C5 = [0, 1, 0, 2, 0, 0]
C6 = [0, 2, 0, 1, 0, 0]
D1 = [0, 1, 0, 0, 0, 0]
D2 = [0, 0, 0, 1, 0, 0]
D3 = [0, 0, 0, 0, 1, 0]
E1 = [0, 1, 0, 1, 2, 0]
E2 = [0, 1, 0, 2, 1, 0]
E3 = [0, 2, 0, 1, 1, 0]
F1 = [0, 1, 0, 1, 0, 0]
F2 = [0, 1, 0, 0, 1, 0]
F3 = [0, 0, 0, 1, 1, 0]
G1 = [0, 0, 0, 0, 0, 0]


info([random.randrange(-10, 10), random.randrange(-10, 10), random.randrange(-10, 10), random.randrange(-10, 10), random.randrange(-10, 10), random.randrange(-10, 10)])