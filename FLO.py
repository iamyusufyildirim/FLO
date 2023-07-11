                                                        #################################
                                                        # FLO.com MÜŞTERİ SEGMENTASYONU #
                                                        #################################


#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                          UYGULAMA ÖNCESİ                                                                                                                                                                                                                                                                       +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                                                                                                                                                                                                                                                                                                               +
#    +                  master_id                   order_channel    last_order_channel   first_order_date   last_order_date   last_order_date_online   last_order_date_offline   order_num_total_ever_online   order_num_total_ever_offline   customer_value_total_ever_offline   customer_value_total_ever_online    interested_in_categories_12   +
#    +   0  cc294636-19f0-11eb-8d74-000d3a38a36f     Android App           Offline           2020-10-30         2021-02-26           2021-02-21               2021-02-26                     4.000                         1.000                            139.990                           799.380                                      [KADIN]   +
#    +   1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f     Android App            Mobile           2017-02-08         2021-02-16           2021-02-16               2020-01-10                     19.000                        2.000                            159.970                          1853.580             [ERKEK, COCUK, KADIN, AKTIFSPOR]   +
#    +   2  69b69676-1a40-11ea-941b-000d3a38a36f     Android App       Android App           2019-11-27         2020-11-27           2020-11-27               2019-12-01                      3.000                        2.000                            189.970                           395.350                               [ERKEK, KADIN]   +
#    +   3  1854e56c-491f-11eb-806e-000d3a38a36f     Android App       Android App           2021-01-06         2021-01-17           2021-01-17               2021-01-06                      1.000                        1.000                             39.990                            81.980                          [AKTIFCOCUK, COCUK]   +
#    +   4  d6ea1074-f1f5-11e9-9346-000d3a38a36f       Desktop             Desktop           2019-08-03         2021-03-07           2021-03-07               2019-08-03                      1.000                        1.000                             49.990                           159.990                                  [AKTIFSPOR]   +
#    +                                                                                                                                                                                                                                                                                                                                               +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                          UYGULAMA SONRASI                                                                                 +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    +                                                                                                                                                           +
#    +                            master_id            Recency  Frequency  Monetary Recency_Score Frequency_Score Monetary_Score RF_Score              SEGMENT   +
#    +    0      00016786-2f5a-11ea-bb80-000d3a38a36f       10       5.00    776.07             5               4              4       54            champions   +
#    +    1      00034aaa-a838-11e9-a2fc-000d3a38a36f      298       3.00    269.47             1               2              1       12          hibernating   +
#    +    2      000be838-85df-11ea-a90b-000d3a38a36f      213       4.00    722.69             2               3              4       23              at_Risk   +
#    +    3      000c1fe2-a8b7-11ea-8479-000d3a38a36f       27       7.00    874.16             5               4              4       54            champions   +
#    +    4      000f5e3e-9dde-11ea-80cd-000d3a38a36f       20       7.00   1620.33             5               4              5       54            champions   +
#    +                                                                                                                                                           +
#    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


"""
# 1. İş Problemi - (Business Problem)
# 2. Veriyi Anlama - (Data Understanding)
# 3. Veriyi Hazırlama - (Data Preparation)
# 4. RFM Metriklerinin Oluşturulması - (Calculating RFM Metrics)
# 5. RFM Skorlarının Oluşturulması - (Calculating RFM Scores)
# 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi - (Creating & Analysing RFM Segments)
"""


# ---------------------------------------
# - 1. İş Problemi - (Business Problem) -
# ---------------------------------------
# FLO müşteri davranışlarının tanımlanmasıyla segmentler oluşturup
# bu segmentler özelinde pazarlama stratejileri belirlemek istemektedir.
# Segmentasyon için RFM analizi kullanılacaktır.



# -------------------------------------------
# - 2. Veriyi Anlama - (Data Understanding) -
# -------------------------------------------

# Gerekli kütüphane importları ve bazı görsel ayarlamalar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option("display.float_format", lambda x : "%.2f" % x)


# flo.csv veri setinin projeye dahil edilmesi
def load_dataset():
    data = pd.read_csv("data_sets/flo_data_20k.csv")
    return data

df = load_dataset()


def check_df(dataframe, head=10):
    """
    Veri setindeki gözlem birimi, boyut bilgisi, değişken isimleri
    gibi veri seti hakkındaki genel resmi verir.

    Parameters
    ----------
    dataframe : dataframe
                Bilgisi istenilen veri seti

    head : int
           Kaç satır gözlem birimi istenildiği bilgisi

    """
    print("###################################")
    print(f"#### İlk {head} Gözlem Birimi ####")
    print("###################################")
    print(dataframe.head(head), "\n\n")

    print("###################################")
    print("###### Veri Seti Boyut Bilgisi ####")
    print("###################################")
    print(dataframe.shape, "\n\n")

    print("###################################")
    print("######## Değişken İsimleri ########")
    print("###################################")
    print(dataframe.columns, "\n\n")

    print("###################################")
    print("####### Eksik Değer Var mı? #######")
    print("###################################")
    print(dataframe.isnull().values.any(), "\n\n")

    print("###################################")
    print("##### Betimsel İstatistikler ######")
    print("###################################")
    print(dataframe.describe().T, "\n\n")

    print("###################################")
    print("### Veri Seti Hakkında Bilgiler ###")
    print("###################################")
    print(dataframe.info())

check_df(dataframe=df)


def grab_col_names(dataframe, cat_th=10, car_th=20, num_th=20, plot=False):
    """
        Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin raporlama işlemini gerçekleştirir.

        Parameters
        ----------
        dataframe : dataframe
            değişken isimleri alınmak istenen veri seti.
        cat_th : int, float
            kategorik değişkenler için sınıf eşik değeri.
        num_th : int, float
            numerik değişkenler için sınıf eşik değeri.
        plot : bool

        Returns
        -------
            cat_cols: list
                Kategorik değişkenlerin listesi
            cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi
            num_cols: list
                Numerik değişkenlerin listesi

        Notes
        -----
        plot argümanının True olması durumunda ilgili kategorik ve numerik değişkenler görselleştirilecektir.
        """

    # Kategorik ve numerik görünümlü ancak kategorik olan değişkenleri filtreledik.
    cat_cols = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                                                    dataframe[col].dtypes in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < num_th and
                                                       dataframe[col].dtypes in ["int", "float"]]
    cat_cols += num_but_cat


    # Kategorik görünümlü ancak Kardinal değişkenleri filtreledik.
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                                                       dataframe[col].dtypes in ["category", "object"]]

    # Eğer plot argümanı True'ysa ilgili özet ve görselleştirme işlemini uygula
    if plot:
        for cat in cat_cols:
            print(dataframe[cat].value_counts())
            print("###########################")

            sns.countplot(x=dataframe[cat], data=dataframe)
            plt.show(block=True)


    # Numerik değişkenleri filtreleyioruz.
    num_cols = [col for col in dataframe.columns if dataframe[col].nunique() > num_th and
                                                    dataframe[col].dtypes in ["int", "float"]]


    # Eğer plot argümanı True'ysa ilgili özet ve görselleştirme işlemini uygula
    if plot:
        for num in num_cols:
            print(dataframe[num].describe().T)
            print("###########################")

            dataframe[num].hist()
            plt.show(block=True)


    print(f"""
    ilgili veri setine ait toplamda {dataframe.shape[0]} gözlem birimi ve {dataframe.shape[1]} değişken bulunmaktadır.
    -> Kategorik Değişken: {len(cat_cols)} Adet kategorik değişken bulunmaktadır.
    -> Kategorik Değişkenler: {cat_cols}
    -> Kardinal Değşken: {len(cat_but_car)} Adet kategorik görünümlü ancak kardinal olan değişken bulunmaktadır.
    -> Kardinal Değişkenler: {cat_but_car}
    -> Numerik Değişken: {len(num_cols)} Adet Sayısal değişken bulunmaktadır.
    -> Numerik Değişkenler: {num_cols}
    """)

grab_col_names(dataframe=df)


# - 3. Veriyi Hazırlama - (Data Preparation) -
# --------------------------------------------

# Tarih ifade eden değişkenlerin tipini date'e çevirdik.
for col in df.columns:
    if "date" in col:
        df[col] = df[col].astype("datetime64[ns]")


# Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı yeni değişken oluşturunuz.
df["total_order_num"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
# Herbir müşterinin toplam harcama tutarı için yeni değişken oluşturunuz.
df["total_price"] = df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"]


# ------------------------------------------------------------------
# - 4. RFM Metriklerinin Oluşturulması - (Calculating RFM Metrics) -
# ------------------------------------------------------------------

# Veri setindeki en son alışverişin yapıldığı tarihi nedir?
df["last_order_date"].max() # 2021-05-30

# Analiz tarihi için en son alışveriş tarihinden 2 gün sonrasını
# baz alarak ilgili hesaplamaları gerçekleştireceğiz.
today_date = dt.datetime(2021, 6, 1)


# R -> Recency: Müşteri yeniliğini ifade eder. Matematiksel karşılığı = Analiz tarihi - ilgili müşterinin son aLışveriş tarihi
# F -> Frequency: Toplam alışveriş sayısı bir diğer ifadesiyle toplam işlem sayısıdır. Matematiksel karşılığı = ilgili müşterinin toplam alışveriş sayısı
# M -> Monetary: Müşterinin şirket ile kurduğu ilişki süresince bıraktığı toplam parasal değeri ifade eder. Matematiksel karşılığı = ilgili müşterinin toplam harcama tutarı

rfm = df.groupby("master_id").agg({"last_order_date" : lambda date : (today_date - date.max()).days,
                                   "total_order_num" : lambda total_order_num : total_order_num.sum(),
                                   "total_price" : lambda total_price : total_price.sum(),
                                   "interested_in_categories_12" : lambda category : category  # PowerBI ile raporlama işlemi için category değişkeninide dahil ettim.
                                   }).sort_values(by="total_price", ascending=False)


rfm.columns = ["Recency", "Frequency", "Monetary", "Category"]


rfm.reset_index(inplace=True)


# master_id değişken ismini customer_id ismiyle güncelliyoruz.
rfm = rfm.rename(columns={'master_id': 'customer_id'})



# ---------------------------------------------------------------
# - 5. RFM Skorlarının Oluşturulması - (Calculating RFM Scores) -
# ---------------------------------------------------------------

# Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi
rfm["Recency_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["Frequency_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["Monetary_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])

# Recency ve Frequency skorlarının birleştirilmesi
rfm["RF_Score"] = rfm["Recency_Score"].astype(str) + rfm["Frequency_Score"].astype(str)
rfm["RFM_Score"] = rfm["Recency_Score"].astype(str) + rfm["Frequency_Score"].astype(str) + rfm["Monetary_Score"].astype(str)


# ------------------------------------------------------------------------------------------------
# - 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi - (Creating & Analysing RFM Segments) -
# ------------------------------------------------------------------------------------------------

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm["SEGMENT"] = rfm['RF_Score'].replace(seg_map, regex=True)


# Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
rfm[["SEGMENT", "Recency", "Frequency", "Monetary"]].groupby("SEGMENT").agg(["mean", "count"])



# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.
target_segments_customer_ids = rfm[rfm["SEGMENT"].isin(["champions","loyal_customers"])]["customer_id"]
cust_ids = df[(df["master_id"].isin(target_segments_customer_ids)) &(df["interested_in_categories_12"].str.contains("KADIN"))]["master_id"]
cust_ids.to_csv("yeni_marka_hedef_müşteri_id.csv", index=False)



# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.
target_segments_customer_ids = rfm[rfm["SEGMENT"].isin(["cant_loose","hibernating","new_customers"])]["customer_id"]
cust_ids = df[(df["master_id"].isin(target_segments_customer_ids)) & ((df["interested_in_categories_12"].str.contains("ERKEK"))|(df["interested_in_categories_12"].str.contains("COCUK")))]["master_id"]
cust_ids.to_csv("indirim_hedef_müşteri_ids.csv", index=False)



# Monetary değerlerindeki virgülden sonraki ondalıklı ifade dikkat dağııtığı için sadece int değer olarak görme isteğimi bildiriyorum.
rfm["Monetary"] = rfm["Monetary"].astype(int)


# İgili analizin Excel formatında dış ortama aktarılması.
FLO_RFM = pd.DataFrame(rfm)
FLO_RFM.to_excel("FLO_RFM.xlsx")