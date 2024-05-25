Evaluatorid = int(input("Evaluator ID:"))
HTnumber= int(input("HT number:"))
sub1=int(input("English:"))
sub2=int(input("Maths:"))
sub3=int(input("Physics:"))
sub4=int(input("Biology:"))
sub5=int(input("Social:"))
total=sub1+sub2+sub3+sub4+sub5
print("Total score :",total)
percentage=(total/500)*100
print("Percentage :",percentage)
if percentage>=75:
      print("Grade A")
elif percentage>=60:
      print("Grade B")
elif percentage>=50:
      print("Grade C")
else:
      print("Fail")
