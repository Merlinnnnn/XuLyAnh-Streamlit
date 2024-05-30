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
from Chapter04 import FrequencyFilter, RemoveMoire, Spectrum
from Chapter05 import CreateMotionNoise, DenoiseMotion
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

def onCreateMotionNoise():
    global imgout
    imgout = CreateMotionNoise(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onDenoiseMotion():
    global imgout
    temp = cv2.medianBlur(imgin, 7)
    imgout = DenoiseMotion(temp)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onDenoisestMotion():
    global imgout
    imgout = np.array(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

st.title("Morphological Image Processing")
col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    option = st.selectbox("Function",("None", "CreateMotionNoise", "DenoiseMotion", "DenoisestMOtion"))

    if option == "None":
        st.write("Vui lòng chọn option!")
    else:
        st.write("")
    uploaded_file = st.file_uploader("Upload Image")
    if uploaded_file is not None:
        st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
        st.write("Tên của ảnh: ", uploaded_file.name)
        st.write("---------------------------------------------------------------")
    if option == "CreateMotionNoise":
        st.write(
            "Nhiễu chuyển động là một hiệu ứng thường được áp dụng trong xử lý ảnh để mô phỏng các tình huống như chuyển động. ")
        st.write("Bộ lọc này tạo ra một hiệu ứng làm mờ tương tự như khi một đối tượng chuyển động được quan sát trong một khoảng thời gian. Kết quả là một ảnh với hiệu ứng chuyển động được thêm vào, giúp tạo ra cảm giác của sự chuyển động trong ảnh.")
    elif option == "DenoiseMotion":
        st.write(
            "Làm rõ nhiễu áp dụng một bộ lọc ngược lại để loại bỏ các hiệu ứng làm mờ tương tự như khi một đối tượng chuyển động được quan sát trong một khoảng thời gian. ")
        st.write(
            "Kết quả là một ảnh được làm sạch, giảm thiểu hiệu ứng chuyển động và tái tạo lại hình ảnh gốc với chất lượng tốt hơn.")
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
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Output', use_column_width=True)
    if option == "CreateMotionNoise":
        onCreateMotionNoise()
    elif option == "DenoiseMotion":
        onDenoiseMotion()
    elif option == "DenoisestMotion":
        onDenoisestMotion()
    else:
        st.write("")
with col2:
    if option == "None":
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Input', use_column_width=True)
    else:
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/out1.jpg')
        st.image(image, caption='Output', use_column_width=True)
        

