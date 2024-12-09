class RecommendationAnalyzer:
    def __init__(self):
        self.confidence_thresholds = {
            'high': 0.8,
            'medium': 0.5,
            'low': 0.3
        }

    def calculate_data_quality_score(self, data, category):
        required_metrics = {
            'marketing': {
                'primary': ['market_share', 'customer_acquisition_cost', 'marketing_roi'],
                'secondary': ['brand_recognition', 'market_growth', 'competitive_advantage'],
                'supporting': ['total_addressable_market', 'conversion_rate']
            },
            'sales': {
                'primary': ['revenue_growth', 'pipeline_conversion', 'average_deal_size'],
                'secondary': ['recurring_revenue_percentage', 'sales_cycle_length'],
                'supporting': ['customer_retention', 'customer_satisfaction']
            }
        }

        metrics = required_metrics.get(category, {})
        scores = {
            'completeness': self._calculate_completeness(data, metrics),
            'accuracy': self._calculate_accuracy(data, metrics),
            'reliability': self._calculate_reliability(data, category)
        }

        weights = {'completeness': 0.4, 'accuracy': 0.4, 'reliability': 0.2}
        return sum(scores[k] * weights[k] for k in scores)

    def _calculate_completeness(self, data, metrics):
        primary_count = sum(1 for m in metrics.get('primary', []) if data.get(m) is not None)
        secondary_count = sum(1 for m in metrics.get('secondary', []) if data.get(m) is not None)
        
        primary_weight = 0.6
        secondary_weight = 0.4
        
        primary_score = primary_count / len(metrics.get('primary', [])) if metrics.get('primary') else 0
        secondary_score = secondary_count / len(metrics.get('secondary', [])) if metrics.get('secondary') else 0
        
        return (primary_score * primary_weight) + (secondary_score * secondary_weight)

    def _calculate_accuracy(self, data, metrics):
        accuracy_score = 0
        total_metrics = 0
        
        for metric in metrics.get('primary', []) + metrics.get('secondary', []):
            if metric in data:
                total_metrics += 1
                value = data[metric]
                accuracy_score += 1
                    
        return accuracy_score / total_metrics if total_metrics > 0 else 0

    def _calculate_reliability(self, data, category):
        reliability_score = 0
        data_source = data.get('data_source', 'manual')
        reliability_score += 0.7 if data_source == 'automatic' else 0.3
        
        data_age = data.get('data_age_months', 12)
        age_factor = max(0, 1 - (data_age / 12))
        reliability_score *= age_factor
        
        return reliability_score

    def get_confidence_level(self, quality_score):
        if quality_score >= self.confidence_thresholds['high']:
            return 'High'
        elif quality_score >= self.confidence_thresholds['medium']:
            return 'Medium'
        elif quality_score >= self.confidence_thresholds['low']:
            return 'Low'
        else:
            return 'Very Low'

    def format_recommendation(self, recommendation, confidence_score):
        confidence_level = self.get_confidence_level(confidence_score)
        confidence_indicator = {
            'High': '🟢',
            'Medium': '🟡',
            'Low': '🟠',
            'Very Low': '🔴'
        }
        
        return {
            'text': recommendation,
            'confidence_level': confidence_level,
            'confidence_score': confidence_score,
            'indicator': confidence_indicator[confidence_level]
        }
