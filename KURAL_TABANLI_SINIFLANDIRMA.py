import pandas as pd

print("#################  GÖREV 1  #################\n")
## SORU 1: """Dosyayı okut ve bazı bilgileri göster"""
file = pd.read_csv("persona.csv")
print(file.head(3), "\n", file.tail(3)) #baştan ve sondan birkaç veriyi göstermeye karar verdim.


## SORU 2: """Benzersiz "SOURCE" değerleri ve frekanslar"""
print("Benzersiz değerler: ", file["SOURCE"].unique())
print("Benzersiz değerlerin sayısı: ", file["SOURCE"].unique().size)
print(f"Frekanslar:\n{file['SOURCE'].value_counts()}")

# print("Frekanslar: \n", file["SOURCE"].value_counts())              # "android" onunde bosluk oluyor; sevmedim.
# print("{}\n{}".format("Frekanslar", file["SOURCE"].value_counts()))              ; bu sekilde de yapilabilirdi.


## SORU 3: """Benzersiz "PRICE" değerleri"""
print("Benzersiz değerler: ", file["PRICE"].unique())
print("Benzersiz değerlerin sayısı: ", file["PRICE"].unique().size)


## SORU 4: """Benzersiz "PRICE" değerlerinden kaç tane gerçekleşmiş?"""
print(f"Frekanslar:\n{file['PRICE'].value_counts()}")


## SORU 5: """Hangi ülkede kaç satış olmuş?"""
print(f"Sayılar:\n{file['COUNTRY'].value_counts()}")
print(f"Türkiye'den kaç satış olmuş:\n{file['COUNTRY'].value_counts()['tur']}") #Fazladan ekledim, ödevde yoktu.


## SORU 6: """Ülkelere göre toplam kazançlar"""
country_groupped_prices = file.groupby("COUNTRY")["PRICE"]
print(f"Ülkelere göre toplam kazançlar:\n{country_groupped_prices.sum()}")


## SORU 7: """Kaynaklara göre satış sayıları"""
print(f"Kaynaklara göre satış sayıları:\n{file['SOURCE'].value_counts()}")


## SORU 8: """Ülkelere göre ortalama kazançlar"""
print(f"Ülkelere göre ortalama kazançlar:\n{country_groupped_prices.mean()}")


## SORU 9: """Kaynaklara göre ortalama kazançlar"""
source_groupped_prices = file.groupby("SOURCE")["PRICE"]
print(f"Kaynaklara göre ortalama kazançlar:\n{source_groupped_prices.mean()}")


## SORU 10: """Ülke-Kaynak kırılımına göre ortalama kazançlar"""
source_groupped_prices = file.groupby(["SOURCE", "COUNTRY"])["PRICE"]
print(f"Ülke-Kaynak kırılımına göre ortalama kazançlar:\n{source_groupped_prices.mean()}")


print("#################  GÖREV 2  #################\n")
print(file.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean())


print("#################  GÖREV 3  #################\n")
agg_df = file.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).mean().sort_values("PRICE", ascending=False)
print(agg_df.head())


print("#################  GÖREV 4  #################\n")
agg_df = agg_df.reset_index()
print(agg_df.head())


print("#################  GÖREV 5  #################\n")
age_bins = [0, 18, 23, 30, 40, 70]
age_categories = ['0_18', '19_23', '24_30', '31_40', '41_70']
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], age_bins, labels = age_categories)
print(agg_df.head())


print("#################  GÖREV 6  #################\n")
customers_level_categories = ["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]
agg_df["customers_level_based"] = agg_df[customers_level_categories[0]].str.upper()
for cat in customers_level_categories[1:]:
    agg_df["customers_level_based"] += "_" + agg_df[cat].str.upper()

persona_groupped_agg_price_mean = agg_df.groupby(["customers_level_based"])["PRICE"].mean()
print(persona_groupped_agg_price_mean.head())


print("#################  GÖREV 7  #################\n")
agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, labels=["D", "C", "B", "A"])
print(agg_df.groupby('SEGMENT').agg({'PRICE': ['mean', 'max','sum']}))


print("#################  GÖREV 8  #################\n")
TUR_ANDROID_FEMALE_31_40 = agg_df[agg_df['customers_level_based'] == 'TUR_ANDROID_FEMALE_31_40']
FRA_IOS_FEMALE_31_40 = agg_df[agg_df['customers_level_based'] == 'FRA_IOS_FEMALE_31_40']
print("31-40 yaş arası Türk kadını Android: \n", "Ortalama Kazanç: ", TUR_ANDROID_FEMALE_31_40["PRICE"].mean().__round__(2), "Segment: ", TUR_ANDROID_FEMALE_31_40["SEGMENT"].unique())
print("31-40 yaş arası Fransız kadını iOS: \n", "Ortalama Kazanç: ", FRA_IOS_FEMALE_31_40["PRICE"].mean().__round__(2), "Segment: ", FRA_IOS_FEMALE_31_40["SEGMENT"].unique())