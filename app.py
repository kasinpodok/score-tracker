import streamlit as st

# รหัสผ่านและสิทธิ์
PASSWORDS = {
    "admin123": "admin",
    "groupa": "กลุ่ม A",
    "groupb": "กลุ่ม B",
    "groupc": "กลุ่ม C"
}

# เริ่มต้นคะแนน
if "scores" not in st.session_state:
    st.session_state.scores = {
        "กลุ่ม A": 0,
        "กลุ่ม B": 0,
        "กลุ่ม C": 0
    }

# รับรหัสผ่าน
st.title("📊 ระบบดูและควบคุมคะแนน")
password_input = st.text_input("กรอกรหัสผ่านเพื่อเข้าสู่ระบบ:", type="password")

if password_input in PASSWORDS:
    role = PASSWORDS[password_input]
    st.success(f"✅ เข้าสู่ระบบในสิทธิ์: {role}")
    
    if role == "admin":
        # แสดงคะแนนทุกกลุ่ม
        st.header("📌 คะแนนรวมทุกกลุ่ม")
        for group, score in st.session_state.scores.items():
            st.write(f"🔸 {group}: {score} คะแนน")
        
        # ควบคุมคะแนน
        st.header("🛠️ ควบคุมคะแนน")
        selected_group = st.selectbox("เลือกกลุ่ม", list(st.session_state.scores.keys()))
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ เพิ่ม 1 คะแนน"):
                st.session_state.scores[selected_group] += 1
        with col2:
            if st.button("➖ ลด 1 คะแนน"):
                st.session_state.scores[selected_group] -= 1
    else:
        # ผู้ใช้ทั่วไป เห็นคะแนนเฉพาะกลุ่มตัวเอง
        group_score = st.session_state.scores[role]
        st.header(f"📌 คะแนนของคุณ ({role})")
        st.write(f"🔹 {role}: {group_score} คะแนน")

else:
    if password_input:
        st.error("❌ รหัสไม่ถูกต้อง")
