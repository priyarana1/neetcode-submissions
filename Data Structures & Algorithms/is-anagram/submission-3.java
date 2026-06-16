class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        

        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            sMap.put(c1, sMap.getOrDefault(c1, 0) + 1);

            char c2 = t.charAt(i);
            tMap.put(c2, tMap.getOrDefault(c2,0) + 1);
        }

        return (sMap.equals(tMap));



    }
}
