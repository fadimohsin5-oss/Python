def num_notes (a):
    Q= [2000, 1000, 500, 200, 100, 50, 20, 10]
    x=0
    for i in range(8):
        q = Q[i]
        x = a//q
        print("Notes of {} = {}".format(q, x))
        a = a%q

amount = int(input("Enter Total Amount"))
num_notes (amount)