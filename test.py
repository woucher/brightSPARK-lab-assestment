class geeks:
    course = 'DSA'
  
    def purchase(obj):
        print("Puchase course : ", obj.course)
  
  
geeks.purchase = staticmethod(geeks.purchase)
geeks.purchase()