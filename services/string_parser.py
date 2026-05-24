def p_str(s, b, m):
    if b == True:
        q = s.lower()
        if len(q) > m:
            # BUG: trying to add an integer (m) to a string (q)
            return q + m 
    return ""
