import streamlit as st

# --- Thiết lập trang ---
st.set_page_config(page_title="Cửa hàng Apple Mini", layout="wide")

# --- CSS tùy chỉnh cho màu nền xám/trắng/đen ---
st.markdown("""
    <style>
    body {
        background-color: #f2f2f2;
        color: #000000;
    }
    .stButton>button {
        background-color: #333333;
        color: white;
        border-radius: 5px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #555555;
        color: #ffffff;
    }
    .stAlert {
        background-color: #e6e6e6;
        border-left: 5px solid #000000;
    }
    </style>
""", unsafe_allow_html=True)

# --- Danh sách sản phẩm (giá VNĐ) ---
products = {
    "iPhone 15": {"price": 23990000, "image": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone15-select-2023?wid=940&hei=1112&fmt=png-alpha&.v=1692927179096"},
    "MacBook Air M2": {"price": 28990000, "image": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-m2-hero-202206?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1653493200207"},
    "AirPods Pro (2nd Gen)": {"price": 5790000, "image": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MQD83?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1660803972361"},
}

# --- Session state để lưu giỏ hàng ---
if "cart" not in st.session_state:
    st.session_state.cart = {}

# --- Tiêu đề ---
st.title("🛒 CỬA HÀNG APPLE MINI VIỆT NAM")

# --- Hiển thị danh sách sản phẩm ---
cols = st.columns(3)
for i, (name, info) in enumerate(products.items()):
    with cols[i % 3]:
        st.image(info["image"], width=220)
        st.markdown(f"**{name}**")
        st.write(f"💰 Giá: {info['price']:,} VNĐ")
        if st.button(f"➕ Thêm vào giỏ - {name}", key=f"add_{name}"):
            st.session_state.cart[name] = st.session_state.cart.get(name, 0) + 1
            st.success(f"✅ Đã thêm **{name}** vào giỏ hàng!")

st.markdown("---")

# --- Hiển thị giỏ hàng ---
st.header("🛍️ GIỎ HÀNG")
total = 0
if st.session_state.cart:
    for name, quantity in st.session_state.cart.items():
        price = products[name]["price"]
        st.write(f"- {name} x {quantity} = {price * quantity:,} VNĐ")
        total += price * quantity
    st.markdown(f"### 🧾 Tổng cộng: {total:,} VNĐ")
    if st.button("💳 Thanh toán"):
        st.success("🎉 Thanh toán thành công! Cảm ơn bạn đã mua hàng.")
        st.session_state.cart = {}
else:
    st.info("Giỏ hàng của bạn đang trống. Hãy chọn sản phẩm để thêm vào.")
