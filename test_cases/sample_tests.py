def test_add_positive(student_module):
    """Test add function with positive numbers"""
    return student_module.add(2, 3) == 5

def test_add_negative(student_module):
    """Test add function with negative numbers"""
    return student_module.add(-2, -3) == -5

def test_add_mixed(student_module):
    """Test add function with mixed numbers"""
    return student_module.add(-2, 5) == 3
