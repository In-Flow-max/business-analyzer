import streamlit as st

def get_marketing_metrics(col):
    st.subheader("Marketing Metrics")
    metrics = {}
    
    st.markdown("#### Market Position Assessment")
    market_known = st.radio("Do you know your market share?", ["Yes", "No", "Uncertain"])
    
    if market_known == "Yes":
        total_market = st.number_input(
            "Total Market Size ($)",
            help="Total addressable market value in dollars",
            min_value=0,
            value=1000000
        )
        your_revenue = st.number_input(
            "Your Annual Revenue ($)",
            help="Your company's annual revenue",
            min_value=0
        )
        if total_market > 0:
            metrics['market_share'] = (your_revenue / total_market) * 100
            st.info(f"Calculated Market Share: {metrics['market_share']:.1f}%")
            st.markdown(f"Industry Benchmark: 15-20% for market leaders")
    else:
        company_age = st.slider("Company Age (years)", 0, 50, 1)
        company_size = st.selectbox("Company Size", 
            ["Startup (1-10 employees)",
             "Small (11-50 employees)",
             "Medium (51-200 employees)",
             "Large (201+ employees)"])
        metrics['market_share'] = estimate_market_share(company_age, company_size)
        st.info(f"Estimated Market Share: {metrics['market_share']:.1f}%")

    st.markdown("#### Customer Acquisition")
    has_acquisition_data = st.radio("Do you track customer acquisition costs?", ["Yes", "No"])
    
    if has_acquisition_data == "Yes":
        cac = st.number_input(
            "Customer Acquisition Cost ($)",
            help="Total marketing spend / Number of new customers",
            min_value=0.0
        )
        roas = st.number_input(
            "Return on Ad Spend (ROAS)",
            help="Revenue generated / Marketing spend",
            min_value=0.0
        )
        metrics['customer_acquisition_cost'] = cac
        metrics['marketing_roi'] = roas * 100
    else:
        industry = st.selectbox("Industry", 
            ["B2B Software", "B2C E-commerce", "Professional Services", "Manufacturing"])
        metrics.update(get_industry_benchmarks(industry))

    return metrics

def estimate_market_share(age, size):
    size_factors = {
        "Startup (1-10 employees)": 0.1,
        "Small (11-50 employees)": 0.5,
        "Medium (51-200 employees)": 2.0,
        "Large (201+ employees)": 5.0
    }
    age_multiplier = min(1 + (age * 0.2), 3)
    return size_factors[size] * age_multiplier

def get_industry_benchmarks(industry):
    benchmarks = {
        "B2B Software": {
            "customer_acquisition_cost": 400,
            "marketing_roi": 250,
        },
        "B2C E-commerce": {
            "customer_acquisition_cost": 30,
            "marketing_roi": 400,
        },
        "Professional Services": {
            "customer_acquisition_cost": 200,
            "marketing_roi": 300,
        },
        "Manufacturing": {
            "customer_acquisition_cost": 600,
            "marketing_roi": 200,
        }
    }
    return benchmarks[industry]
