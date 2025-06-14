import streamlit as st
import json

st.title("🔄 Đổi mật khẩu")

if "recovery_user" not in st.session_state:
    st.warning("Không có thông tin khôi phục. Vui lòng quay lại trang Quên mật khẩu.")
    st.markdown("[Quay lại](./Quên_mật_khẩu)")
else:
    new_password = st.text_input("Nhập mật khẩu mới", type="password")
    confirm = st.text_input("Xác nhận mật khẩu mới", type="password")

    if st.button("Đổi mật khẩu"):
        if new_password != confirm:
            st.error("Mật khẩu không khớp!")
        else:
            with open("users.json", "r") as f:
                users = json.load(f)
            for user in users:
                if user["username"] == st.session_state.recovery_user["username"]:
                    user["password"] = new_password
            with open("users.json", "w") as f:
                json.dump(users, f, indent=2)
            st.success("Đổi mật khẩu thành công!")
            st.switch_page("pages/1_Đăng_nhập.py")
