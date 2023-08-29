# teorie o cyklech

parts = ["jedna", "dva", "tři"] #jakoby body_parts. jednička je vyřešena, potřebuji od dva řešit tak aby se nedotkla operace jedničky, protože je už vyřešená

# jak to vyřešit má několik řešení:
# jedna z variant je jít odzadu

for index in range(len(parts)-1, 0, -1): #vypasání pozadu, bez kroku -1 to nefunguje
    print(parts[index])
    print(index)