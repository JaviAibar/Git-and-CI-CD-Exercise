import pytest
from exercise341 import process_checkout_system

def test_exercise341():
    # Datos de prueba
    data = [
        2, 2, 
        10, 5,
        2, 2,
        5, 10,
        3, 2,
        5, 10
    ]
    
    # Resultado esperado para los datos de prueba
    expected_result = [3, 1, 2]
    
    # Llamada a la función y verificación del resultado
    result = process_checkout_system(data)
    assert result == expected_result

if __name__ == "__main__":
    pytest.main()
