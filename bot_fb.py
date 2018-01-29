import facebook

group = ['609529895797342','846159958780221','1526689954213507','120325428031450','1443765765867083','871965082870622','751512931534596','591759354185504'
         ,'584095768289909','504735246212124','487739907943984','463588560358236','255428914632455','122235371221779','217338361740668',
         '519540098071577','1531512357067946','1057283950952357','179392185449619','489531731103924','1730246590529463']
graph = facebook.GraphAPI("EAACEdEose0cBAOEyUSL1MGZCBEtk8aSKJkqfThOOlE5kXGUQYBLBPLk4YdkRIU5DCUdq91Q71JAbzOjSSlZB7zMJPNmhFeMR6tR2NXePHkokFAZB7zOzLM259ZARLK5kMq6cqEaZBcdLzJVtb0017GUQaZB7T7pRTqQZBbsbJLyrt1sUlDOeU5ZCns9OrOspZAqMZD")
#groups = graph.get_object("me/groups") # we take the ID of the first group
text = """GOEBOEG Production & Jatilawang South Conspiration present :
SOUTH OF GRIND #3
"Back To The Worms Of Bleed"
Sunday, July 2nd 2017
At Sport Hall Badmintoon Balai Desa Tinggarjaya
Grinding :
> Chalera [ Bekasi Brutal Death Metal ]
> Trench Horror [ Jakarta Grindcore ]
> Democrazy [ Cilacap Death Metal]
> Notion Baby Murder [ Jatilawang Death Metal ]
> Viral Damage [ Purwokerto Grindcore ]
> Jengah [ Purbalingga Hardcore Promo Album Innerstrength Foundation ]
> Eugenics [ Jatilawang Death Metal ]
> Bloodygod [Rawalo Death Metal ]
> Konspirator [ Kebasen Grindcore ]
> Rise Of Horus [Cilongok Death Metal ]
> Begotten Death [ Ajibarang Slamming Death Metal ]
> Before Dead [ Jatilawang Grindcore ]
> Planthing Sweet Potato [ Jatilawang Hardcore ]
> Zariyat Shakih [ Purwokerto Metalcore ]
> Anorexia Nervosa [ Jatilawang Deathcore ]
Suportde by :
- Rel Grinder 
- Purwokerto Underground Community
- Darma Underground Community 
- Gumelar Corpse Grinder
- Pekuncen Death Metal
- Akas Jaya Konfeksi 
- Setyowati Screen Printing 
- Re-Move 
- Sucker Distro 
- Dekatoki 
- Embrio.co 
- Klinik Metalik Distro
More Info :
085869951950
083876291666
http://southconspiration.blogspot.co.id/"""
for id in group:
    print id
    graph.put_object(id, "feed", message=text)