def total_calc(bill_amt,tip_perc):
#define function to calculate tip
    total = bill_amt*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")
# specify only bill_amt
# default value on tip percentage is used
total_calc(320,25)