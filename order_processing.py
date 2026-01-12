from typing import Dict, List, Tuple, Optional

class OrderConstants:
    """Константы для обработки заказов"""
    DEFAULT_CURRENCY = "USD"
    TAX_RATE = 0.21
    MIN_TOTAL_AFTER_DISCOUNT = 0
    
    COUPON_RULES = {
        "SAVE10": {"type": "percentage", "value": 0.10},
        "SAVE20": {"type": "tiered", "high": 0.20, "low": 0.05, "threshold": 200},
        "VIP": {"type": "fixed_conditional", "value": 50, "fallback": 10, "min_for_value": 100},
    }

def parse_request(request: Dict):
    return (
        request.get("user_id"),
        request.get("items"),
        request.get("coupon"),
        request.get("currency"),
    )

def validate_request(user_id, items, currency):
    if user_id is None:
        raise ValueError("user_id is required")
    if items is None:
        raise ValueError("items is required")
    if not isinstance(items, list):
        raise ValueError("items must be a list")
    if len(items) == 0:
        raise ValueError("items must not be empty")
    
    for item in items:
        if "price" not in item or "qty" not in item:
            raise ValueError("item must have price and qty")
        if item["price"] <= 0:
            raise ValueError("price must be positive")
        if item["qty"] <= 0:
            raise ValueError("qty must be positive")
    
    return currency if currency is not None else OrderConstants.DEFAULT_CURRENCY

def calculate_subtotal(items: List[Dict]) -> int:
    return sum(item["price"] * item["qty"] for item in items)

def calculate_discount(subtotal: int, coupon: Optional[str]) -> int:
    if not coupon:
        return 0
    
    if coupon not in OrderConstants.COUPON_RULES:
        raise ValueError("unknown coupon")
    
    rule = OrderConstants.COUPON_RULES[coupon]
    
    if rule["type"] == "percentage":
        return int(subtotal * rule["value"])
    
    elif rule["type"] == "tiered":
        rate = rule["high"] if subtotal >= rule["threshold"] else rule["low"]
        return int(subtotal * rate)
    
    elif rule["type"] == "fixed_conditional":
        return rule["value"] if subtotal >= rule["min_for_value"] else rule["fallback"]
    
    return 0

def calculate_tax_and_total(subtotal: int, discount: int) -> Tuple[int, int]:
    total_after_discount = max(subtotal - discount, OrderConstants.MIN_TOTAL_AFTER_DISCOUNT)
    tax = int(total_after_discount * OrderConstants.TAX_RATE)
    total = total_after_discount + tax
    return tax, total

def generate_order_id(user_id: int, items_count: int) -> str:
    return f"{user_id}-{items_count}-X"

def process_checkout(request: Dict) -> Dict:
    user_id, items, coupon, currency = parse_request(request)
    currency = validate_request(user_id, items, currency)
    
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, coupon)
    tax, total = calculate_tax_and_total(subtotal, discount)
    
    return {
        "order_id": generate_order_id(user_id, len(items)),
        "user_id": user_id,
        "currency": currency,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
        "items_count": len(items),
    }
