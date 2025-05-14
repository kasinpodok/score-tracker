import streamlit as st

PASSWORD = "1234"

if "scores" not in st.session_state:
    st.session_state.scores = {
        "กลุ่ม A": 0,
        "กลุ่ม B": 0,
        "กลุ่ม C": 0
    }

st.title("📊 ระบบควบคุมคะแนนกลุ่ม")

st.header("📌 คะแนนปัจจุบัน")
for group, score in st.session_state.scores.items():
    st.write(f"🔸 {group}: {score} คะแนน")

st.markdown("---")

st.header("🔐 ส่วนควบคุม (สำหรับผู้ควบคุม)")

password_input = st.text_input("กรอกรหัสผ่านเพื่อควบคุม:", type="password")

if password_input == PASSWORD:
    st.success("✅ เข้าสู่ระบบสำเร็จ!")
    selected_group = st.selectbox("เลือกกลุ่ม", list(st.session_state.scores.keys()))
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ เพิ่ม 1 คะแนน"):
            st.session_state.scores[selected_group] += 1
    with col2:
        if st.button("➖ ลด 1 คะแนน"):
            st.session_state.scores[selected_group] -= 1
else:
    if password_input:
        st.error("❌ รหัสไม่ถูกต้อง")
