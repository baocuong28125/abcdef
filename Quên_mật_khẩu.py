import streamlit as st
import json

st.title("📱 Quên mật khẩu")

username = st.text_input("Tài khoản đã đăng ký")
phone = st.text_input("Số điện thoại")

if st.button("Gửi mã xác nhận qua SĐT"):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
        user = next((u for u in users if u["username"] == username and u["phone"] == phone), None)
        if user:
            st.success("Mã xác nhận đã gửi! (Giả lập)")
            st.session_state.recovery_user = user
            st.switch_page("pages/5_Đổi_mật_khẩu.py")
        else:
            st.error("Không tìm thấy tài khoản với thông tin đã nhập.")
    except:
        st.error("Không tìm thấy dữ liệu.")

