from datetime import date, timedelta,datetime

start_date = date(2025, 7, 1)
end_date = datetime.now().date()

delta_days = (end_date - start_date).days


for i in range(delta_days + 1):
        current_date = start_date + timedelta(days=i)

        format_start_date = current_date.strftime("%Y-%m-%d")
        format_end_date = current_date.strftime("%Y-%m-%d")
      
        url = f"?from={format_start_date}&to={format_end_date}"
        print(url)
    

