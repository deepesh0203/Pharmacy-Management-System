"""
HashTable data structure implemented using separate chaining.
The following functions are possible:
	1. items () -- Returns a list containing (key, value) tuples.
	2. keys () -- Returns a list containing keys.
	3. values () -- Returns a list containing values.
	4. hash_table[key] = value -- Inserts a key-value pair. Updates existing value.
	5. hash_table[key] -- Returns the value stored at key.
	6. remove(key) -- Removes the key-value pair stored at key and returns the value.
"""
INITIAL_CAPACITY = 51

# Node data structure - essentially a LinkedList node
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)
# Hash table with separate chaining
class HashTable:
	# Initialize hash table
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity
	# Get the hashtable in the form of (key, value) tuples in list
	def items(self):
		items=[]
		for node in self.buckets:
			while node is not None:
				items.append((node.key,node.value))
				node=node.next
		return items
	def keys(self):
		keys=[]
		for node in self.buckets:
			while node is not None:
				keys.append(node.key)
				node=node.next
		return keys
	def values(self):
		values=[]
		for node in self.buckets:
			while node is not None:
				values.append(node.value)
				node=node.next
		return values
	def __str__(self):
		return str(self.items())		
	# Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity	
	def hash(self, key):
		hashsum = 0
		# For each character in the key
		for idx, c in enumerate(key):
			# Add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			# Perform modulus to keep hashsum in range [0, self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	# Input:  key - string
	# 		  value - anything
	# Output: void
	def __setitem__(self, key, value):
		# 1. Check if key already exists
		existingItem=self[key]
		# 2. Compute index of key
		index = self.hash(key)
		# Go to the node corresponding to the hash
		node = self.buckets[index]
		# 3. If bucket is empty:
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return
		# 4. Iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		if existingItem is not None:
			prev.value=value # size remains same
		else:
			prev.next = Node(key, value)
			self.size+=1 # increment size

	# Find a data value based on key
	# Input:  key - string
	# Output: value stored under "key" or None if not found
	def __getitem__(self, key):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return None
		else:
			# Found - return the data value
			return node.value

	# Remove node stored at key
	# Input:  key - string
	# Output: removed data value or None if not found
	def remove(self, key):
		# 1. Compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# 2. Iterate to the requested node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# Now, node is either the requested node or none
		if node is None:
			# 3. Key not found
			return None
		else:
			# 4. The key was found.
			self.size -= 1
			result = node.value
			# Delete this element in linked list
			if prev is None:
				self.buckets[index] = node.next # May be None, or the next match
			else:
				prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result 
			return result
med_dict=HashTable()

#med_dict[medicine name]=[box no,quantity available,price of medicine,expiry date]
med_dict["crocin"]=[1,70,10,"17/12/2022"]
med_dict["digene"]=[2,30,20,"05/02/2023"]
med_dict["paracetemol"]=[3,20,5,"02/07/2021"]
med_dict["dolo"]=[4,50,15,"21/05/2023"]
med_dict["amoxicillin"]=[5,45,10,"02/06/2024"]
med_dict["baclofen"]=[6,3,25,"20/12/2025"]
med_dict["carmustine"]=[7,15,9,"20/09/2026"]
med_dict["cephalexin"]=[8,26,6,"11/01/2021"]
med_dict["cefepime"]=[9,37,3,"17/11/2023"]
med_dict["dacarbazine"]=[10,34,4,"28/02/2020"]
med_dict["dopamine"]=[11,21,5,"30/10/2025"]
med_dict["doxorubicin"]=[12,2,8,"26/06/2023"]
med_dict["enoxaparin"]=[13,70,14,"03/09/2024"]
med_dict["erythromycin"]=[14,45,15,"08/04/2026"]
med_dict["fidaxomicin"]=[15,32,12,"29/09/2023"]
med_dict["gemcitabine"]=[16,90,31,"16/04/2025"]
med_dict["hydralazine"]=[17,8,7,"18/07/2024"]
med_dict["hydromorphone"]=[18,62,5,"03/03/2023"]
med_dict["immune globulin"]=[19,4,2,"06/11/2021"]
med_dict["l-glutamine"]=[20,12,1,"08/09/2023"]
med_dict["meperidine"]=[21,18,25,"15/12/2024"]
med_dict["methylphenidate"]=[22,45,14,"16/05/2024"]
med_dict["morphine"]=[23,66,14,"16/06/2025"]
med_dict["oxycodone"]=[24,21,3,"07/03/2024"]
med_dict["penicillin"]=[25,66,2,"09/12/2025"]
med_dict["promethazine"]=[26,30,25,"06/06/2024"]
med_dict["propoxyphene"]=[27,34,65,"02/02/2021"]
med_dict["ranitidine"]=[28,92,25,"22/06/2026"]
med_dict["ritonavir"]=[29,55,25,"26/01/2024"]
med_dict["sunitinib"]=[30,66,36,"06/09/2026"]
med_dict["stavudine"]=[31,14,4,"15/10/2023"]
med_dict["thioguanine"]=[32,8,5,"16/06/2025"]
med_dict["topotecan"]=[33,36,9,"09/08/2024"]
med_dict["tretinoin"]=[34,25,5,"27/07/2026"]
med_dict["vancomycin"]=[35,14,6,"25/09/2025"]
med_dict["voxelotor"]=[36,25,1,"16/09/2026"]
med_dict["warfarin"]=[37,95,14,"11/02/2028"]
med_dict["zidovudine"]=[38,55,25,"16/06/2024"]
med_dict["hydrocodone"]=[39,55,36,"09/06/2020"]
med_dict["metformin"]=[40,42,6,"03/05/2024"]
med_dict["losartan"]=[41,37,8,"16/09/2024"]
med_dict["albuterol"]=[42,24,10,"16/12/2026"]
med_dict["antihistamines"]=[43,16,36,"05/12/2026"]
med_dict["gabapentin"]=[44,17,8,"18/11/2025"]
med_dict["omeprazole"]=[45,29,7,"20/08/2023"]
med_dict["levothyroxine"]=[46,36,18,"21/04/2023"]
med_dict["atorvastatin"]=[47,25,16,"13/05/2023"]
med_dict["adalimumab"]=[48,14,17,"29/06/2024"]
med_dict["apixaban"]=[49,55,14,"31/03/2026"]
med_dict["etanercept"]=[50,4,25,"22/02/2022"]
