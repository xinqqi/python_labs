price=float(input())
discount=float(input())
vat=float(input())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print("База после скидки: %.2f" %(base))
print("НДС:               %.2f" %(vat_amount))
print("Итого к оплате:    %.2f" %(total))