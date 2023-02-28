import csv
with open('products_data_all',encoding="utf8") as Base:
    base_read= csv.DictReader(Base)
    i=1
    new_base={}
    while i<190:
         for x in base_read:
             if x["id_product"]==(f"{i}"):
                i+=1

                new_base|=x
                print (new_base)





