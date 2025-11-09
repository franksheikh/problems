class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)

        if "0000" in seen:
            return -1
        seen.add("0000")

        q = collections.deque([("0000",0)])

        while q:
            combo, steps = q.popleft()
            # [0,0,0,0] => strings
            list_combo = list(combo)

            if combo == target:
                return steps
            
            for i in range(4):
                num = int(list_combo[i])
                nf = str(num + 1) if num < 9 else "0"
                nb = str(num - 1) if num > 0 else "9"
                lf = "".join(list_combo[0:i]+[nf]+list_combo[i+1:])
                lb = "".join(list_combo[0:i]+[nb]+list_combo[i+1:])
                
                if not lf in seen:
                    seen.add(lf)
                    q.append((lf, steps + 1))
                if not lb in seen:
                    seen.add(lb)
                    q.append((lb, steps + 1))
        return -1

                

        

        