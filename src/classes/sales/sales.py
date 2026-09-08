"""
Sales analizer modul
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

from pydantic import BaseModel


# Модели Pydantic
class Product(BaseModel):
    """
    Product class
    """
    id: int
    name: str
    price: float

class Customer(BaseModel):
    """
    Customer class
    """
    id: int
    name: str

class Order(BaseModel):
    """
    Order class
    """
    id: int
    customer_id: int
    product_ids: list[int]

class SalesAnalyzer:
    """
    SalesAnalyzer class
    """
    def __init__(self,
                 products: list[Product],
                 customers: list[Customer],
                 orders: list[Order]
    ):
        self.products = products
        self.customers = customers
        self.orders = orders

    def analyze(self) -> dict:
        """
        Get an analytical summary
        """
        new_products = {}
        for product in self.products:
            new_products[product["id"]] = (product["name"], product["price"])

        new_customers = {}
        for cust in self.customers:
            new_customers[cust['id']] = cust["name"]

        sold_products = []
        customer_checks = defaultdict(list)
        for order in self.orders:
            sold_products += [new_products[prod][0] for prod in order["product_ids"]]
            # Цены позиций в одном заказе
            prices_in_check = [new_products[prod][1] for prod in order["product_ids"]]
            # Сумма чека покупателя
            customer_checks[new_customers[order["customer_id"]]].append(sum(prices_in_check))

        # Сколько куплено товаров
        cnt_products = Counter(sold_products)
        # Наименование товара, который покупали чаще всего
        popular_product = max(cnt_products, key=cnt_products.get, default=None)
        # Количество наиболее покупаемого товара
        sales_count = max(cnt_products.values(), default=0)
        # Средний чек в разрезе каждого покупателя
        avg_check_per_cust = [self.average(checks) for checks in customer_checks.values()]
        # Средний чек по всем покупателям
        avg_check = self.average(avg_check_per_cust)
        # Общая выручка
        total_revenue = sum(sum(checks) for checks in customer_checks.values())

        return {
         "popular_product": {"name": popular_product,
                             "sales_count": sales_count},
         "average_check": avg_check,
         "total_revenue": total_revenue
        }

    @staticmethod
    def average(numbers):
        """
        Calculate average value
        """
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)


def load_data(products_path: str,
              customers_path: str,
              orders_path: str
    ) -> SalesAnalyzer:
    """
    Load data
    """
    # Получаем путь к папке скрипта
    base_dir = Path(__file__).resolve().parent

    with open(base_dir / products_path, 'r', encoding='utf-8') as p:
        products = json.load(p)

    with open(base_dir / customers_path, 'r', encoding='utf-8') as c:
        customers = json.load(c)

    with open(base_dir / orders_path, 'r', encoding='utf-8') as o:
        orders = json.load(o)

    return SalesAnalyzer(products, customers, orders)


def print_results(analysis: dict):
    """
    Print an analytical summary
    """
    pop_product = analysis["popular_product"]["name"]
    sales_count = analysis["popular_product"]["sales_count"]
    avg_check = analysis["average_check"]
    total_revenue = analysis["total_revenue"]
    print(f"Самый популярный товар: {pop_product} ({sales_count} продажи)")
    print(f"Средний чек покупателя: {avg_check}")
    print(f"Общая выручка: {total_revenue}")


# Пример использования
if __name__ == "__main__":
    analyzer = load_data("products.json", "customers.json", "orders.json")
    analysis = analyzer.analyze()
    print_results(analysis)
