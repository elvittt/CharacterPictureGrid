grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#def image(alist):
    #for x in range(len(alist)):
        #print(alist[x][0],end='')
    #print('')
    #for x in range(len(alist)):
        #print(alist[x][1],end='')  
    #print('')
    #for x in range(len(alist)):
        #print(alist[x][2],end='')   
    #print('')
    #for x in range(len(alist)):
         #print(alist[x][3],end='')  
    #print('')
    #for x in range(len(alist)):
         #print(alist[x][4],end='')   
    #print('')
    #for x in range(len(alist)):
         #print(alist[x][5],end='')

def image(alist):
    for x in range(len(alist[0])):
        for y in range(len(alist)):
            print(alist[y][x],end='')
        print()

image(grid)
