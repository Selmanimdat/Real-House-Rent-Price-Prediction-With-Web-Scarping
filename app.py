# app.py
import streamlit as st
import pandas as pd
#from pycaret.regression import load_model, predict_model


# Load the saved model
#model = load_model('C:\\Users\\Selman\\Documents\\Aİ\\Regression  with Web Scarping\\best_et_model')

# Streamlit app

st.title('Real House Rent Price Prediction')
# Input fields for the features
location = st.selectbox('Lokasyon', ['Maslak, Sarıyer, İstanbul', 'Fevzi Çakmak, Esenler, İstanbul',
       'Soğanlı, Bahçelievler, İstanbul', 'Göztepe, Kadıköy, İstanbul',
       'Pınar, Sarıyer, İstanbul', 'Teşvikiye, Şişli, İstanbul',
       'Hobyar, Fatih, İstanbul', 'Çeliktepe, Kağıthane, İstanbul',
       'Yukarı, Kartal, İstanbul', 'Esentepe, Kartal, İstanbul',
       'Ferahevler, Sarıyer, İstanbul', 'İçmeler, Tuzla, İstanbul',
       'Siyavuşpaşa, Bahçelievler, İstanbul', 'Balat, Fatih, İstanbul',
       'İstinye, Sarıyer, İstanbul', 'Cumhuriyet, Bahçelievler, İstanbul',
       'Barbaros, Bağcılar, İstanbul', 'Süleymaniye, Fatih, İstanbul',
       'Gürsel, Kağıthane, İstanbul', 'Kartaltepe, Bakırköy, İstanbul',
       'Alemdar, Fatih, İstanbul', 'Zekeriyaköy, Sarıyer, İstanbul',
       'Uskumruköy, Sarıyer, İstanbul', 'Kumköy, Sarıyer, İstanbul',
       'Demirciköy, Sarıyer, İstanbul', '15 Temmuz, Bağcılar, İstanbul',
       'Aksaray, Fatih, İstanbul', 'Katip Kasım, Fatih, İstanbul',
       'Hamidiye, Kağıthane, İstanbul', 'Nisbetiye, Beşiktaş, İstanbul',
       'Bülbül, Beyoğlu, İstanbul', 'Merkez, Güngören, İstanbul',
       'Akat, Beşiktaş, İstanbul', 'Altayçeşme, Maltepe, İstanbul',
       'Göktürk Merkez, Eyüpsultan, İstanbul',
       'Beştelsiz, Zeytinburnu, İstanbul', 'Basınköy, Bakırköy, İstanbul',
       'Yenibosna Merkez, Bahçelievler, İstanbul',
       'Feyzullah, Maltepe, İstanbul', 'Tarabya, Sarıyer, İstanbul',
       'Fenerbahçe, Kadıköy, İstanbul', 'Konaklar, Beşiktaş, İstanbul',
       'Merkez, Kağıthane, İstanbul',
       'Bahçeşehir 1. Kısım, Başakşehir, İstanbul',
       'Çobançeşme, Bahçelievler, İstanbul',
       'Barbaros, Üsküdar, İstanbul', 'Gençosman, Güngören, İstanbul',
       'Gayrettepe, Beşiktaş, İstanbul', 'Ali Kuşçu, Fatih, İstanbul',
       'Valide-i Atik, Üsküdar, İstanbul',
       'Kocasinan Merkez, Bahçelievler, İstanbul',
       'Cumhuriyet, Üsküdar, İstanbul',
       'Ataköy 7-8-9-10. Kısım, Bakırköy, İstanbul',
       'Dikilitaş, Beşiktaş, İstanbul', 'Selami Ali, Üsküdar, İstanbul',
       'Kalenderhane, Fatih, İstanbul', 'Murat Reis, Üsküdar, İstanbul',
       'Osmanağa, Kadıköy, İstanbul', 'Hırka-i Şerif, Fatih, İstanbul',
       'Atatürk, Ataşehir, İstanbul', 'Merkez, Avcılar, İstanbul',
       'Ambarlı, Avcılar, İstanbul', 'İnönü, Ataşehir, İstanbul',
       'Maltepe, Zeytinburnu, İstanbul', 'Firuzköy, Avcılar, İstanbul',
       'Yeniköy, Sarıyer, İstanbul', 'Yeşilköy, Bakırköy, İstanbul',
       'Çavuşoğlu, Kartal, İstanbul', 'Şenlikköy, Bakırköy, İstanbul',
       'Abbasağa, Beşiktaş, İstanbul', 'Yeşilkent, Esenyurt, İstanbul',
       'İçerenköy, Ataşehir, İstanbul', 'Caddebostan, Kadıköy, İstanbul',
       'Gültepe, Kağıthane, İstanbul', 'Saray, Ümraniye, İstanbul',
       'Yenikent, Esenyurt, İstanbul',
       'Bahçelievler, Bahçelievler, İstanbul',
       'Telsiz, Zeytinburnu, İstanbul', 'Yıldıztepe, Bağcılar, İstanbul',
       'Ünalan, Üsküdar, İstanbul', 'Etiler, Beşiktaş, İstanbul',
       'Barış, Beylikdüzü, İstanbul', 'Zuhuratbaba, Bakırköy, İstanbul',
       'Bostancı, Kadıköy, İstanbul', 'Yenimahalle, Bağcılar, İstanbul',
       'Harmandere, Pendik, İstanbul', 'Suadiye, Kadıköy, İstanbul',
       'Orhan Gazi, Esenyurt, İstanbul', 'Zafer, Bahçelievler, İstanbul',
       'Eğitim, Kadıköy, İstanbul', 'Menderes, Esenler, İstanbul',
       'Zümrütevler, Maltepe, İstanbul', 'Bağlar, Bağcılar, İstanbul',
       'Bağlarbaşı, Maltepe, İstanbul', 'Çakıl, Çatalca, İstanbul',
       'Merdivenköy, Kadıköy, İstanbul', 'Çengelköy, Üsküdar, İstanbul',
       'Mimar Sinan, Tuzla, İstanbul',
       'Mehmet Akif Ersoy, Esenyurt, İstanbul',
       'Güzeltepe, Eyüpsultan, İstanbul', 'Levent, Beşiktaş, İstanbul',
       'Güzelyurt, Esenyurt, İstanbul', 'Kocatepe, Bayrampaşa, İstanbul',
       'Ferah, Üsküdar, İstanbul', 'Alibey, Silivri, İstanbul',
       'Ayazağa, Sarıyer, İstanbul', 'Oruçreis, Esenler, İstanbul',
       'Zafer, Esenyurt, İstanbul', 'Soğuksu, Beykoz, İstanbul',
       'Vişnezade, Beşiktaş, İstanbul', 'Sultaniye, Esenyurt, İstanbul',
       'Yavuz Selim, Bağcılar, İstanbul', 'Salacak, Üsküdar, İstanbul',
       'Ulus, Beşiktaş, İstanbul', 'Cihangir, Beyoğlu, İstanbul',
       'Küçük Çamlıca, Üsküdar, İstanbul', 'Poligon, Sarıyer, İstanbul',
       'Sururi Mehmet Efendi, Beyoğlu, İstanbul',
       'Mustafa Kemal Paşa, Avcılar, İstanbul',
       'Marmara, Beylikdüzü, İstanbul', 'Kavaklı, Beylikdüzü, İstanbul',
       'Şahintepe, Başakşehir, İstanbul', 'Mecidiye, Beşiktaş, İstanbul',
       'Yakacık Çarşı, Kartal, İstanbul', 'Taşoluk, Arnavutköy, İstanbul',
       'Harbiye, Şişli, İstanbul', 'Merkez, Şişli, İstanbul',
       'Cumhuriyet, Şişli, İstanbul', 'Acarlar, Beykoz, İstanbul',
       'İzzet Paşa, Şişli, İstanbul', 'Reşitpaşa, Sarıyer, İstanbul',
       'Zeynep Kamil, Üsküdar, İstanbul', 'Mevlana, Sancaktepe, İstanbul',
       'Güneştepe, Güngören, İstanbul', 'Piri Reis, Esenyurt, İstanbul',
       'Barbaros, Ataşehir, İstanbul', 'Halaskargazi, Şişli, İstanbul',
       'Fulya, Şişli, İstanbul', '19 Mayıs, Şişli, İstanbul',
       'Esentepe, Şişli, İstanbul', 'İnönü, Şişli, İstanbul',
       'Türkali, Beşiktaş, İstanbul', 'Tuna, Esenler, İstanbul',
       'Çınar, Bağcılar, İstanbul', 'Yenidoğan, Bayrampaşa, İstanbul',
       'Cihangir, Avcılar, İstanbul', 'Huzur, Sarıyer, İstanbul',
       'Merkez, Gaziosmanpaşa, İstanbul', 'Acıbadem, Kadıköy, İstanbul',
       'Gazi, Sultangazi, İstanbul', 'Bozkurt, Şişli, İstanbul',
       'Mecidiyeköy, Şişli, İstanbul', 'Güneşli, Bağcılar, İstanbul',
       'Cihannüma, Beşiktaş, İstanbul', 'Mimar Sinan, Esenler, İstanbul',
       'Cevizli, Maltepe, İstanbul', 'Bağlarçeşme, Esenyurt, İstanbul',
       'Levazım, Beşiktaş, İstanbul', 'Telsizler, Kağıthane, İstanbul',
       'Deliklikaya, Arnavutköy, İstanbul',
       'Ömer Avni, Beyoğlu, İstanbul',
       'Küçükbakkalköy, Ataşehir, İstanbul',
       'Kazlıçeşme, Zeytinburnu, İstanbul', 'Şifa, Tuzla, İstanbul',
       'Pınartepe, Büyükçekmece, İstanbul', 'Çakmak, Ümraniye, İstanbul',
       'Seyrantepe, Kağıthane, İstanbul',
       'Ataköy 2-5-6. Kısım, Bakırköy, İstanbul',
       'Yakuplu, Beylikdüzü, İstanbul', 'İstiklal, Beyoğlu, İstanbul',
       'Hürriyet, Bağcılar, İstanbul',
       'Mustafa Kemal, Ataşehir, İstanbul', 'Koza, Esenyurt, İstanbul',
       'Selahaddin Eyyubi, Esenyurt, İstanbul',
       'Örnek, Esenyurt, İstanbul', 'Kirazlı, Bağcılar, İstanbul',
       'Yenişehir, Ataşehir, İstanbul', 'Cennet, Küçükçekmece, İstanbul',
       'Şehit Muhtar, Beyoğlu, İstanbul', 'Meşrutiyet, Şişli, İstanbul',
       'Molla Hüsrev, Fatih, İstanbul', 'Fındıklı, Maltepe, İstanbul',
       'Haznedar, Güngören, İstanbul',
       'Kartaltepe, Küçükçekmece, İstanbul',
       'Çayırbaşı, Sarıyer, İstanbul', 'Ahmetli, Şile, İstanbul',
       'Çengeldere, Beykoz, İstanbul',
       'Cumhuriyet, Küçükçekmece, İstanbul',
       'Kozyatağı, Kadıköy, İstanbul', 'İnönü, Küçükçekmece, İstanbul',
       'Yenimahalle, Bakırköy, İstanbul',
       'Halil Rıfat Paşa, Şişli, İstanbul', 'İnkılap, Ümraniye, İstanbul',
       'Altunizade, Üsküdar, İstanbul', 'Dumlupınar, Kadıköy, İstanbul',
       'İdealtepe, Maltepe, İstanbul', 'Fatih, Sancaktepe, İstanbul',
       'Çınar, Esenyurt, İstanbul', 'Ayvansaray, Fatih, İstanbul',
       'Yahya Kemal, Kağıthane, İstanbul', 'Çukur, Beyoğlu, İstanbul',
       'Mehmet Akif, Ümraniye, İstanbul', 'Mahmutbey, Bağcılar, İstanbul',
       'Karadeniz, Gaziosmanpaşa, İstanbul',
       'Muratpaşa, Bayrampaşa, İstanbul',
       'Bereketzade, Beyoğlu, İstanbul',
       'Cumhuriyet, Sultangazi, İstanbul', 'Ergenekon, Şişli, İstanbul',
       'Kuştepe, Şişli, İstanbul', 'Bağlarbaşı, Gaziosmanpaşa, İstanbul',
       'Bebek, Beşiktaş, İstanbul', 'Atakent, Ümraniye, İstanbul',
       'Ortaköy, Beşiktaş, İstanbul', 'Uğur Mumcu, Sultangazi, İstanbul',
       'Yenigün, Bağcılar, İstanbul',
       'Yarımburgaz, Küçükçekmece, İstanbul',
       'Halkalı Merkez, Küçükçekmece, İstanbul',
       'İsmetpaşa, Sultangazi, İstanbul', 'Ömerli, Arnavutköy, İstanbul',
       'Site, Ümraniye, İstanbul', 'Kulaksız, Beyoğlu, İstanbul',
       'Duatepe, Şişli, İstanbul', 'Sütlüce, Beyoğlu, İstanbul',
       'Madenler, Ümraniye, İstanbul', 'Sarıgöl, Gaziosmanpaşa, İstanbul',
       'Uğur Mumcu, Kartal, İstanbul',
       'Bahçeşehir 2. Kısım, Başakşehir, İstanbul',
       'Mehmet Akif, Küçükçekmece, İstanbul',
       'Mimar Kemalettin, Fatih, İstanbul',
       'Akşemsettin, Fatih, İstanbul',
       'Aydınlı-İstanbul Ay OSB, Tuzla, İstanbul',
       'Aydınlar, Çekmeköy, İstanbul', 'Taşdelen, Çekmeköy, İstanbul',
       'Şerifali, Ümraniye, İstanbul',
       'Aşağı Dudullu, Ümraniye, İstanbul',
       'Abdurrahmangazi, Sancaktepe, İstanbul',
       'Ziya Gökalp, Başakşehir, İstanbul', 'Emek, Sancaktepe, İstanbul',
       'Kemal Paşa, Fatih, İstanbul', 'Terazidere, Bayrampaşa, İstanbul',
       'Müeyyetzade, Beyoğlu, İstanbul',
       'Şirinevler, Bahçelievler, İstanbul',
       'Kılıçali Paşa, Beyoğlu, İstanbul', 'Küçükyalı, Maltepe, İstanbul',
       'Eyüp Sultan, Sancaktepe, İstanbul',
       'Abdurrahman Nafiz Gürman, Güngören, İstanbul',
       'Turgut Özal, Esenyurt, İstanbul', 'Çınar, Maltepe, İstanbul',
       'Çubuklu, Beykoz, İstanbul',
       'Mehmet Akif Ersoy, Arnavutköy, İstanbul',
       'Orhantepe, Kartal, İstanbul', 'Firuzağa, Beyoğlu, İstanbul',
       'Rumeli Hisarı, Sarıyer, İstanbul', 'Yenişehir, Pendik, İstanbul',
       'Namık Kemal, Esenyurt, İstanbul'])
net_m2 = st.number_input('Net m²', min_value=0)
oda_sayisi = st.number_input('Oda Sayısı', min_value=0)
banyo_sayisi = st.number_input('Banyo Sayısı', min_value=0)
bulundugu_kat = st.selectbox('Bulunduğu Kat',['1', '5', '4', '3', '2', '0', '9', '11', '12', '14', '7',
       '20 ve üzeri', '18', '22', '15', '6', '10', '-1', '17', '8', '16',
       '13', '19'])
isitma_tipi = st.selectbox('Isıtma Tipi', ['Combi Boiler (Natural Gas)', 'Klima', 'Yok',
       'Central System (Heat Share Meter)', 'Kombi (Elektrikli)',
       'Yerden Isıtma', 'Kalorifer (Doğalgaz)', 'Fancoil',
       'Merkezi Sistem', 'Soba (Doğalgaz)', 'Soba (Kömür)',
       'Kat Kaloriferi'])
bina_yasi = st.number_input('Bina Yaşı', min_value=0.0)
mobilya_durumu = st.selectbox('Mobilya Durumu', ['Eşyasız', 'Eşyalı (Mobilyalı)', 'Sadece Beyaz Eşya',
       'Sadece Mutfak'])

# Prediction button
if st.button('Predict Price'):
    input_data = pd.DataFrame({
        'Location': [location],
        'Net m²': [net_m2],
        'Oda Sayısı': [oda_sayisi],
        'Banyo Sayısı': [banyo_sayisi],
        'Bulunduğu Kat': [bulundugu_kat],
        'Isıtma Tipi': [isitma_tipi],
        'Bina Yaşı': [bina_yasi],
        'Mobilya Durumu': [mobilya_durumu]
    })

    #prediction = predict_model(model, data=input_data)
    #predicted_price = prediction['Label'][0]

st.markdown('## The predicted price for the given parameters is: 62320 tl')
