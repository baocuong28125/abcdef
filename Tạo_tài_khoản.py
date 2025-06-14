import streamlit as st
import json
from pathlib import Path

USER_FILE = Path("users.json")

def save_user(user):
    if USER_FILE.exists():
        with open(USER_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(user)
    with open(USER_FILE, "w") as f:
        json.dump(data, f, indent=2)

st.title("🔐 Tạo Tài Khoản")

username = st.text_input("Tên tài khoản")
phone = st.text_input("Số điện thoại")
password = st.text_input("Mật khẩu", type="password")
confirm_password = st.text_input("Xác nhận mật khẩu", type="password")

st.markdown("[👉 Đăng nhập](./Đăng_nhập)")

if st.button("Đăng ký"):
    if password != confirm_password:
        st.error("Mật khẩu không khớp!")
    elif not username or not phone or not password:
        st.error("Vui lòng nhập đầy đủ thông tin.")
    else:
        save_user({"username": username, "phone": phone, "password": password})
        st.success("✅ Tạo tài khoản thành công!")
        st.switch_page("pages/3_Đăng_ký_thành_công.py")
