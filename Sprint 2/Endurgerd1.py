import pygame, sys, os, time
from math import pi
pygame.init()
class skilgr:
    def __init__(self):
        Svartur  = (0, 0, 0 )
        Dokkbr = (58, 26, 12)
        Blue = (0, 0, 255)
        self.Black  = (0, 0, 0)

        #self.skrif = open("constraintshluti1.txt", 'a')
        o  = 0          # Wall
        x =  1          # Floor
        b  = 2          # Water
        s  = 3

        self.colours = {
                    o : Svartur,
                    x : Dokkbr,
                    b : Blue,
                    s : self.Black
                  }
        self.tilemap = [
                    #1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o],#1
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,o,o,o,o,o,o,o,o,x,x,x,x,x,o,x,x,x,x,x,x,o],#2
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,o,o,o,x,x,x,x,o,x,o,x,x,x,x,x,x,x,x,x,x,o],#3
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,o,o,o,x,o,o,x,o,x,o,x,o,o,x,x,o,x,x,x,x,o],#4
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,o,o,o,x,o,o,x,o,x,o,x,o,o,x,x,o,x,x,x,x,o],#5
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,o,o,o,x,o,o,x,x,x,o,x,x,x,x,x,o,o,o,x,x,o],#6
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,x,x,x,x,x,o,o,x,o,o,o,o,o,o,x,x,o,o,o,o,x,o],#7
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,o,o,x,x,x,x,x,x,x,x,x,x,x,x,x,o,x,x,x,x,o],#8
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,x,x,x,x,o,o,o,x,x,o,o,x,x,x,x,o,x,o,x,x,o],#9
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,x,o,o,x,x,x,o,x,o,o,o,o,o,o,o,o,x,x,o,o,o],#0
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,x,x,x,x,x,x,o,x,o,o,o,o,o,o,o,o,x,x,o,o,o],#1
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,o,o,o,o,o,o,o,x,o,o,x,x,x,x,x,x,x,x,x,x,o],#2
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,o,x,x,x,x,x,x,o,x,o,o,x,o,o,x,o,o,o,o,x,x,o],#3
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,o,o,o,o,x,x,o,x,o,o,x,o,o,x,o,o,x,x,x,x,o],#4
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,x,x,x,x,o,x,o,o,x,x,x,x,x,x,x,x,x,x,o],#5
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,x,x,x,x,x,x,o,x,x,x,x,x,x,x,x,x,x,o,o,o,o],#6
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,x,x,x,x,o],#7
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,o,x,x,x,x,x,x,x,o],#8
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,o,o,o,o,o,x,x,x,x,x,x,x,o,x,x,x,x,x,x,x,o],#9
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,o,x,x,x,x,x,x,o,x,x,x,x,x,o,x,x,x,x,x,x,x,o],#0
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,x,o,x,x,x,o,x,x,o,o,o,o,x,x,x,x,x,x,x,o],#1
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,x,x,x,x,x,x,x,x,x,o,x,x,x,x,x,x,x,x,x,x,o],#2
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,o,o,x,o,o,o,o,o,o,o,o,x,o,o,x,x,x,x,x,x,x,o],#3
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,b,b,b,x,x,o,o,o,x,x,o,x,x,x,x,x,x,x,x,o,o,x,x,x,x,x,x,x,o],#4
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,b,o,b,x,o,o,o,o,x,x,o,x,o,o,o,o,o,o,x,o,o,o,o,x,x,o,o,o,o],#5
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,b,b,o,o,o,o,o,x,o,o,x,o,x,x,o,o,o,o,o,o,o,o,x,x,x,x,x,o],#6
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,b,b,b,o,o,o,o,o,x,x,o,x,o,o,x,o,o,o,x,x,x,x,o,x,x,x,x,x,o],#7
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,x,x,o,x,o,o,x,x,x,o,x,o,o,x,x,x,x,o],#8
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,x,x,x,x,x,x,x,x,o,o,x,x,x,x,x,x,x,o],#9
                    [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o]#0
                    #1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3
                    ]
        self.Tilesize = 26
        self.Mapwidth = 53
        self.Mapheight= 30

        pygame.init()
        self.RED=(255,0,0)
        self.player_pos=[53*26-13*5,30*26-13*5]
        self.player_size=8

    def keyrsla(self,file,file2,file3):

        #Þetta hér að neðan getur orðið einn klassi með input-ið
        #   self.mapwidth*self.Tilesize,  self.Mapheight*self.Tilesize
        x = 0
        y = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((self.Mapwidth*self.Tilesize,self.Mapheight*self.Tilesize))
        pygame.FULLSCREEN

        pr_left=False; pr_right=False; pr_down=False;pr_up = False
        game_over = False####

        #óþarfi nema þegar verið er að skrifa í gagnasafn
        #x_hnit=747.5
        #y_hnit=403

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

                    x = self.player_pos[0]
                    y = self.player_pos[1]
#                    Hagri =False
#                    Vinstri =False
#                    Up=False
#                    Nid=False
#                    if event.key == pygame.K_LEFT:
#                        Vinstri=True
#                        x -= (13/2)
#                    elif event.key == pygame.K_RIGHT:
#                        Hagri = True
#                        x += (13/2)
#                    elif event.key == pygame.K_UP:
#                        Up = True
#                        y -= (13/2)
#                    elif event.key == pygame.K_DOWN:
#                        Nid = True
#                        y += (13/2)
#                    self.player_pos=[x,y]
                    if event.key == pygame.K_LEFT:
                        pr_left = True
                    if event.key == pygame.K_RIGHT:
                        pr_right= True
                    if event.key == pygame.K_UP:
                        pr_up   = True
                    if event.key == pygame.K_DOWN:
                        pr_down = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        pr_left = False
                    if event.key == pygame.K_RIGHT:
                        pr_right = False
                    if event.key == pygame.K_UP:
                        pr_up   = False
                    if event.key == pygame.K_DOWN:
                        pr_down = False
            x =self.player_pos[0]
            y =self.player_pos[1]
            if pr_left:
                x -=(13/2)
                print(x,y)
            if pr_right:
                x +=(13/2)
                print(x,y)
            if pr_up:
                y -=(13/2)
                print(x,y)
            if pr_down:
                y +=(13/2)
                print(x,y)



#            if (x_hnit!=x)or(y_hnit!=y):
#                print(x,y)
#                y_hnit=y
#                self.skrif.write(str(x_hnit))
#                self.skrif.write(",")
#                self.skrif.write(str(y_hnit))
#                self.skrif.write("\n")

            if y >= 403:
                f = open(file, 'r');
                #print(x,y)
                texti = str(x)+','+str(y)+'\n';
                #print(texti)
                #print(texti)

                for line in f.readlines():
                    if texti == line:
                        if pr_left:
                            x +=(13/2)
                        if pr_right:
                            x -=(13/2)
                        if pr_up:
                            y +=(13/2)
                        if pr_down:
                            y -=(13/2)

            else:
                f = open(file2, 'r');
                #print(x,y)
                texti = str(x)+','+str(y)+'\n';
                #print(texti)
                #print(texti)

                for line in f.readlines():

                    if texti == line:
                        if pr_left:
                            x +=(13/2)
                        if pr_right:
                            x -=(13/2)
                        if pr_up:
                            y +=(13/2)
                        if pr_down:
                            y -=(13/2)
            self.player_pos=[x,y]


            for row in range(self.Mapheight):         #ROÐ 1 UPPÍ 24

                for column in range(self.Mapwidth):   #DÁLKUR 1 UPPÍ 38

                    #pygame.draw.rect(  Surface  ,  color  ,  Rect  ,  Width  )
                    #  Surface => DISPLAYSURF
                    #  Color   => self.colours[  self.tilemap[ röð ][ dalkur ]  ]
                    #  Rect    => ( Dálkur_i * Tilesize,  röð_j * Tilesize , Tilesize, Tilesize)
                    pygame.draw.rect(DISPLAYSURF,   self.colours[self.tilemap[row][column]],   (column*self.Tilesize, row*self.Tilesize,self.Tilesize,self.Tilesize))
            #Teikna kassann
            pygame.draw.rect(DISPLAYSURF, self.RED, (self.player_pos[0],self.player_pos[1], self.player_size, self.player_size))
            if x >= 682.5:
                pygame.draw.circle(DISPLAYSURF, [0,0,0], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520,1480)
            elif x <682.5-6.25 and x>=682.5-6.25*2:
                pygame.draw.circle(DISPLAYSURF, [51,51,51], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.05)
            elif x <682.5-6.25*2 and x>=682.5-6.25*3:
                pygame.draw.circle(DISPLAYSURF, [76.5,76.5,76.5], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.08)
            elif x <682.5-6.25*3 and x>=682.5-6.25*4:
                pygame.draw.circle(DISPLAYSURF, [102,102,102], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.095)
            elif x <682.5-6.25*4 and x>=682.5-6.25*5:
                pygame.draw.circle(DISPLAYSURF, [127.5,127.5,127.5], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.1)
            elif x <682.5-6.25*5 and x>=682.5-6.25*6:
                pygame.draw.circle(DISPLAYSURF, [153,153,153], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.115)
            elif x <682.5-6.25*6 and x>=682.5-6.25*7:
                pygame.draw.circle(DISPLAYSURF, [179,179,179], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.134)
            elif x <682.5-6.25*7 and x>=682.5-6.25*8:
                pygame.draw.circle(DISPLAYSURF, [205,205,205], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.15)
            elif x <682.5-6.25*8 and x>=682.5-6.25*9:
                pygame.draw.circle(DISPLAYSURF, [230,230,230], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(0.2)
            elif x <682.5-6.25*9 and x>=682.5-6.25*10:
                pygame.draw.circle(DISPLAYSURF, [255,255,255], [int(self.player_pos[0])+5,int(self.player_pos[1]) +5], 1520)
                time.sleep(1.2)
            pygame.display.update()

def main():
    filename1="constraintshluti1.txt"
    filename2="constraintshluti2.txt"
    filename3="tefjari.txt"
    volun=skilgr()
    volun.keyrsla(filename1,filename2,filename3)
if __name__ == "__main__":
    main()
