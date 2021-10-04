amount=int(input("enter the price"))
if amount<1000:
    discount=amount*0.05
    print("discount :",discount)

elif amount<5000:
    discount=amount*0.10
    print("discount :",discount)

else:
    discount=amount*0.15
    print("discount:",discount)

print("Net payable amount :",amount-discount)