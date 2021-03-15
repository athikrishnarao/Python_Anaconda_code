"""a=int(input("enter number"))
if a>1:
   for x in range(2,a):
      if(a%x)==0:
          print("not prime")
            break
    else:
        print("Prime")
else:
    print("not prime")"""

class airport:
    def checkin(self):
        name = input("What is Your Name : ")
        flight_name = input("Flight Name : ")
        boarding_time = int(input("Boarding Time :" ))
        print(name,flight_name,boarding_time)
        self.boardingpass()
    def boardingpass(self):
        ticket_no = int(input("Enter the Flight Ticket No : "))
athi = airport()
athi.checkin()
#athi.boardingpass()