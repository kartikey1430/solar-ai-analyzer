import streamlit as st
import time  # ⏱️ For performance metrics

# Set page config first
st.set_page_config(page_title="☀️ Solar Rooftop Analyzer", layout="wide")

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from PIL import Image
from image_analysis import analyze_image
from solar_calculations import estimate_solar_capacity, estimate_roi

# Header
st.markdown("""
    <h1 style='text-align: center; color: #FFA500;'>🔆 Solar Rooftop Analysis Tool</h1>
    <p style='text-align: center; font-size: 18px;'>Upload a rooftop satellite image to assess its solar installation potential using AI</p>
    <hr>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload Rooftop Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, caption="📸 Uploaded Image", use_column_width=True)

    # ⏱️ Start timer
    start_time = time.time()

    with st.spinner("🧠 Analyzing rooftop with AI..."):
        analysis_result = analyze_image(image)

    elapsed_time = time.time() - start_time  # ⏱️ End timer

    with col2:
        st.subheader("🧾 Rooftop Analysis Summary")
        if "error" in analysis_result:
            st.error(analysis_result["error"])
        else:
            st.success("✅ Analysis completed successfully")

            with st.expander("🔍 View Full AI Analysis"):
                st.write(analysis_result["raw_output"])

            area = analysis_result.get("estimated_area_sqm", 100)

            capacity = estimate_solar_capacity(area)
            roi = estimate_roi(capacity["capacity_kw"])

            st.markdown("### ☀️ Estimated Solar Capacity")
            st.markdown(f"""
                - **Estimated Panel Count**: `{capacity["panel_count"]}`
                - **System Capacity**: `{capacity["capacity_kw"]} kW`
            """)

            st.markdown("### 💰 ROI & Cost Estimation")
            st.markdown(f"""
                - **Installation Cost**: ₹ `{roi["estimated_cost_inr"]:,}`
                - **Annual Savings**: ₹ `{roi["annual_savings_inr"]:,}`
                - **Payback Period (ROI)**: `{roi["roi_years"]} years`
            """)

            # Show processing time
            st.markdown("### ⏱️ Performance Metrics")
            st.info(f"🕒 Total Processing Time: `{elapsed_time:.2f} seconds`")

# Footer
st.markdown("""<hr style="margin-top: 2em;">""", unsafe_allow_html=True)
st.caption("🔧 Built by Kartikey Agrawal • Powered by Claude 3 Sonnet & Streamlit")
