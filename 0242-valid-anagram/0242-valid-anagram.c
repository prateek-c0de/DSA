bool isAnagram(char* s, char* t) {
    if (strlen(s) != strlen(t))
        return false;

    int arr[26] = {0};

    for (int i = 0; s[i] != '\0'; i++) {
        arr[s[i] - 'a']++;
        arr[t[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++) {
        if (arr[i] != 0)
            return false;
    }

    return true;
}