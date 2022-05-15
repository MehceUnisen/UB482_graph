#print("I love boobs")
import pandas as pd
import matplotlib.pyplot as plt

heading_list = ["gnss", "msgLen", "year", "month","day", "hour", "min", "sec", "rtkStat","headingStat", "gpsStat","bdsStat", "gloStat", "baselineN", "baselineE","baselineU", "baselineNStd", "baselineEStd","baselineUStd", "heading", "gpsPitch", "gpsRoll","gpsSpeed", "velN", "velE", "velUp", "xigVx", "xigVy", "xigVz", "lat", "lon","roverHei", "ecefX", "ecefY", "ecefZ", "xigLat","xigLon", "xigAlt", "xigEcefX", "xigEcefY","xigEcefZ","secLat", "secLon","secAlt", "gpsWeekSec", "diffage", "speedHeading", "undulation","galStat"]

df = pd.read_csv("log.csv", usecols=heading_list)
#buraya kadar ortak kod buraya kadar elleme


#birden fazla grafigi ayni anda gosterebilmek icin figure kullaniliyor
#parametre olarak aldigi string pencerenin adi oluyor
plot1 = plt.figure("terapistim anime kizlari gercek degil diyor nasil degil yanimda bir tane var su anda")
plt.plot(df["rtkStat"])
plt.plot(df["year"])
#birden fazla veriyi tek grafikte gostermek icin bu sekilde arka arkaya
#iki tane veriyi plot demek lazim

#ayri bir pencerede yeni bir grafik acmak icin yeni bir tane figure tanimliyoruz
plot2 = plt.figure("待って ください")
plt.plot(df["month"])
#sonra da vur plotu gec



#bu satir ne olursa olsun en sonda kalacak
plt.show()