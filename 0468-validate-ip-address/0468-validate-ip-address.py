class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            ips = queryIP.split(".")
            if len(ips) != 4:
                return "Neither"
            
            for i in range(len(ips)):
                try:
                    if (not (1 <= len(ips[i]) <= 4)) or len(ips[i]) != len(str(int(ips[i]))) or (not (0 <= int(ips[i]) <= 255)):
                        return "Neither"
                except:
                    return "Neither"
            
            return "IPv4"
        
        else:
            ips = queryIP.split(":")
            if len(ips) != 8:
                return "Neither"
            
            for i in range(len(ips)):
                if not (1 <= len(ips[i]) <= 4):
                    return "Neither"

                for string in ips[i]:
                    if string not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]:
                        return "Neither"
            
            return "IPv6"

                
