"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness 


def print_melon(name, price, seedless, flesh_color = {}, rind_color = {}, average_weight = {}):
    """Print each melon with corresponding attribute information."""
    inventory = {}
    for index, fruit in name.items():
        value = {}
        value['price'] = price.get(index,None)
        value['seedless'] = seedless.get(index, None)
        value['flesh_color'] = flesh_color.get(index, None)
        value['rind_color'] = rind_color.get(index, None)
        value['average_weight'] = average_weight.get(index, None)
        
        inventory[fruit.title()] = value
    
    for fruit, value in inventory.items():
        print(f"\n{fruit.upper()}")
        for category, value in value.items():
            print(f"{category}: {value}")

#call function 
print(print_melon(melon_names, melon_prices, melon_seedlessness))
