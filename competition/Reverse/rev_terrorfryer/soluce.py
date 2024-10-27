flag_melange="1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB60tuarun0c_tr1y3"
print(len(flag_melange))

flag_test="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"
tf_melange = "TzHLVAnNpJbkdlOsuaCSGwtyIUeojKgcQqmiMhBxRDfErFvP"

result = []
for char in flag_test:
	i = 0
	for c in tf_melange:
		if c == char:
			result += [i]
			break
		i+=1

flag = ""
for r in result:
	flag += flag_melange[r]

print(flag)
