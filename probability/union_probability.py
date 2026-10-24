
def calculate_union(p_a, p_b, p_intersection):
    return p_a + p_b - p_intersection

p_a = 0.5
p_b = 0.4
p_intersection = 0.2

result = calculate_union(p_a, p_b, p_intersection)
print("P(A or B):", result)  # 0.7
