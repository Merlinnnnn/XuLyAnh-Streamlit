import sys
import tkinter
from io import StringIO
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
import cv2
import numpy as np
import pandas as pd
from PIL import Image

from Chapter03 import BoxFilter,MyBoxFilter, Gradient, Histogram, Logarit, MedianFilter, Negative, Power, Sharpen, HistEqual, LocalHist, HistStat, Threshold, MedianFilter, Sharpen, Gradient, PiecewiseLinear, HistEqualColor
import streamlit as st
from streamlit_option_menu import option_menu


ftypes = [('Images', '*.jpg *.tif *.bmp *.gif *.png')]
img_color = None
def onOpen():
    global ftypes
    dlg = Open(filetypes=ftypes)
    fl = dlg.show()

def onSave():
    dlg = SaveAs( filetypes=ftypes);
    fl = dlg.show()
    if fl != '':
        cv2.imwrite(fl, imgout)

def onNegative():
    if imgin is None:
        return
    global imgout
    imgout = Negative(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onLogarit():
    if imgin is None:
        return
    global imgout
    imgout = Logarit(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onPower():
    if imgin is None:
        return
    global imgout
    imgout = Power(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onPiecewiseLinear():
    if imgin is None:
        return
    global imgout
    imgout = PiecewiseLinear(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHistogram():
    if imgin is None:
        return
    global imgout
    imgout = Histogram(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHistEqual():
    if imgin is None:
        return
    global imgout
    imgout = HistEqual(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHistEqualColor():
    if img_color is None:
        return
    global imgout
    if img_color.ndim == 3:
        imgout = HistEqualColor(img_color)
    else:  
        imgout = img_color
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))


def onLocalHist():
    if imgin is None:
        return
    global imgout
    imgout = LocalHist(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onHistStat():
    if imgin is None:
        return
    global imgout
    imgout = HistStat(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onMyBoxFilter():
    if imgin is None:
        return
    global imgout
    imgout = MyBoxFilter(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onBoxFilter():
    if imgin is None:
        return
    global imgout
    imgout = BoxFilter(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onThreshold():
    if imgin is None:
        return
    global imgout
    imgout = Threshold(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onMedianFilter():
    if imgin is None:
        return
    global imgout
    imgout = MedianFilter(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onSharpen():
    if imgin is None:
        return
    global imgout
    imgout = Sharpen(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))

def onGradient():
    if imgin is None:
        return
    global imgout
    imgout = Gradient(imgin)
    img_array = np.array(imgout)
    cv2.imwrite('out1.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))


st.title("Morphological Image Processing")
col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    option = st.selectbox("Function",("None", "Negative", "Logarit", "Power", "PiecewiseLinear", "Histogram",
                                        "HistEqual", "HistEqualColor", "LocalHist", "HistStat", "MyBoxFilter", "BoxFilter", "Threshold", "MedianFilter", "Sharpen", "Gradient"))

    if option == "None":
        st.write("Vui lòng chọn option!")
    else:
        st.write("")
    uploaded_file = st.file_uploader("Upload Image")
    if uploaded_file is not None:
        st.write("Kích thước của file ảnh là: ", uploaded_file.size, "Bytes")
        st.write("Tên của ảnh: ", uploaded_file.name)
        st.write("---------------------------------------------------------------")
    if option == "Negative":
        st.write(
            "Negative là thuật toán xử lý ảnh negative được sử dụng để tạo ra bản đảo màu sắc của một ảnh.")
        st.write(
            "Quá trình này đơn giản là đảo ngược giá trị màu sắc của từng pixel trong ảnh, từ giá trị ban đầu sang giá trị đối của nó")
    elif option == "Logarit":
        st.write(
            "Logarit là thuật toán sử dụng hàm logarithm để tăng độ tương phản của ảnh bằng cách giảm độ sáng của các vùng màu sắc sáng hơn. ")
    elif option == "Power":
        st.write(
            "Thuật toán xử lý ảnh dựa trên hàm mũ được gọi là thuật toán Power hay còn được gọi là thuật toán Gamma.")
        st.write(" Thuật toán này được sử dụng để điều chỉnh độ tương phản của ảnh bằng cách tăng hoặc giảm độ sáng của các vùng màu sắc khác nhau.")
    elif option == "Histogram":
        st.write(
            "Là thuật toán tính toán tần suất xuất hiện của các mức xám trong ảnh.")
    elif option == "HistEqual":
        st.write(
            "Histogram Equalization là thuật toán tăng cường độ tương phản của ảnh bằng cách sử dụng phân phối tần suất của các mức xám để tăng độ phân giải của ảnh")
    elif option == "HistEqualColor":
        st.write(
            "Cũng tương tự như Histogram Equalization, Histogram Equalization Color áp dụng cho ảnh màu RGB")
    elif option == "LocalHist":
        st.write(
            "Trong xử lý hình ảnh kỹ thuật số, biểu đồ được sử dụng để biểu diễn đồ họa của hình ảnh kỹ thuật số. Biểu đồ là một biểu đồ theo số pixel cho mỗi giá trị âm.")
        st.write(
            "Ngày nay, biểu đồ hình ảnh có mặt trong máy ảnh kỹ thuật số. Các nhiếp ảnh gia sử dụng chúng để xem sự phân bổ tông màu được chụp.")
    elif option == "HistStat":
        st.write(
            "Biểu đồ histogram ảnh là loại biểu đồ histogram được sử dụng để biểu diễn đồ họa về phân phối tông màu trong một hình ảnh kỹ thuật số.")
        st.write(
            "Trong ngữ cảnh xử lý ảnh, histogram của một hình ảnh thường đề cập đến biểu đồ histogram của các giá trị độ sáng pixel.")
    elif option == "MyBoxFilter":
        st.write(
            "MyBoxFilter là một loại bộ lọc xử lý hình ảnh hoạt động bằng cách thay thế từng pixel trong ảnh bằng giá trị trung bình của các pixel lân cận.")
        st.write(
            "Quá trình này được lặp lại cho từng pixel trong ảnh, dẫn đến phiên bản ảnh gốc bị mờ, mịn. Bộ lọc hộp thường được sử dụng để giảm nhiễu và giảm lượng chi tiết trong hình ảnh.")
    elif option == "BoxFilter":
        st.write(
            "BoxFilter là một loại bộ lọc xử lý hình ảnh hoạt động bằng cách thay thế từng pixel trong ảnh bằng giá trị trung bình của các pixel lân cận.")
        st.write(
            "Quá trình này được lặp lại cho từng pixel trong ảnh, dẫn đến phiên bản ảnh gốc bị mờ, mịn.")
    elif option == "Threshold":
        st.write(
            "Threshold là phương pháp phân đoạn hình ảnh đơn giản nhất. Nó đóng một vai trò quan trọng trong xử lý hình ảnh vì nó cho phép phân đoạn và trích xuất thông tin quan trọng từ hình ảnh.")
    elif option == "MedianFilter":
        st.write(
            "MedianFilter là một kỹ thuật lọc kỹ thuật số phi tuyến tính, thường được sử dụng để loại bỏ nhiễu khỏi hình ảnh hoặc tín hiệu. Việc giảm nhiễu như vậy là một bước tiền xử lý điển hình để cải thiện kết quả của quá trình xử lý sau này.")
        st.write(
            "MedianFilter được sử dụng rất rộng rãi trong xử lý hình ảnh kỹ thuật số vì trong những điều kiện nhất định, nó bảo toàn các cạnh trong khi loại bỏ nhiễu, cũng có ứng dụng trong xử lý tín hiệu.")
    elif option == "Sharpen":
        st.write(
            "Mục tiêu của việc làm sắc nét hình ảnh là tăng cường độ dốc của cạnh mà không tạo ra các hiệu ứng hào quang, trong khi mục tiêu của thuật toán khử nhiễu hình ảnh là giảm nhiễu trong khi vẫn giữ được các cạnh của hình ảnh.")
    elif option == "Gradient":
        st.write(
            "Gradient giúp phát hiện các cạnh và ranh giới bằng cách đo sự thay đổi cường độ ở các pixel liền kề.")
        st.write(
            " Tính toán độ dốc liên quan đến các thuật toán và bộ lọc và có các ứng dụng trong thị giác máy tính, phân tích hình ảnh và học máy. Nó đòi hỏi phải xem xét cẩn thận các yếu tố như nhiễu hình ảnh, độ phân giải và lựa chọn bộ lọc để làm mịn hình ảnh.")
    elif option == "PiecewiseLinear":
        st.write(
            "PiecewiseLinear là loại chuyển đổi mức xám được sử dụng để nâng cao hình ảnh. Đây là một phương pháp miền không gian.")
        st.write(
            "Nó được sử dụng để xử lý hình ảnh sao cho kết quả phù hợp hơn bản gốc cho một ứng dụng cụ thể.")
    else:
        st.write("")
with col2:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Input', use_column_width=True)
        img_array = np.array(image)
        cv2.imwrite('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/out.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        imgin = cv2.imread('out.jpg', cv2.IMREAD_GRAYSCALE)
        img_color = cv2.imread('out.jpg')
    else:
        #image = Image.open('nen-trang-47.jpg')
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Output', use_column_width=True)
    if option == "Negative":
        onNegative()
    elif option == "Logarit":
        onLogarit()
    elif option == "Power":
        onPower()
    elif option == "PiecewiseLinear":
        onPiecewiseLinear()
    elif option == "Histogram":
        onHistogram()
    elif option == "HistEqual":
        onHistEqual()
    elif option == "HistEqualColor":
        onHistEqualColor()
    elif option == "LocalHist":
        onLocalHist()
    elif option == "HistStat":
        onHistStat()
    elif option == "MyBoxFilter":
        onMyBoxFilter()
    elif option == "BoxFilter":
        onBoxFilter()
    elif option == "Threshold":
        onThreshold()
    elif option == "MedianFilter":
        onMedianFilter()
    elif option == "Sharpen":
        onSharpen()
    elif option == "Gradient":
        onGradient()
    else:
        st.write("")
with col2:
    if option == "None":
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/nen-trang-47.jpg')
        st.image(image, caption='Output', use_column_width=True)
    else:
        image = Image.open('C:/Users/Hi/Desktop/2023-2024/XuLyAnh/CuoiKy/Project/out1.jpg')
        st.image(image, caption='Output', use_column_width=True)
