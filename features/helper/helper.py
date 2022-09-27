
#Converting string TL price to float
def tl_to_float(self):
    return float(self.replace(" TL", "").replace(".", "").replace(",", "."))