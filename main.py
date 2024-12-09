import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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
            'market_position': {
                'score': 0,
                'criteria': {
                    'market_share': data.get('market_share', 0) / 100 * 10,
                    'brand_recognition': data.get('brand_recognition', 0) / 100 * 10,
                    'competitive_advantage': data.get('competitive_advantage', 0) / 10
                }
            },
            'customer_acquisition': {
                'score': 0,
                'criteria': {
                    'cac': self._normalize_cac(data.get('customer_acquisition_cost', 0)),
                    'conversion_rate': data.get('conversion_rate', 0) / 100 * 10,
                    'marketing_roi': self._normalize_roi(data.get('marketing_roi', 0))
                }
            },
            'growth_potential': {
                'score': 0,
                'criteria': {
                    'market_growth': data.get('market_growth', 0) / 100 * 10,
                    'addressable_market': self._normalize_tam(data.get('total_addressable_market', 0))
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
                    'gross_margin': self._normalize_margin(data.get('gross_margin', 0)),
                    'net_margin': self._normalize_margin(data.get('net_margin', 0)),
                    'ebitda_margin': self._normalize_margin(data.get('ebitda_margin', 0))
                }
            },
            'liquidity': {
                'score': 0,
                'criteria': {
                    'current_ratio': self._normalize_ratio(data.get('current_ratio', 0)),
                    'quick_ratio': self._normalize_ratio(data.get('quick_ratio', 0)),
                    'cash_ratio': self._normalize_ratio(data.get('cash_ratio', 0))
                }
            },
            'growth': {
                'score': 0,
                'criteria': {
                    'revenue_growth': data.get('revenue_growth', 0) / 100 * 10,
                    'profit_growth': data.get('profit_growth', 0) / 100 * 10
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
                recommendations.append(self._get_category_recommendation(category, score))
        return recommendations

    def _get_category_recommendation(self, category, score):
        recommendations = {
            'marketing': "Focus on improving market positioning and customer acquisition efficiency",
            'sales': "Optimize sales process and enhance pipeline management",
            'product_delivery': "Streamline delivery process and improve quality controls",
            'operational_efficiency': "Implement process automation and optimize resource allocation",
            'financial_health': "Strengthen financial controls and improve cash management",
            'people': "Invest in talent development and enhance organizational culture"
        }
        return f"{category.replace('_', ' ').title()} ({score:.1f}/10): {recommendations[category]}"

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

def main():
    st.write("Debug: Application Starting")
    st.title("Business Viability & Scalability Analysis Tool")

    analyzer = BusinessAnalysisTool()

    tab1, tab2 = st.tabs(["Input Metrics", "Analysis Results"])

    with tab1:
        st.header("Business Metrics Input")

        col1, col2, col3 = st.columns(3)

        inputs = {}

        with col1:
            st.subheader("Marketing Metrics")
            inputs['market_share'] = st.slider("Market Share (%)", 0, 100, 15)
            inputs['brand_recognition'] = st.slider("Brand Recognition (%)", 0, 100, 60)
            inputs['competitive_advantage'] = st.slider("Competitive Advantage (1-10)", 1, 10, 7)
            inputs['customer_acquisition_cost'] = st.number_input("Customer Acquisition Cost ($)", 0, 10000, 500)
            inputs['conversion_rate'] = st.slider("Conversion Rate (%)", 0, 100, 25)
            inputs['marketing_roi'] = st.number_input("Marketing ROI (%)", 0, 1000, 150)
            inputs['market_growth'] = st.slider("Market Growth (%)", 0, 100, 20)
            inputs['total_addressable_market'] = st.number_input("Total Addressable Market ($)", 0, 1000000000, 500000000)

        with col2:
            st.subheader("Sales & Product Metrics")
            inputs['revenue_growth'] = st.slider("Revenue Growth (%)", 0, 100, 30)
            inputs['recurring_revenue_percentage'] = st.slider("Recurring Revenue (%)", 0, 100, 70)
            inputs['average_deal_size'] = st.number_input("Average Deal Size ($)", 0, 100000, 5000)
            inputs['pipeline_conversion'] = st.slider("Pipeline Conversion (%)", 0, 100, 20)
            inputs['sales_cycle_length'] = st.number_input("Sales Cycle Length (days)", 0, 365, 45)
            inputs['defect_rate'] = st.slider("Defect Rate (%)", 0, 100, 2)
            inputs['on_time_delivery'] = st.slider("On-Time Delivery (%)", 0, 100, 95)
            inputs['automation_percentage'] = st.slider("Automation Level (%)", 0, 100, 60)

        with col3:
            st.subheader("Financial & Operational Metrics")
            inputs['operating_margin'] = st.slider("Operating Margin (%)", -100, 100, 25)
            inputs['overhead_ratio'] = st.slider("Overhead Ratio (%)", 0, 100, 30)
            inputs['gross_margin'] = st.slider("Gross Margin (%)", -100, 100, 65)
            inputs['net_margin'] = st.slider("Net Margin (%)", -100, 100, 15)
            inputs['current_ratio'] = st.number_input("Current Ratio", 0.0, 10.0, 2.5)
            inputs['employee_satisfaction'] = st.slider("Employee Satisfaction (%)", 0, 100, 80)
            inputs['employee_retention'] = st.slider("Employee Retention (%)", 0, 100, 85)
            inputs['culture_rating'] = st.slider("Culture Rating (1-10)", 1, 10, 8)

        # Add remaining required fields with default values
        default_fields = {
            'product_satisfaction': 90,
            'sla_compliance': 98,
            'delivery_cost': 200,
            'cycle_time': 15,
            'capacity_utilization': 75,
            'process_automation': 70,
            'resource_utilization': 80,
            'error_rate': 3,
            'cost_per_unit': 50,
            'tech_stack_rating': 8,
            'infrastructure_scalability': 7,
            'ebitda_margin': 20,
            'quick_ratio': 1.8,
            'cash_ratio': 0.8,
            'profit_growth': 25,
            'skill_coverage': 75,
            'leadership_experience': 8,
            'succession_readiness': 7,
            'vision_rating': 8,
            'innovation_rating': 7
        }
        inputs.update(default_fields)

    with tab2:
            if st.button("Generate Analysis"):
                # Generate report
                report = analyzer.generate_comprehensive_report(inputs)

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

                # Display recommendations and risks
                col3, col4 = st.columns(2)

                with col3:
                    st.subheader("Recommendations")
                    for rec in report['recommendations']:
                        st.warning(rec)

                with col4:
                    st.subheader("Risk Assessment")
                    for risk in report['risk_assessment']:
                        if "High risk" in risk:
                            st.error(risk)
                        elif "Moderate risk" in risk:
                            st.warning(risk)
                        else:
                            st.success(risk)
if __name__ == "__main__":
    main()
