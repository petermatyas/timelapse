#!/bin/sh                                                                       
                                                                                
                                                         
echo "ido beallitasa"
echo "ev:"
read ev                                                
echo "honap: [Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]"                
read honap 
echo "nap:"
read nap
echo "ora:"
read ora
echo "perc:"
read perc       
            
sudo date -s "Mon $honap $nap $ora:$perc:00 UTC $ev"
sudo hwclock -w
sleep 1
sudo hwclock -r
