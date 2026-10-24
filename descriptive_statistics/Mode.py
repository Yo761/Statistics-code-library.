
from scipy import stats

def calculate_mode(data):
    result = stats.mode(data, keepdims=False)
    return result.mode

data = [10, 20, 20, 30, 40, 20, 50]

result = calculate_mode(data)
print("Mode:", result)  # 20
