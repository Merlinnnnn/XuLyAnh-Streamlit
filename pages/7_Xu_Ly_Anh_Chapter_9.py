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

#Chapter 9
def onErosion():
    if imgin is None:
        return
    global imgout
    imgout = np.zeros(imgin.shape, np.uint8)
    Erosion(imgin, imgout)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onDilation():
    if imgin is None:
        return 
    global imgout
    imgout = np.zeros(imgin.shape, np.uint8)
    Dilation(imgin, imgout)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onOpeningClosing():
    if imgin is None:
        return 
    global imgout
    imgout = np.zeros(imgin.shape, np.uint8)
    OpeningClosing(imgin, imgout)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onBoundary():
    if imgin is None:
        return 
    global imgout
    imgout = Boundary(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHoleFill():
    if imgin is None:
        return 
    global imgout
    imgout = HoleFill(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onMyConnectedComponent():
    global imgout
    imgout = MyConnectedComponent(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onConnectedComponent():
    global imgout
    imgout = ConnectedComponent(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onCountRice():
    global imgout
    imgout = CountRice(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

st.title("Morphological Image Processing")
col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    option = st.selectbox("Function",("None", "Connected Component", "Count Rice"))

    if option == "None":
        st.write("Vui lòng chọn option!")
    else:
        st.write("")
    uploaded_file = st.file_uploader("Upload Image")
    if uploaded_file is not None:
        st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
        st.write("Tên của ảnh: ", uploaded_file.name)
        st.write("---------------------------------------------------------------")
    elif option == "Connected Component":
        st.write(
            "Kết nối thành phần chuyển đổi hình ảnh thành dạng nhị phân, sau đó đếm và gán màu cho các vùng kết nối.")
        st.write(
            "Kết quả trả về là hình ảnh với các thành phần liên thông được đánh số và thông tin về số lượng và kích thước của mỗi thành phần.")
    elif option == "Count Rice":
        st.write(
            "Đếm hạt gạo áp dụng một loạt các phép biến đổi hình thái học và lọc để làm sạch và phát hiện các hạt gạo.")
        st.write(
            "Sau đó, nó đếm và gán nhãn cho các hạt gạo và loại bỏ những hạt nhỏ. Kết quả trả về là hình ảnh với số lượng và thông tin về các hạt gạo đã đếm được.")
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
    if option == "Connected Component":
        onConnectedComponent()
    elif option == "Count Rice":
        onCountRice()
    else:
        st.write("")
with col2:
    if option == "None":
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Output', use_column_width=True)
    else:
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/out1.jpg')
        st.image(image, caption='Output', use_column_width=True)
        

