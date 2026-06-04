class StockSpanner:

    def __init__(self):
        self.stack = [] # Pair: (price, span)
                        # Stack only contains the next highest number, and the span of days between them
                        # So it only tracks the important numbers rather than holding the whole stock span

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price: # While the last price is less than or equal to the current price
            span += self.stack[-1][1] # Span is increased by the previous items span
            self.stack.pop() # Pop the last item off the stack, since the new price is all that we need

        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)