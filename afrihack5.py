def find_missing_letter(chars):
    holder = []
    final = []
    for i in range(1,len(chars)):
        if ord(chars[i]) == ord(chars[i-1])+1:
            holder.append(chars[i])
        else:
            final.append(chr(ord(chars[i-1])+1))
    return final[0]