function solution(s1, s2) {
    var count = 0;
    s1 = s1.split('');
    s2 = s2.split('');
    
    s1.forEach(e => {
      if (s2.includes(e)) {
        count++;
        s2.splice(s2.indexOf(e), 1);
      }
    });
        
    return count;
}

// Given two strings, find the number of common characters between them.