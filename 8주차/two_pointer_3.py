class ListNode(object):
    def __init__(self, val=0, check = 0, next=None):   # __init__ : ListNode 클래스의 생성자
        self.val = val  # 현재 노드의 data 정의
        self.check = check
        self.next = next   # 현재 노드에서 연결된(linked) 다음 노드 정의

    

    


class Solution(object):
    def deleteDuplicates(self, head):
        # add dummy and initialize all the pointers
        dummy = ListNode(0) 
        dummy.next = head 
        pre = dummy
        cur = head
        while cur: 
            if pre.val == cur.val:
                pre.next = cur.next
                pre.check = -1
            else:
                pre = cur
            cur = cur.next

        return dummy.next
    
num_list = [1, 2, 3, 3, 4, 4, 5]   # input

# input에 대한 연결리스트 정의
for i, num in enumerate(num_list):
    if i==0:
        head = ListNode(num)
        curr_node = head
    else:
        curr_node.next = ListNode(num)
        curr_node = curr_node.next

# 연결리스트가 잘 구현되었는지 첫 노드부터 순서대로 출력
print("Print all elements of the implemented linked list in order from the beginning(= head)")
node=head
while node:
    print(node.val)
    node=node.next
print("----------------------------------------------------------------------------------------------")

sol_node = Solution().deleteDuplicates(head = head)   # 중복 원소가 제거된 연결리스트 sol_node

result = []
while sol_node:
    if sol_node.check != -1:
        result.append(sol_node.val)
    sol_node=sol_node.next

print(f"After removing duplicates : {result}")   # 결과 출력
