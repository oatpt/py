name=input("ชื่อ-คำโปรย : ")
print(name)
id=input("รหัสทรัพย์ : ")
print("♦️รหัสทรัพย์  "+id+"♦️")
print("------------------------------------------")
badroom=input("ห้องนอน : ")
bathroom=input("ห้องน้ำ : ")
livingroom=input("ห้องนั่งเล่น : ")
arearoom=input("พื้นที่ใช้สอย : ")
floor=input("ชั้นไหน : ")
building=input("ตึกไหน : ")
print("🔥 "+badroom+"ห้องนอน "+bathroom+"ห้องน้ำ "+badroom+"ห้องนั่งเล่น 🔥\nคอนโดมีพื้นที่ใช้สอย "+arearoom+" ตร.ม   ชั้น "+floor+"ตึก "+building)
price=input("ราคาเช่า : ")
print("⭕️ราคาเช่า  "+price+" บาท/เดือน")
Location=input("Location : ")
print("📌Location : "+Location)
print("------------------------------------------")
print("✨รายละเอียดห้อง ✨")
have_air=input("มีแอร์ไหม Y/N :")
if have_air in "Yy":
    air=input("มีแอร์กี่ตัว :")
    print("• แอร์ "+air+"ตัว")
have_fridge=input("มีตู้เย็นไหม Y/N :")
if have_fridge in "Yy":
    print("• ตู้เย็น")
have_waterheater=input("มีเครื่องทำน้ำอุ่นไหม Y/N :")
if have_waterheater in "Yy":
    print("• เครื่องทำน้ำอุ่น")
have_TV=input("มีTVไหม Y/N :")
if have_TV in "Yy":
    print("• TV")
temp='Y'
other=[]
while temp not in 'nN':
    temp=input("มีอย่างอื่นอีกไหมใช่พิมพ์มา ไม่มีพิมพ์ N :")
    print("• "+temp)
    other.append(temp)
other.pop()
print("------------------------------------------")
print("✨สิ่งอำนวยความสะดวก ✨")
facilities=[]
temp='Y'
while temp not in 'nN':
    temp=input("ใส่สิ่งอำนวยความสะดวก ไม่มีพิมพ์ N :")
    facilities.append(temp)
facilities.pop()
for i in facilities :
    print("• "+i)
print("------------------------------------------")
print("✨สถานที่สำคัญ ✨")
landmark=[]
temp='Y'
while temp not in 'nN':
    temp=input("ใส่สถานที่สำคัญ ไม่มีพิมพ์ N :")
    landmark.append(temp)
landmark.pop()
for i in landmark :
    print("- "+i)
print("*ราคา "+price+"บาท / เดือน ")
taboo=[]
temp='Y'
while temp not in 'nN':
    temp=input("ใส่ข้อห้าม ไม่มีพิมพ์ N :")
    taboo.append(temp)
taboo.pop()
if len(taboo)>0:
    print("หมายเหตุ : ",end=' ')
for i in taboo :
    print(i,end=' ')
lease=input("สัญญาเช่า : ")
print("♦️สัญญาเช่า  "+lease+"ปี ")
deposit=input("มัดจำ : ")
advancerental=input("ค่าเช่าล่วงหน้า : ")





print(name)
print("♦️รหัสทรัพย์  "+id+"♦️")
print("------------------------------------------")
print("🔥 "+badroom+"ห้องนอน "+bathroom+"ห้องน้ำ "+badroom+"ห้องนั่งเล่น 🔥\nคอนโดมีพื้นที่ใช้สอย "+arearoom+" ตร.ม   ชั้น "+floor)
print("⭕️ราคาเช่า  "+price+" บาท/เดือน")
print("📌Location : "+Location)
print("------------------------------------------")
print("✨รายละเอียดห้อง ✨")
if have_air in "Yy":
    print("• แอร์ "+air+"ตัว")
if have_fridge in "Yy":
    print("• ตู้เย็น")
if have_waterheater in "Yy":
    print("• เครื่องทำน้ำอุ่น")
if have_TV in "Yy":
    print("• TV")
for i in other :
    print("• "+i)
print("------------------------------------------")
print("✨สิ่งอำนวยความสะดวก ✨")
for i in facilities :
    print("• "+i)
print("------------------------------------------")
print("✨สถานที่สำคัญ ✨")
for i in landmark :
    print("- "+i)
print("*ราคา "+price+"บาท / เดือน ")
if len(taboo)>0:
    print("หมายเหตุ : ",end=' ')
for i in taboo :
    print(i,end=' ')
print("♦️สัญญาเช่า  "+lease+"ปี ")
print("*มัดจำ "+deposit+" เดือน, ค่าเช่าล่วงหน้า "+advancerental+" เดือน ")
print("📲Tel. 062-417-2624 (มูมู่ค่าา)")
print("Line : https://line.me/ti/p/6M7qoxEKr4")
print("Line ID: mu32776")
print("มูมู่ ยินดีให้บริการค่าา")
print("#รับฝากขายปล่อยเช่า #บ้านคอนโด  #ให้เช่าคอนโด #คอนโดติดรถไฟฟ้า #เช่าคอนโด #คอนโด #คอนโดแนวรถไฟฟ้า #คอนโดใกล้ห้าง")
