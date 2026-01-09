"""Calculator module met basis bewerkingen."""


class Calculator:
    """Eenvoudige calculator class."""
    
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Kan niet delen door nul")
        return a / b
    
    def is_prime(self, n: int) -> bool:
        """Check of een getal een priemgetal is."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
