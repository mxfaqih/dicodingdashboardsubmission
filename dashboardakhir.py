import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from babel.numbers import format_currency
import seaborn as sns

# Load data
url = 'https://raw.githubusercontent.com/mxfaqih/dicodingdashboardsubmission/main/main_data.csv'
main_data= pd.read_csv(url,index_col=0)

datetime_columns = ["order_purchase_timestamp", "order_delivered_customer_date", "order_approved_at"]
for column in datetime_columns:
    main_data[column] = pd.to_datetime(main_data[column])
    
with st.sidebar:
    st.header('Brazilian E Commerce')
    st.write('sebuah dashboard yang menampilkan informasi tentang Brazilian E-commerce. Dashboard ini dibuat menggunakan library Streamlit dan menampilkan beberapa visualisasi yang menarik')
    selected_cities = st.multiselect('Pilih Kota', main_data['customer_city'].unique())

st.header('Brazilian E-commerce Dashboard')

st.subheader('Data Overview')
st.write(main_data.head())

st.subheader('Distribusi Status Order')
status_counts = main_data['order_status'].value_counts()
st.bar_chart(status_counts)
with st.expander("Detail"):
    st.write('Diagram "Distribusi Status Order" pada dashboard tersebut menunjukkan bahwa sebagian besar status order pada Brazilian E-commerce adalah "delivered". Hal ini menunjukkan bahwa sebagian besar pelanggan telah menerima produk yang mereka pesan dan produk tersebut telah dikirimkan dengan sukses. Namun, diagram ini juga menunjukkan bahwa ada sejumlah kecil order yang dibatalkan atau belum diproses, yang dapat menjadi perhatian bagi Brazilian E-commerce untuk meningkatkan kualitas layanan mereka. Dengan informasi ini, Brazilian E-commerce dapat memperbaiki proses pengiriman dan memastikan bahwa produk yang dipesan oleh pelanggan dapat dikirimkan dengan cepat dan aman.')

st.subheader('5 Product dengan peforma terbaik')
top_products = main_data['product_category_name'].value_counts().head(5)
st.bar_chart(top_products)
with st.expander("Detail"):
    st.write('Diagram "5 Product dengan Performa Terbaik" pada dashboard tersebut menunjukkan 5 produk dengan performa terbaik pada Brazilian E-commerce. Diagram ini dapat membantu pengguna untuk memahami produk mana yang paling laris dan populer di antara pelanggan.')

st.subheader('Distribusi Tipe Payment ')
payment_counts = main_data['payment_type'].value_counts()
st.bar_chart(payment_counts)
with st.expander("Detail"):
    st.write('Diagram ini menunjukkan bahwa sebagian besar pelanggan menggunakan kartu kredit sebagai metode pembayaran. Hal ini menunjukkan bahwa penggunaan kartu kredit sangat populer di antara pelanggan Brazilian E-commerce. Selain itu, diagram ini juga menunjukkan bahwa sebagian kecil pelanggan menggunakan metode pembayaran lain seperti boleto, voucher, dan debit card.')

st.subheader('Review Scores')
review_scores = main_data['review_score'].value_counts().sort_index()
st.bar_chart(review_scores)
with st.expander("Detail"):
    st.write('Diagram ini menunjukkan bahwa sebagian besar pelanggan memberikan review bintang 5 sebanyak 66264 dan review bintang 1 sebanyak 14854. Hal ini menunjukkan bahwa sebagian besar pelanggan merasa puas dengan produk dan layanan yang ditawarkan oleh Brazilian E-commerce, namun ada sejumlah kecil pelanggan yang merasa tidak puas dengan produk dan layanan tersebut')

st.subheader('Distribusi Waktu Pengiriman')
delivery_time = (main_data['order_delivered_customer_date'] - main_data['order_purchase_timestamp']).dt.days
fig, ax = plt.subplots()
sns.histplot(delivery_time, kde=True, color='lightblue', ax=ax)
st.pyplot(fig)

st.subheader('Nilai Pembayaran Rata-rata berdasarkan Jenis Pembayaran')
avg_payment = main_data.groupby('payment_type')['payment_value'].mean()
st.bar_chart(avg_payment)
    
st.caption('Copyright © 2023 Brazilian E-commerce')
st.caption('Dashboard Creator : M Faqih')
