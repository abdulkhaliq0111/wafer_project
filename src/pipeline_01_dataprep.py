��f r o m   j s o n . t o o l   i m p o r t   m a i n 
 
 i m p o r t   o s 
 
 i m p o r t   a r g p a r s e 
 
 i m p o r t   y a m l 
 
 i m p o r t   l o g g i n g 
 
 
 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " : 
 
         a r g s   =   a r g p a r s e . A r g u m e n t P a r s e r ( ) 
 
         a r g s . a d d _ a r g u m e n t ( " - - c o n f i g " ,   d e f a u l t   =     " d e f a u l t " ) 
 
 
 
         a r g s . a d d _ a r g u m e n t ( " - - d a t a s o u r c e " ,   d e f a u l t   =     N o n e ) 
 
 
 
         p a r s e d _ a r g s = a r g s . p a r s e _ a r g s ( ) 
 
         p r i n t ( p a r s e d _ a r g s ) 
 
         