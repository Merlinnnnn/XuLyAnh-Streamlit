import sys
import tkinter
from io import StringIO
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
import cv2
import numpy as np
import pandas as pd
from PIL import Image

from Chapter03 import Gradient, Histogram, Logarit, MedianFilter, Negative, PiecewiseLinear, Power, Sharpen
from Chapter09 import Boundary, ConnectedComponent, CountRice, Dilation, Erosion, HoleFill, MyConnectedComponent, OpeningClosing
from Chapter04 import FrequencyFilter, RemoveMoire, Spectrum, CreateNotchRejectFilter, DrawNotchRejectFilter
from Chapter05 import CreateMotionfilter, CreateMotionNoise, CreateInverseMotionfilter, DenoiseMotion
import streamlit as st
from streamlit_option_menu import option_menu

def onOpen():
    global ftypes
    ftypes = [('Images', '*.jpg *.tif *.bmp *.gif *.png')]
    dlg = Open(filetypes=ftypes)
    fl = dlg.show()

def onSave():
    dlg = SaveAs( filetypes=ftypes);
    fl = dlg.show()
    if fl != '':
        cv2.imwrite(fl, imgout)

#Chapter 4
def onSpectrum():
    if imgin is None:
        return
    global imgout
    imgout = Spectrum(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onFrequencyFilter():
    if imgin is None:
        return
    global imgout
    imgout = FrequencyFilter(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onCreateNotchRejectFilter():
    global imgout
    imgout = CreateNotchRejectFilter()
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onDrawNotchRejectFilter():
    if imgin is None:
        return
    global imgout
    imgout = DrawNotchRejectFilter()
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onRemoveMoire():
    global imgout
    imgout = RemoveMoire(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

st.title("Morphological Image Processing")
col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    option = st.selectbox("Function",("None", "Spectrum", "FrequencyFilter", "CreateNotchRejectFilter", "DrawNotchRejectFilter", "RemoveMoire"))

    if option == "None":
        st.write("Vui lòng chọn option!")
    else:
        st.write("")
    uploaded_file = st.file_uploader("Upload Image")
    if uploaded_file is not None:
        st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
        st.write("Tên của ảnh: ", uploaded_file.name)
        st.write("---------------------------------------------------------------")
    if option == "Spectrum":
        st.write(
            "Spectrum dựa vào việc sử dụng các thuật toán toán học phù hợp để thao tác và nâng cao dữ liệu được ghi lại thông qua quá trình tạo ảnh quang phổ.")
    elif option == "FrequencyFilter":
        st.write(
            "FrequencyFilter được sử dụng để làm mịn và sắc nét hình ảnh bằng cách loại bỏ các thành phần tần số cao hoặc thấp.")
    elif option == "CreateNotchRejectFilter":
        st.write(
            "CreateNotchRejectFilter được sử dụng trong xử lý hình ảnh để loại bỏ các thành phần tần số cụ thể, thường liên quan đến nhiễu hoặc nhiễu không mong muốn.")
    elif option == "DrawNotchRejectFilter":
        st.write(
            "DrawNotchRejectFilter bao gồm việc trực quan hóa đáp ứng tần số của nó, cho biết cách bộ lọc suy giảm hoặc vượt qua các tần số khác nhau.")
    elif option == "RemoveMoire":
        st.write(
            "RemoveMoire là các họa tiết nhiễu không mong muốn có thể xuất hiện trong ảnh, đặc biệt khi có xung đột giữa lưới điểm ảnh của cảm biến hình ảnh và họa tiết trong cảnh được chụp")
    else:
        st.write("")
with col2:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Input', use_column_width=True)
        img_array = np.array(image)
        cv2.imwrite('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/out.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        imgin = cv2.imread('out.jpg', cv2.IMREAD_GRAYSCALE)
    else:
        #image = Image.open('nen-trang-47.jpg')
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Output', use_column_width=True)
    if option == "Spectrum":
        onSpectrum()
    elif option == "FrequencyFilter":
        onFrequencyFilter()
    elif option == "CreateNotchRejectFilter":
        onCreateNotchRejectFilter()
    elif option == "DrawNotchRejectFilter":
        onDrawNotchRejectFilter()
    elif option == "RemoveMoire":
        onRemoveMoire()
    else:
        st.write("")
with col2:
    if option == "None":
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Input', use_column_width=True)
    else:
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/out1.jpg')
        st.image(image, caption='Output', use_column_width=True)

        
        

