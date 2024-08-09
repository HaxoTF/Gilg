class VisualTable:
    def __init__(self, headers:list[any], gap:int=1) -> None:
        self.headers = headers
        self.values  = []
        self.gap = gap
    
    def add_row(self, values:list[any]) -> None:
        if len(values)!=len(self.headers): raise ValueError("Too less or too much values")
        self.values.append(values)

    def __str__(self) -> str:
        
        best_sizes :list = []
        for h in self.headers:
            best_sizes.append(len(h))
        
        for row in self.values:
            for i in range(0, len(best_sizes)):
                best_sizes[i] = max(len(str(row[i])), best_sizes[i])
        
        head_text = " "
        for i in range(0, len(best_sizes)):
            head_text += str(self.headers[i]).ljust(best_sizes[i]+self.gap)
        
        value_text :list[str] = []
        for row in self.values:
            value_text.append(" ")
            for i in range(0, len(best_sizes)):
                value_text[-1] += str(row[i]).ljust(best_sizes[i]+self.gap)
        
        full_text = head_text+"\n\n" + "\n".join(value_text)
        return full_text