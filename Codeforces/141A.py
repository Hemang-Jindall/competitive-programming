guest_name = input()
host_name = input()
pile = input()
full_list = guest_name + host_name
if sorted(full_list) == sorted(pile):
    print("YES")
else:
    print("NO")