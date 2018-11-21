invitationList =['习近平','彭丽媛','江泽民']
print(invitationList[0]+"我想邀请你吃饭")
print(invitationList[1]+"我想邀请你吃饭")
print(invitationList[2]+"我想邀请你吃饭")

print("\n"+invitationList[1]+"今晚来不了了")
invitationList[1] ='胡锦涛'
print(invitationList[0]+"我想邀请你吃饭")
print(invitationList[1]+"我想邀请你吃饭")
print(invitationList[2]+"我想邀请你吃饭")

print("\n我找到个更大的餐桌")
invitationList.insert(0,'温家宝')
invitationList.insert(1,'毛泽东')
invitationList.append('汪洋')
print(invitationList[0]+"我想邀请你吃饭")
print(invitationList[1]+"我想邀请你吃饭")
print(invitationList[2]+"我想邀请你吃饭")
print(invitationList[3]+"我想邀请你吃饭")
print(invitationList[4]+"我想邀请你吃饭")
print(invitationList[5]+"我想邀请你吃饭")
print("我邀请了"+str(len(invitationList))+"位")

print("\n我只能邀请两位来了")
print(invitationList.pop(0)+"抱歉我无法邀请你来了")
print(invitationList.pop(0)+"抱歉我无法邀请你来了")
print(invitationList.pop(1)+"抱歉我无法邀请你来了")
print(invitationList.pop(2)+"抱歉我无法邀请你来了")

print("\n"+invitationList[0]+"我仍想邀请你吃饭")
print(invitationList[1]+"我仍想邀请你吃饭")

del invitationList[0]
del invitationList[0]
print(invitationList)
