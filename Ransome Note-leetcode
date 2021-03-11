class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_mapping = {}
        m_mapping = {}
        
        
        for i in ransomNote:
            if i not in r_mapping:
                r_mapping[i] = 1
            else:
                r_mapping[i] += 1
        for i in magazine:
            if i not in m_mapping:
                m_mapping[i] = 1
            else:
                m_mapping[i] += 1
        if len(r_mapping.keys())>len(m_mapping.keys()):
            return False
        
        for key, value in r_mapping.items():
            if key not in m_mapping or value > m_mapping[key]:
                return False
        return True    
