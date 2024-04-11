function solution(my_string) {
    var answer = '';
    
    const vowel = ["a", "e", "i", "o", "u"];
    
    for (ms of my_string) {
        if (vowel.indexOf(ms) == -1) {
            answer += ms;
        }  
    }
    return answer;
}