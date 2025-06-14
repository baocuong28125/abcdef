import streamlit as st
import json

st.title("🔐 Đăng Nhập")
st.markdown("<style>body { background-color: #f5f5f5; }</style>", unsafe_allow_html=True)

username = st.text_input("Tài khoản")
password = st.text_input("Mật khẩu", type="password")

if st.button("Đăng nhập"):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
        user = next((u for u in users if u["username"] == username and u["password"] == password), None)
        if user:
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tài khoản hoặc mật khẩu.")
    except FileNotFoundError:
        st.error("Chưa có tài khoản nào được tạo.")

st.markdown("[❓ Quên mật khẩu?](./Quên_mật_khẩu)")
st.markdown("[➕ Tạo tài khoản mới](./Tạo_tài_khoản)")
