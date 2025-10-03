'''

A <- B - C - D
n

save => C - D
node.next.next = node => B -> A
node.next = save.next => A -> D
node = save => C -> D
















A - B - C - D - E - F
B - A
SAVE C - D
A -> D
SWAP D and C

B - A - D - C -> F -> E
SAVE E - F
C -> F
SWAP E and F
F -> E
head = save
B - A - D - C -> F -> E


A    <-      B    x     C		   <- 			D
			           nextNode
					   head
					   prev


A -> D


---

while head and head.next:
if prev:
	prev.next = head.next

prev = head
nextNode = head.next.next
head.next.next -> head
head -> nextNode





'''