import streamlit as st
from PIL import Image
import pickle




#st.video('video.mp4')
st.markdown("![Alt Text](https://gifyu.com/images/video1f6e16e39cc814b9.gif)")

# https://gifyu.com/images/video1f6e16e39cc814b9.gif
#st.image('prof-serdc-01.jpg') # загружаем изображение   28022022_1

#загружаем наш файл модели - функция будет возвращать обученную модель
def load ():
    with open('model.pcl', 'rb') as fid:
        return pickle.load(fid)

st.title('Характеристики пользователя')


age = st.slider('Возраст, лет', 25, 100, 45)

height = st.slider('Рост, cm', 150, 200, 170)

weight = st.slider('Вес, kg', 45, 160, 80)


lc, rc = st.columns(2)

ap_hi = lc.selectbox('Систолическое давление: ', (80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250), key = 'ap_hi')

ap_lo = rc.selectbox('Диастолическое давление: ', (40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150), key = 'ap_lo')

#st.write('возраст {}'.format(age))
#st.write('рост {}'.format(height))
#st.write('вес {}'.format(weight))
#st.write('Сист давл {}'.format(ap_hi))
#st.write('Диаст давл {}'.format(ap_lo))

st.write('### Предсказание: ')

st.sidebar.header('Заданные пользователем параметры: ')

cholesterol = st.sidebar.selectbox('cholesterol level', (1, 2, 3), key = 'cholesterol')

gluc = st.sidebar.selectbox('glucosa level', (1, 2, 3), key = 'gluc')

gender = st.sidebar.radio('Gender', ('M', 'F'), key = 'gender')

smoke = st.sidebar.radio('Smoke', ('Yes', 'No'), key = 'smoke')

alco = st.sidebar.radio('Alcogole', ('Yes', 'No'), key = 'alco')

active = st.sidebar.radio('Active', ('Yes', 'No'), key = 'active')

#cardio = st.sidebar.radio('Cardio', ('Yes', 'No'), key = 'cardio')

translation = {
    'M': 2,
    'F': 1,
}
translation_s = {
    'Yes': 2,
    'No': 1,
}
translation_a = {
    'Yes': 2,
    'No': 1,
}
translation_act = {
    'Yes': 1,
    'No': 2,
}
#translation_card = {
   # 'Yes': 2,
   # 'No': 1,
#}

# выгружаем модель

model = load()

y_pr = model.predict_proba([[age, height, weight, ap_hi, ap_lo, cholesterol, gluc, translation[gender], translation_s[smoke], translation_a[alco], translation_act[active]]])[:, 1]

st.write(y_pr)
#%%

#%%

#%%

#%%

#%%
