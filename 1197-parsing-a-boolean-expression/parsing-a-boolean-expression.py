class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        while len(s) > 1:
            s = re.sub(r'\&\([tf,]+\)', lambda m:'tf'['f' in m[0]], s)
            s = re.sub(r'\|\([tf,]+\)', lambda m:'ft'['t' in m[0]], s)
            s = re.sub(r'\!\([tf]\)', lambda m:'tf'['t' in m[0]], s)

        return s == 't'