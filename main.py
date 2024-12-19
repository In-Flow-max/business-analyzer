import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from data_quality import RecommendationAnalyzer 
st.set_page_config(
    page_title="Business Analysis Tool", 
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

class BusinessAnalysisTool:
    def __init__(self):
        self.score_weights = {
            'marketing': 0.15,
            'sales': 0.20,
            'product_delivery': 0.20,
            'operational_efficiency': 0.15,
            'financial_health': 0.20,
            'people': 0.10
        }
    
    def analyze_marketing(self, data):
        metrics = {
            'audience_metrics': {
                'score': 0,
                'criteria': {
                    'total_addressable_audience': self._normalize_audience(data.get('total_addressable_audience', 0)),
                    'campaign_effectiveness': data.get('campaign_effectiveness', 0) / 10,
                    'conversion_rate': data.get('conversion_rate', 0) / 100 * 10
                }
            },
            'performance_metrics': {
                'score': 0,
                'criteria': {
                    'cac': self._normalize_cac(data.get('customer_acquisition_cost', 0)),
                    'marketing_roi': self._normalize_roi(data.get('marketing_roi', 0))
                }
            }
        }
        return self._calculate_category_score(metrics)

    def analyze_sales(self, data):
        metrics = {
            'revenue_metrics': {
                'score': 0,
                'criteria': {
                    'revenue_growth': data.get('revenue_growth', 0) / 100 * 10,
                    'recurring_revenue': data.get('recurring_revenue_percentage', 0) / 100 * 10,
                    'average_deal_size': self._normalize_deal_size(data.get('average_deal_size', 0))
                }
            },
            'pipeline_health': {
                'score': 0,
                'criteria': {
                    'conversion_rate': data.get('pipeline_conversion', 0) / 100 * 10,
                    'sales_cycle': self._normalize_sales_cycle(data.get('sales_cycle_length', 0)),
                    'pipeline_coverage': data.get('pipeline_coverage', 0) / 4 * 10
                }
            },
            'customer_metrics': {
                'score': 0,
                'criteria': {
                    'customer_retention': data.get('retention_rate', 0) / 100 * 10,
                    'customer_satisfaction': data.get('satisfaction_score', 0) / 100 * 10
                }
            }
        }
        return self._calculate_category_score(metrics)

    def analyze_product_delivery(self, data):
        metrics = {
            'quality_metrics': {
                'score': 0,
                'criteria': {
                    'defect_rate': (100 - data.get('defect_rate', 0)) / 100 * 10,
                    'customer_satisfaction': data.get('product_satisfaction', 0) / 100 * 10,
                    'service_level': data.get('sla_compliance', 0) / 100 * 10
                }
            },
            'delivery_efficiency': {
                'score': 0,
                'criteria': {
                    'on_time_delivery': data.get('on_time_delivery', 0) / 100 * 10,
                    'delivery_cost': self._normalize_delivery_cost(data.get('delivery_cost', 0)),
                    'cycle_time': self._normalize_cycle_time(data.get('cycle_time', 0))
                }
            },
            'scalability': {
                'score': 0,
                'criteria': {
                    'capacity_utilization': self._normalize_utilization(data.get('capacity_utilization', 0)),
                    'automation_level': data.get('automation_percentage', 0) / 100 * 10
                }
            }
        }
        return self._calculate_category_score(metrics)

    def analyze_operational_efficiency(self, data):
        metrics = {
            'process_efficiency': {
                'score': 0,
                'criteria': {
                    'process_automation': data.get('process_automation', 0) / 100 * 10,
                    'resource_utilization': data.get('resource_utilization', 0) / 100 * 10,
                    'error_rate': (100 - data.get('error_rate', 0)) / 100 * 10
                }
            },
            'cost_efficiency': {
                'score': 0,
                'criteria': {
                    'operating_margin': self._normalize_margin(data.get('operating_margin', 0)),
                    'overhead_ratio': (100 - data.get('overhead_ratio', 0)) / 100 * 10,
                    'cost_per_unit': self._normalize_unit_cost(data.get('cost_per_unit', 0))
                }
            },
            'infrastructure': {
                'score': 0,
                'criteria': {
                    'tech_stack': data.get('tech_stack_rating', 0) / 10,
                    'scalability_rating': data.get('infrastructure_scalability', 0) / 10
                }
            }
        }
        return self._calculate_category_score(metrics)

    def analyze_financial_health(self, data):
        metrics = {
            'profitability': {
                'score': 0,
                'criteria': {
                    'gross_profit_margin': self._normalize_margin(data.get('gross_profit_margin', 0)),
                    'net_profit_margin': self._normalize_margin(data.get('net_profit_margin', 0)),
                    'operating_margin': self._normalize_margin(data.get('operating_margin', 0))
                }
            },
            'liquidity': {
                'score': 0,
                'criteria': {
                    'current_ratio': self._normalize_ratio(data.get('current_ratio', 0)),
                    'quick_ratio': self._normalize_ratio(data.get('quick_ratio', 0)),
                    'cash_flow_operations': self._normalize_cash_flow(data.get('cash_flow_operations', 0))
                }
            },
            'efficiency': {
                'score': 0,
                'criteria': {
                    'inventory_turnover': self._normalize_turnover(data.get('inventory_turnover', 0)),
                    'days_sales_outstanding': self._normalize_dso(data.get('days_sales_outstanding', 0)),
                    'debt_to_equity': self._normalize_leverage(data.get('debt_to_equity', 0))
                }
            }
        }
        return self._calculate_category_score(metrics)
    def analyze_people(self, data):
        metrics = {
            'talent_metrics': {
                'score': 0,
                'criteria': {
                    'employee_satisfaction': data.get('employee_satisfaction', 0) / 100 * 10,
                    'retention_rate': data.get('employee_retention', 0) / 100 * 10,
                    'skill_coverage': data.get('skill_coverage', 0) / 100 * 10
                }
            },
            'leadership': {
                'score': 0,
                'criteria': {
                    'experience': data.get('leadership_experience', 0) / 10,
                    'succession_planning': data.get('succession_readiness', 0) / 10,
                    'vision_clarity': data.get('vision_rating', 0) / 10
                }
            },
            'culture': {
                'score': 0,
                'criteria': {
                    'culture_score': data.get('culture_rating', 0) / 10,
                    'innovation_index': data.get('innovation_rating', 0) / 10
                }
            }
        }
        return self._calculate_category_score(metrics)

    def _calculate_category_score(self, metrics):
        category_score = 0
        for metric_group in metrics.values():
            metric_group['score'] = sum(metric_group['criteria'].values()) / len(metric_group['criteria'])
            category_score += metric_group['score']
        return category_score / len(metrics)

    def _normalize_cac(self, cac):
        if cac <= 0: return 0
        return min(10, max(0, 10 - (cac / 1000)))

    def _normalize_roi(self, roi):
        return min(10, max(0, roi / 30))

    def _normalize_tam(self, tam):
        if tam <= 0: return 0
        return min(10, max(0, tam / 1e9))

    def _normalize_deal_size(self, size):
        if size <= 0: return 0
        return min(10, max(0, size / 10000))

    def _normalize_sales_cycle(self, cycle):
        if cycle <= 0: return 0
        return min(10, max(0, 10 - (cycle / 30)))

    def _normalize_delivery_cost(self, cost):
        if cost <= 0: return 0
        return min(10, max(0, 10 - (cost / 1000)))

    def _normalize_cycle_time(self, time):
        if time <= 0: return 0
        return min(10, max(0, 10 - (time / 30)))

    def _normalize_utilization(self, utilization):
        return min(10, max(0, utilization / 10))

    def _normalize_margin(self, margin):
        return min(10, max(0, margin / 10))

    def _normalize_unit_cost(self, cost):
        if cost <= 0: return 0
        return min(10, max(0, 10 - (cost / 100)))

    def _normalize_ratio(self, ratio):
        if ratio <= 0: return 0
        return min(10, max(0, ratio * 5))

    def _normalize_audience(self, audience):
        if audience <= 0: return 0
        return min(10, max(0, (audience / 100000)))  # Scale based on audience size

    def _normalize_cash_flow(self, cash_flow):
        if cash_flow <= 0: return 0
        return min(10, max(0, (cash_flow / 100000)))  # Scale based on cash flow amount

    def _normalize_turnover(self, turnover):
        if turnover <= 0: return 0
        return min(10, max(0, (turnover / 12) * 10))  # 12 turns per year as benchmark

    def _normalize_dso(self, dso):
        if dso <= 0: return 0
        return min(10, max(0, 10 - (dso / 30)))  # Lower DSO is better

    def _normalize_leverage(self, ratio):
        if ratio <= 0: return 0
        return min(10, max(0, 10 - (ratio * 2)))  # Lower debt-to-equity is better
    def generate_comprehensive_report(self, data):
        scores = {
            'marketing': self.analyze_marketing(data),
            'sales': self.analyze_sales(data),
            'product_delivery': self.analyze_product_delivery(data),
            'operational_efficiency': self.analyze_operational_efficiency(data),
            'financial_health': self.analyze_financial_health(data),
            'people': self.analyze_people(data)
        }

        weighted_score = sum(scores[category] * self.score_weights[category] 
                           for category in scores)

        report = {
            'overall_score': round(weighted_score, 2),
            'category_scores': {k: round(v, 2) for k, v in scores.items()},
            'viability_rating': self._get_viability_rating(weighted_score),
            'scalability_rating': self._get_scalability_rating(scores),
            'recommendations': self._generate_recommendations(scores),
            'risk_assessment': self._assess_risks(scores)
        }

        return report

    def _get_viability_rating(self, score):
        if score >= 8.5: return "Excellent"
        elif score >= 7: return "Strong"
        elif score >= 5.5: return "Good"
        elif score >= 4: return "Fair"
        else: return "Poor"

    def _get_scalability_rating(self, scores):
        key_scalability_factors = [
            scores['operational_efficiency'],
            scores['product_delivery'],
            scores['financial_health']
        ]
        avg_scalability = sum(key_scalability_factors) / len(key_scalability_factors)

        if avg_scalability >= 8.5: return "Highly Scalable"
        elif avg_scalability >= 7: return "Scalable"
        elif avg_scalability >= 5.5: return "Moderately Scalable"
        elif avg_scalability >= 4: return "Limited Scalability"
        else: return "Poor Scalability"

    def _generate_recommendations(self, scores):
        recommendations = []
        for category, score in scores.items():
            if score < 6:
                recommendations.append(self._get_category_recommendation(category, score, scores))
        return recommendations

    def _get_category_recommendation(self, category, score, data):
        analyzer = RecommendationAnalyzer()
        quality_score = analyzer.calculate_data_quality_score(data, category)
    
        recommendations = []
    
        if category == 'marketing':
            # Market Share Based Recommendations
            market_share = data.get('market_share', 0)
            industry = data.get('industry', 'General')
            benchmark = self._get_industry_benchmark(industry, 'market_share')
            
            if market_share < benchmark:
                if data.get('brand_recognition', 0) < 50:
                    recommendations.append({
                        'text': "Increase brand awareness through targeted digital marketing and PR campaigns",
                        'priority': 'high'
                    })
                if data.get('customer_acquisition_cost', 0) > self._get_industry_benchmark(industry, 'cac'):
                    recommendations.append({
                        'text': "Optimize marketing channels to reduce customer acquisition costs",
                        'priority': 'high'
                    })
            
            # ROAS Based Recommendations
            roas = data.get('marketing_roi', 0)
            if roas < self._get_industry_benchmark(industry, 'roas'):
                recommendations.append({
                    'text': "Review and optimize marketing spend allocation across channels",
                    'priority': 'medium'
                })
    
        # Format recommendations with confidence scores
        formatted_recommendations = []
        for rec in recommendations:
            formatted_rec = analyzer.format_recommendation(
                rec['text'], 
                quality_score * (1.2 if rec['priority'] == 'high' else 1.0)
            )
            formatted_recommendations.append(formatted_rec)
    
        return formatted_recommendations

    def _get_industry_benchmark(self, industry, metric):
        benchmarks = {
            "B2B Software": {
                "total_addressable_audience": 100000,
                "cac": 400,
                "marketing_roi": 250,
                "gross_profit_margin": 70,
                "net_profit_margin": 15,
                "current_ratio": 2.0,
                "quick_ratio": 1.5,
                "inventory_turnover": 12,
                "days_sales_outstanding": 45
            },
            "B2C E-commerce": {
                "total_addressable_audience": 500000,
                "cac": 30,
                "marketing_roi": 400,
                "gross_profit_margin": 45,
                "net_profit_margin": 10,
                "current_ratio": 1.8,
                "quick_ratio": 1.2,
                "inventory_turnover": 8,
                "days_sales_outstanding": 30
            },
            # Add other industries with their benchmarks
        }
        return benchmarks.get(industry, {}).get(metric, 0)

    def _assess_risks(self, scores):
        risks = []
        for category, score in scores.items():
            if score < 5:
                risks.append(f"High risk in {category.replace('_', ' ')}: Score {score:.1f}/10")
            elif score < 7:
                risks.append(f"Moderate risk in {category.replace('_', ' ')}: Score {score:.1f}/10")
        return risks if risks else ["No significant risks identified"]
def create_radar_chart(category_scores):
    categories = list(category_scores.keys())
    values = list(category_scores.values())
    values.append(values[0])
    categories.append(categories[0])

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Business Score'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False
    )

    return fig

def create_risk_gauge(score):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 10]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 4], 'color': "red"},
                {'range': [4, 7], 'color': "yellow"},
                {'range': [7, 10], 'color': "green"}
            ],
        }
    ))
    return fig
def get_missing_key_metrics(data, category):
    key_metrics = {
        'marketing': [
            'market_share',
            'customer_acquisition_cost',
            'marketing_roi',
            'brand_recognition'
        ],
        'sales': [
            'revenue_growth',
            'pipeline_conversion',
            'average_deal_size'
        ]
        # Add other categories as needed
    }
    
    return [metric for metric in key_metrics.get(category, [])
            if metric not in data or data[metric] is None]
def display_enhanced_recommendations(report, data):
    st.header("Analysis & Recommendations")
    
    # Create tabs for different aspects of recommendations
    tab1, tab2, tab3 = st.tabs(["Key Recommendations", "Data Quality", "Industry Benchmarks"])
    
    with tab1:
        # Changed this section to handle recommendations as a list
        st.subheader("Recommendations")
        for rec in report['recommendations']:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"{rec['indicator']} {rec['text']}")
            with col2:
                st.markdown(f"**{rec['confidence_level']}**")
                
            with st.expander("See Details"):
                st.write(f"Confidence Score: {rec['confidence_score']:.2f}")
                st.progress(rec['confidence_score'])
    
    with tab2:
        st.subheader("Data Quality Analysis")
        analyzer = RecommendationAnalyzer()
        
        # Changed this to use scores instead of recommendations
        for category in report['category_scores'].keys():
            quality_score = analyzer.calculate_data_quality_score(data, category)
            st.metric(
                f"{category.title()} Data Quality",
                f"{quality_score*100:.1f}%",
                delta=None
            )
            
            with st.expander("How to improve data quality"):
                st.write("To improve confidence in recommendations:")
                missing_metrics = get_missing_key_metrics(data, category)
                for metric in missing_metrics:
                    st.write(f"- Add data for: {metric}")
    
    with tab3:
        st.subheader("Industry Benchmarks")
        industry = data.get('industry', 'General')
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Industry Avg CAC", 
                     f"${report.get('benchmarks', {}).get('cac', 0)}", 
                     delta=f"{data.get('customer_acquisition_cost', 0) - report.get('benchmarks', {}).get('cac', 0):.0f}")
        with col2:
            st.metric("Industry Avg ROAS",
                     f"{report.get('benchmarks', {}).get('roas', 0)}x",
                     delta=f"{data.get('marketing_roi', 0) - report.get('benchmarks', {}).get('roas', 0):.1f}")
def main():
    st.write("Debug: Application Starting")
    st.title("Business Viability & Scalability Analysis Tool")

    analyzer = BusinessAnalysisTool()

    tab1, tab2 = st.tabs(["Input Metrics", "Analysis Results"])

    with tab1:
        st.header("Business Metrics Input")
        
        with st.form("business_metrics_form"):
            st.subheader("Marketing and Sales Metrics")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Marketing Metrics")
                inputs = {}
                inputs['total_addressable_audience'] = st.number_input(
                    "Total Addressable Audience",
                    help="Total number of potential customers in your target market",
                    min_value=0,
                    max_value=10000000,
                    value=10000
                )
                inputs['campaign_effectiveness'] = st.slider(
                    "Campaign Effectiveness (1-10)",
                    help="Overall effectiveness of your marketing campaigns",
                    min_value=1,
                    max_value=10,
                    value=7
                )
                inputs['customer_acquisition_cost'] = st.number_input(
                    "Customer Acquisition Cost ($)",
                    help="Average cost to acquire a new customer",
                    min_value=0,
                    max_value=10000,
                    value=500
                )
                inputs['conversion_rate'] = st.slider(
                    "Conversion Rate (%)",
                    help="Percentage of leads that convert to customers",
                    min_value=0,
                    max_value=100,
                    value=25
                )
                inputs['marketing_roi'] = st.number_input(
                    "Marketing ROI (%)",
                    help="Return on Marketing Investment",
                    min_value=0,
                    max_value=1000,
                    value=150
                )
            
            with col2:
                st.markdown("#### Financial Metrics")
                inputs['gross_profit_margin'] = st.slider(
                    "Gross Profit Margin (%)",
                    help="(Revenue - COGS) / Revenue × 100",
                    min_value=-100,
                    max_value=100,
                    value=65
                )
                inputs['net_profit_margin'] = st.slider(
                    "Net Profit Margin (%)",
                    help="Net Profit / Revenue × 100",
                    min_value=-100,
                    max_value=100,
                    value=15
                )
                inputs['current_ratio'] = st.number_input(
                    "Current Ratio",
                    help="Current Assets / Current Liabilities",
                    min_value=0.0,
                    max_value=10.0,
                    value=2.5
                )
                inputs['quick_ratio'] = st.number_input(
                    "Quick Ratio",
                    help="(Current Assets - Inventory) / Current Liabilities",
                    min_value=0.0,
                    max_value=10.0,
                    value=1.8
                )
                inputs['debt_to_equity'] = st.number_input(
                    "Debt to Equity Ratio",
                    help="Total Debt / Total Equity",
                    min_value=0.0,
                    max_value=10.0,
                    value=1.0
                )

            st.markdown("#### Operational Metrics")
            col3, col4 = st.columns(2)
            
            with col3:
                inputs['cash_flow_operations'] = st.number_input(
                    "Operating Cash Flow ($)",
                    help="Cash generated from core business operations",
                    min_value=-1000000,
                    max_value=1000000,
                    value=100000
                )
                inputs['inventory_turnover'] = st.number_input(
                    "Inventory Turnover Ratio",
                    help="Cost of Goods Sold / Average Inventory",
                    min_value=0.0,
                    max_value=50.0,
                    value=12.0
                )
                inputs['days_sales_outstanding'] = st.number_input(
                    "Days Sales Outstanding",
                    help="(Accounts Receivable / Total Credit Sales) × 365",
                    min_value=0,
                    max_value=365,
                    value=45
                )

            # Add default values
            inputs.update(default_fields)

            submitted = st.form_submit_button("Generate Analysis")
            if submitted:
                # Generate report
                report = analyzer.generate_comprehensive_report(inputs)
                st.session_state.report = report
                st.session_state.inputs = inputs

    with tab2:
        if 'report' in st.session_state:
            report = st.session_state.report
            inputs = st.session_state.inputs
            
            # Display overall scores
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Overall Performance")
                gauge_chart = create_risk_gauge(report['overall_score'])
                st.plotly_chart(gauge_chart)

                st.metric("Viability Rating", report['viability_rating'])
                st.metric("Scalability Rating", report['scalability_rating'])

            with col2:
                st.subheader("Category Performance")
                radar_chart = create_radar_chart(report['category_scores'])
                st.plotly_chart(radar_chart)

            # Display enhanced recommendations
            display_enhanced_recommendations(report, inputs)

if __name__ == "__main__":
    main()
