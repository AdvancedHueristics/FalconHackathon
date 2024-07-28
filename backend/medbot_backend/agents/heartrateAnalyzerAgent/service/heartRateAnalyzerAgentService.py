from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from medbot_backend.models import HeartRate

class heartRateAnalyzerService:
    def fetch_heart_rate_data(userId):
        heart_rate_records = HeartRate.objects.filter(user_id=userId).order_by('recorded_at')
        heart_rates = []
        times = []
        for record in heart_rate_records:
            heart_rates.append(record.heart_rate)
            times.append(record.recorded_at.strftime('%Y-%m-%d %H:%M:%S'))
        return {
            'times': times,
            'heart_rates': heart_rates
        }    

