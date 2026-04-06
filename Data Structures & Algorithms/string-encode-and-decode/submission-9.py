class Solution:

    def encode(self, strs: List[str]) -> str:
        final_encoded = ''
        for word in strs:
            encoded = ''
            for letter in word:
                encoded += letter
            encoded += '~'
            final_encoded += encoded
        return final_encoded

    def decode(self, s: str) -> List[str]:
        final_decoded = []
        decoded = ''
        for letter in s:
            if letter == '~':
                final_decoded.append(decoded)
                decoded =''
                continue
            else:
                decoded += letter
        return final_decoded
