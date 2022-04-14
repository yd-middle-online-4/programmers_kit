fahrenheit = 77

def fahrenheit_to_celsius(fahrenheit):
    return int((fahrenheit-32)/1.8)

print(fahrenheit_to_celsius(fahrenheit))

# 섭씨 => 화씨 공식 : (x°C × 9/5) + 32 = y°F
# 화씨 => 섭씨 공식 : (x°F − 32) × 5/9 = y°C