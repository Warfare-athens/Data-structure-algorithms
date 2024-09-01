https://leetcode.com/problems/online-stock-span/description/


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span



  """
Consider the input prices: `[100, 80, 60, 70, 60, 75, 85]`.

### Day 1: Price = 100
- **Stack before operation**: `[]`
- **Operation**: The stack is empty, so push `(100, 1)` onto the stack. The span for day 1 is `1` (since it’s just today).
- **Stack after operation**: `[(100, 1)]`
- **Result so far**: `[1]`

### Day 2: Price = 80
- **Stack before operation**: `[(100, 1)]`
- **Operation**: The price `80` is less than `100` (the price at the top of the stack). So, we push `(80, 1)` onto the stack. The span for day 2 is `1` (just today).
- **Stack after operation**: `[(100, 1), (80, 1)]`
- **Result so far**: `[1, 1]`

### Day 3: Price = 60
- **Stack before operation**: `[(100, 1), (80, 1)]`
- **Operation**: The price `60` is less than `80` (the top of the stack). So, we push `(60, 1)` onto the stack. The span for day 3 is `1` (just today).
- **Stack after operation**: `[(100, 1), (80, 1), (60, 1)]`
- **Result so far**: `[1, 1, 1]`

### Day 4: Price = 70
- **Stack before operation**: `[(100, 1), (80, 1), (60, 1)]`
- **Operation**: The price `70` is greater than `60` (the top of the stack). Therefore, we **pop** `(60, 1)` from the stack. The current span becomes `1 + 1 = 2` (since today’s price covers two days: today and the previous day with price `60`).
- Now, `70` is less than `80` (the new top of the stack), so we stop popping and push `(70, 2)` onto the stack.
- **Stack after operation**: `[(100, 1), (80, 1), (70, 2)]`
- **Result so far**: `[1, 1, 1, 2]`

### Day 5: Price = 60
- **Stack before operation**: `[(100, 1), (80, 1), (70, 2)]`
- **Operation**: The price `60` is less than `70` (the top of the stack). So, we push `(60, 1)` onto the stack. The span for day 5 is `1` (just today).
- **Stack after operation**: `[(100, 1), (80, 1), (70, 2), (60, 1)]`
- **Result so far**: `[1, 1, 1, 2, 1]`

### Day 6: Price = 75
- **Stack before operation**: `[(100, 1), (80, 1), (70, 2), (60, 1)]`
- **Operation**: The price `75` is greater than `60`, so we **pop** `(60, 1)` from the stack and add its span to the current span (`span = 1 + 1 = 2`).
- Next, `75` is also greater than `70`, so we **pop** `(70, 2)` from the stack and add its span to the current span (`span = 2 + 2 = 4`).
- Now, `75` is less than `80`, so we stop popping and push `(75, 4)` onto the stack.
- **Stack after operation**: `[(100, 1), (80, 1), (75, 4)]`
- **Result so far**: `[1, 1, 1, 2, 1, 4]`

### Day 7: Price = 85
- **Stack before operation**: `[(100, 1), (80, 1), (75, 4)]`
- **Operation**: The price `85` is greater than `75`, so we **pop** `(75, 4)` from the stack and add its span to the current span (`span = 1 + 4 = 5`).
- Next, `85` is also greater than `80`, so we **pop** `(80, 1)` from the stack and add its span to the current span (`span = 5 + 1 = 6`).
- Now, `85` is less than `100`, so we stop popping and push `(85, 6)` onto the stack.
- **Stack after operation**: `[(100, 1), (85, 6)]`
- **Result so far**: `[1, 1, 1, 2, 1, 4, 6]`

### Final Result:
The span for each day is `[1, 1, 1, 2, 1, 4, 6]`.
"""
      
