def amogus(sped):
   import winsound as w
   import time as t

   c2,d2,f2,g2,a,cd = 277,311,370,415,440,131

   notes = (d2,f2,g2,a,g2,f2,d2,c2,d2,c2,cd,cd,
             d2,f2,g2,a,g2,f2,a,a,g2,f2,a,g2,f2,d2
             )
   delay = (1,1,1,1,1,1,2,.5,.5,2,1,2,
             1,1,1,1,1,1,2,1,1,1,1,1,1,2
             )
   for i in range(len(notes)):
        w.Beep(notes[i],int(200*delay[i]*sped))
   return("sus")

amogus(1)
