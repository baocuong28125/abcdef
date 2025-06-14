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
    "iPhone 15": {
        "price": 23990000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/305659/iphone-15-pink-thumb-600x600.jpg"
    },
    "iPhone 15 Pro Max": {
        "price": 33990000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/303891/iphone-15-pro-max-blue-thumbnew-600x600.jpg"
    },
    "MacBook Air M2": {
        "price": 28990000,
        "image": "https://cdn.tgdd.vn/Products/Images/44/299570/macbook-air-m2-2023-8-core-cpu-256gb-thumb-600x600.jpg"
    },
    "MacBook Pro M3": {
        "price": 43990000,
        "image": "https://cdn.tgdd.vn/Products/Images/44/317922/macbook-pro-14-m3-2023-xam-thumb-600x600.jpg"
    },
    "iPad Gen 10": {
        "price": 10490000,
        "image": "https://cdn.tgdd.vn/Products/Images/522/289577/ipad-gen-10-silver-thumb-600x600.jpg"
    },
    "Apple Watch Series 9": {
        "price": 10990000,
        "image": "https://cdn.tgdd.vn/Products/Images/7077/315693/apple-watch-s9-41mm-vien-nhom-day-silicone-hong-thumb-1-600x600.jpg"
    },
    "Apple Vision Pro (Concept)": {
        "price": 79990000,
        "image": "https://cdn.pocket-lint.com/r/s/970x/assets/images/165415-headphones-review-apple-vision-pro-review-images-image1-0b9whr1kgq.jpg"
    },
    "Apple Pencil Gen 2": {
        "price": 3290000,
        "image": "https://cdn.tgdd.vn/Products/Images/7077/215386/apple-pencil-2nd-gen-apple-thumb-600x600.jpg"
    }
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
