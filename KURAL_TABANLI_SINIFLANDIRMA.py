import pandas as pd

print("#################  GÖREV 1  #################\n")
## SORU 1: """Dosyayı okut ve bazı bilgileri göster"""
file = pd.read_csv("/home/rumeysa/Desktop/Miuul_summercamp/2.Hafta/2.hafta-odevler/Kural-tabanli-siniflandirma/persona.csv")
print(f"persona.csv veri seti:\n\n{file.head(3)}\n\n{file.tail(3)}") #baştan ve sondan birkaç veriyi göstermeye karar verdim.


## SORU 2: """Benzersiz "SOURCE" değerleri ve frekanslar"""
print("\n\nBenzersiz değerler: ", file["SOURCE"].unique())
print("Benzersiz değerlerin sayısı: ", file["SOURCE"].unique().size)
print(f"Frekanslar:\n{file['SOURCE'].value_counts()}")

# print("Frekanslar: \n", file["SOURCE"].value_counts())              # "android" onunde bosluk oluyor; sevmedim.
# print("{}\n{}".format("Frekanslar", file["SOURCE"].value_counts()))              ; bu sekilde de yapilabilirdi.


## SORU 3: """Benzersiz "PRICE" değerleri"""
print("\n\nBenzersiz değerler: ", file["PRICE"].unique())
print("Benzersiz değerlerin sayısı: ", file["PRICE"].unique().size)


## SORU 4: """Benzersiz "PRICE" değerlerinden kaç tane gerçekleşmiş?"""
print(f"\n\nFrekanslar:\n{file['PRICE'].value_counts()}")


## SORU 5: """Hangi ülkede kaç satış olmuş?"""
print(f"\n\nSayılar:\n{file['COUNTRY'].value_counts()}")
print(f"Türkiye'den kaç satış olmuş:\n{file['COUNTRY'].value_counts()['tur']}") #Fazladan ekledim, ödevde yoktu.


## SORU 6: """Ülkelere göre toplam kazançlar"""
country_groupped_prices = file.groupby("COUNTRY")["PRICE"]
print(f"\n\nÜlkelere göre toplam kazançlar:\n{country_groupped_prices.sum()}")


## SORU 7: """Kaynaklara göre satış sayıları"""
print(f"\n\nKaynaklara göre satış sayıları:\n{file['SOURCE'].value_counts()}")


## SORU 8: """Ülkelere göre ortalama kazançlar"""
print(f"\n\nÜlkelere göre ortalama kazançlar:\n{country_groupped_prices.mean()}")


## SORU 9: """Kaynaklara göre ortalama kazançlar"""
source_groupped_prices = file.groupby("SOURCE")["PRICE"]
print(f"\n\nKaynaklara göre ortalama kazançlar:\n{source_groupped_prices.mean()}")


## SORU 10: """Ülke-Kaynak kırılımına göre ortalama kazançlar"""
source_groupped_prices = file.groupby(["SOURCE", "COUNTRY"])["PRICE"]
print(f"\n\nÜlke-Kaynak kırılımına göre ortalama kazançlar:\n{source_groupped_prices.mean()}")


## GOREV 2: """COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar"""
print("\n#################  GÖREV 2  #################\n")
print(f'COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar:\n\n{file.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()}')


## GOREV 3: """Çıktıyı PRICE’a göre sıralama"""
print("\n#################  GÖREV 3  #################\n")
agg_df = file.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).mean().sort_values("PRICE", ascending=False)
print(f"Çıktıyı PRICE’a göre sıralama:\n{agg_df.head()}")


## GOREV 4: """Indekste yer alan isimleri değişken ismine çevirme"""
print("\n#################  GÖREV 4  #################\n")
agg_df = agg_df.reset_index()
print(f"Indekste yer alan isimleri değişken ismine çevirme:\n\n{agg_df.head()}")


## GOREV 5: """Age değişkenini kategorik değişkene çevirme ve agg_df’e ekleme"""
print("\n#################  GÖREV 5  #################\n")
age_bins = [0, 18, 23, 30, 40, 70]
age_categories = ['0_18', '19_23', '24_30', '31_40', '41_70']
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], age_bins, labels = age_categories)
print(f"Age değişkenini kategorik değişkene çevirme:\n\n{agg_df.head()}")


## GOREV 6: """Yeni seviye tabanlı müşterileri (persona) tanımlama"""
print("\n#################  GÖREV 6  #################\n")
customers_level_categories = ["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]
agg_df["customers_level_based"] = agg_df[customers_level_categories[0]].str.upper()
for cat in customers_level_categories[1:]:
    agg_df["customers_level_based"] += "_" + agg_df[cat].str.upper()

persona_groupped_agg_price_mean = agg_df.groupby(["customers_level_based"])["PRICE"].mean()
print(f"Yeni seviye tabanlı müşterileri (persona) tanımlama:\n{persona_groupped_agg_price_mean.head()}")


## GOREV 7: """Yeni müşterileri (personaları) segmentlere ayırma"""
print("\n#################  GÖREV 7  #################\n")
agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, labels=["D", "C", "B", "A"])
print(f"Yeni müşterileri (personaları) segmentlere ayırma:\n{agg_df.groupby('SEGMENT').agg({'PRICE': ['mean', 'max','sum']})}")


## GOREV 8: """Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin etme"""
print("\n#################  GÖREV 8  #################\n")
TUR_ANDROID_FEMALE_31_40 = agg_df[agg_df['customers_level_based'] == 'TUR_ANDROID_FEMALE_31_40']
FRA_IOS_FEMALE_31_40 = agg_df[agg_df['customers_level_based'] == 'FRA_IOS_FEMALE_31_40']
print("31-40 yaş arası Türk kadını Android: \n", "Ortalama Kazanç: ", TUR_ANDROID_FEMALE_31_40["PRICE"].mean().__round__(2), "Segment: ", TUR_ANDROID_FEMALE_31_40["SEGMENT"].unique())
print("31-40 yaş arası Fransız kadını iOS: \n", "Ortalama Kazanç: ", FRA_IOS_FEMALE_31_40["PRICE"].mean().__round__(2), "Segment: ", FRA_IOS_FEMALE_31_40["SEGMENT"].unique())