main();

function solution(k, score) {
  var answer = -1;

  let map = new Map();
  let map2 = new Map();
  let diff = new Set();
  let index = new Set();

  for (let i = 1; i < score.length; i++) {
    let diff = score[i] - score[i - 1];
    map.set([i - 1, i], diff);
  }

  map.forEach((value, key) => {
    map2.set(value, (map2.get(value) || 0) + 1);
  });

  map2.forEach((value, key) => {
    if (value >= k) {
      diff.add(key);
    }
  });

  map.forEach((value, key) => {
    if (diff.has(value)) {
      index.add(key[0]);
      index.add(key[1]);
    }
  });

  answer = score.length - index.size;

  return answer;
}

function main() {
  let score = [24, 22, 20, 19, 16, 14, 8, 6];
  k = 3;

  console.log(solution(k, score));
}
